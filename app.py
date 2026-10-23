from flask import Flask, request, jsonify, send_file, send_from_directory, session, redirect, make_response
from flask_cors import CORS
import os
import uuid
import time
import io
import json
import random
import requests
from datetime import datetime
from dotenv import load_dotenv

import sqlite3
import cv2
import numpy as np
import base64
import hashlib
from flask import session, redirect
from face_service import get_face_embedding
from face_match import find_user
from fer import FER
import smtplib
from email.mime.text import MIMEText
import secrets

emotion_detector = FER(mtcnn=True)

EMOTION_STRESS_WEIGHTS = {
    'angry': 1.0,
    'fear': 1.0,
    'sad': 0.8,
    'disgust': 0.6,
    'surprise': 0.3,
    'neutral': 0.15,
    'happy': 0.0
}

def compute_real_stress_from_image(image):
    try:
        results = emotion_detector.detect_emotions(image)
        print(f"[EMOTION] Faces found: {len(results) if results else 0}")
        if not results:
            return None, None
        emotions = results[0]['emotions']
        weighted_sum = sum(
            prob * EMOTION_STRESS_WEIGHTS.get(emotion, 0.0)
            for emotion, prob in emotions.items()
        )
        stress_score = max(0, min(100, round(weighted_sum * 100)))
        dominant_emotion = max(emotions, key=emotions.get)
        return stress_score, dominant_emotion
    except Exception as e:
        print(f"[EMOTION] Detection failed: {e}")
        return None, None

app = Flask(__name__, static_folder='static')
app.secret_key = 'mindmate_secret_key_2026'


# Top login removed

# Protect main page (optional)

# Try to import gTTS, show error if not installed
try:
    from gtts import gTTS # type: ignore
    GTTS_AVAILABLE = True
    print("[OK] gTTS loaded successfully")
except ImportError:
    GTTS_AVAILABLE = False
    print("[ERROR] gTTS not installed! Run: pip install gtts")
# Try to import SarvamAI Python SDK
try:
    from sarvamai import SarvamAI # type: ignore
    SARVAM_SDK_AVAILABLE = True
    print("[OK] SarvamAI SDK loaded successfully")
except ImportError:
    SARVAM_SDK_AVAILABLE = False
    print("[WARNING] SarvamAI SDK not installed. Falling back to direct REST requests.")
load_dotenv()
CORS(app)
# Create necessary folders
os.makedirs('static', exist_ok=True)
os.makedirs('temp', exist_ok=True)
os.makedirs('data', exist_ok=True)
# Local database file paths
HISTORY_FILE = 'data/history.json'
STRESS_DATA_FILE = 'data/stress_data.json'

# ============================================
# ADMIN DB INIT (runs once at startup)
# ============================================
def init_admin_tables():
    """Creates the admins table if it doesn't exist. Seeds a default admin on first run."""
    conn = sqlite3.connect('mindmate.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

    c.execute("SELECT COUNT(*) FROM admins")
    if c.fetchone()[0] == 0:
        default_pw_hash = hashlib.sha256('ChangeMe123!'.encode()).hexdigest()
        c.execute(
            "INSERT INTO admins (name, email, password_hash) VALUES (?, ?, ?)",
            ('Super Admin', 'admin@mindmate.com', default_pw_hash)
        )
        conn.commit()
        print("[ADMIN] Default admin created -> admin@mindmate.com / ChangeMe123!  (change this immediately)")

    conn.close()

init_admin_tables()

# ============================================
# DATA STORAGE HELPERS
# ============================================

def get_user_file(base_name):
    email = session.get('user', {}).get('email', 'default')
    return f"{email}_{base_name}"

def load_history():
    try:
        with open(get_user_file(HISTORY_FILE), 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_history(history):
    try:
        with open(get_user_file(HISTORY_FILE), 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving history: {e}")

def load_stress_data():
    try:
        with open(get_user_file(STRESS_DATA_FILE), 'r') as f:
            return json.load(f)
    except:
        return []

def save_stress_data(data):
    try:
        with open(get_user_file(STRESS_DATA_FILE), 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving stress data: {e}")

def add_stress_log(emotion, stress_score, source='text'):
    logs = load_stress_data()
    logs.append({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'emotion': emotion,
        'stress_score': stress_score,
        'source': source
    })
    if len(logs) > 50:
        logs = logs[-50:]
    save_stress_data(logs)
    return logs

# ============================================
# ADMIN HELPERS (read any user's files by email, not session)
# ============================================

def admin_load_history(email):
    path = f"{email}_{HISTORY_FILE}"
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def admin_load_stress_data(email):
    path = f"{email}_{STRESS_DATA_FILE}"
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def admin_required(view_func):
    from functools import wraps
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if not session.get('admin'):
            return jsonify({'success': False, 'message': 'Admin authentication required'}), 401
        return view_func(*args, **kwargs)
    return wrapped

# ============================================
# OFFLINE BACKUP RESPONSES
# ============================================
RESPONSES = {
    'mr': {
        'greeting': "नमस्कार! मी तुमचा ममता सहाय्यक आहे. तुम्ही कसे आहात?",
        'how_are_you': "मी ठीक आहे, धन्यवाद! तुम्ही कसे आहात?",
        'good': "तुम्ही ठीक आहात हे ऐकून खूप आनंद झाला!",
        'sad': "तुम्ही दुःखी आहात हे ऐकून मला वाईट वाटले. मी तुमच्यासोबत आहे.",
        'stressed': "तुम्ही तणावात आहात. कृपया खोल श्वास घ्या. श्वास घ्या... आणि सोडा.",
        'angry': "राग येणे सामान्य आहे. तुमच्या भावना वैध आहेत.",
        'tired': "तुम्ही थकले आहात. कृपया विश्रांती घ्या.",
        'default': "मी तुमचे ऐकत आहे. कृपया सुरू ठेवा."
    },
    'hi': {
        'greeting': "नमस्ते! मैं आपका ममता सहायक हूँ। आप कैसे हैं?",
        'how_are_you': "मैं ठीक हूँ, धन्यवाद! आप कैसे हैं?",
        'good': "आप ठीक हैं सुनकर बहुत अच्छा लगा!",
        'sad': "आप दुखी हैं सुनकर मुझे दुख हुआ। मैं आपके साथ हूँ।",
        'stressed': "आप तनाव में हैं। कृपया गहरी सांस लें। सांस लें... और छोड़ें।",
        'angry': "गुस्सा आना सामान्य है। आपकी भावनाएँ वैध हैं।",
        'tired': "आप थके हुए हैं। कृपया आराम करें।",
        'default': "मैं आपकी बात सुन रहा हूँ। कृपया जारी रखें।"
    },
    'te': {
        'greeting': "నమస్కారం! నేను మీ మమత సహాయకుడిని. మీరు ఎలా ఉన్నారు?",
        'how_are_you': "నేను బాగానే ఉన్నాను, ధన్యవాదాలు! మీరు ఎలా ఉన్నారు?",
        'good': "మీరు బాగానే ఉన్నారని విని చాలా సంతోషంగా ఉంది!",
        'sad': "మీరు బాధగా ఉన్నారని విని నాకు బాధగా ఉంది. నేను మీతో ఉన్నాను.",
        'stressed': "మీరు ఒత్తిడికి గురవుతున్నారు. దయచేసి లోతుగా శ్వాస తీసుకోండి.",
        'angry': "కోపం రావడం సాధారణం. మీ భావాలు సరైనవే.",
        'tired': "మీరు అలిసిపోయినట్లున్నారు. దయచేసి విశ్రాంతి తీసుకోండి.",
        'default': "నేను మీ మాట వింటున్నాను. దయచేసి కొనసాగించండి."
    },
    'en': {
        'greeting': "Namaste! I'm your MAMATHA assistant. How are you?",
        'how_are_you': "I'm doing well, thank you! How are you?",
        'good': "I'm glad to hear you're doing well!",
        'sad': "I'm sorry to hear you're feeling sad. I'm here with you.",
        'stressed': "I understand you're feeling stressed. Take a deep breath. Breathe in... and out.",
        'angry': "Feeling angry is normal. Your feelings are valid.",
        'tired': "You sound tired. Please rest.",
        'default': "I'm listening. Please continue."
    },
    'bn': {
        'greeting': "নমস্কার! আমি আপনার মমতা সহকারী। আপনি কেমন আছেন?",
        'how_are_you': "আমি ভালো আছি, ধন্যবাদ! আপনি কেমন আছেন?",
        'good': "আপনি ভালো আছেন শুনে খুব আনন্দ হল!",
        'sad': "আপনার মন খারাপ শুনে আমারও খারাপ লাগছে। আমি আপনার সাথে আছি।",
        'stressed': "আপনি চাপে আছেন বুঝতে পারছি। অনুগ্রহ করে গভীর শ্বাস নিন।",
        'angry': "রাগ হওয়া স্বাভাবিক। আপনার অনুভূতিগুলি বৈধ।",
        'tired': "আপনাকে ক্লান্ত মনে হচ্ছে। অনুগ্রহ করে বিশ্রাম নিন।",
        'default': "আমি শুনছি। অনুগ্রহ করে বলতে থাকুন।"
    },
    'ta': {
        'greeting': "வணக்கம்! நான் உங்கள் மமதா உதவியாளர். நீங்கள் எப்படி இருக்கிறீர்கள்?",
        'how_are_you': "நான் நன்றாக இருக்கிறேன், நன்றி! நீங்கள் எப்படி இருக்கிறீர்கள்?",
        'good': "நீங்கள் நன்றாக இருக்கிறீர்கள் என்று கேட்பதில் மகிழ்ச்சி!",
        'sad': "நீங்கள் சோகமாக இருக்கிறீர்கள் என்று கேட்பதில் வருத்தமாக உள்ளது. நான் உங்களுடன் இருக்கிறேன்.",
        'stressed': "நீங்கள் மன அழுத்தத்தில் உள்ளீர்கள். தயவுசெய்து ஆழமாக மூச்சு விடுங்கள்.",
        'angry': "கோபம் வருவது இயல்பு. உங்கள் உணர்வுகள் சரியானவை.",
        'tired': "நீங்கள் சோர்வாக இருக்கிறீர்கள். தயவுசெய்து ஓய்வெடுங்கள்.",
        'default': "நான் கேட்டுக்கொண்டிருக்கிறேன். தயவுசெய்து தொடரவும்."
    },
    'ur': {
        'greeting': "آداب! میں آپ کا ممتا اسسٹنٹ ہوں۔ آپ کیسے ہیں؟",
        'how_are_you': "میں ٹھیک ہوں، شکریہ! آپ کیسے ہیں؟",
        'good': "یہ سن کر خوشی ہوئی کہ آپ ٹھیک ہیں!",
        'sad': "مجھے افسوس ہے کہ آپ اداس ہیں۔ میں آپ کے ساتھ ہوں۔",
        'stressed': "آپ تناؤ کا شکار ہیں۔ براہ کرم گہری سانس لیں۔",
        'angry': "غصہ آنا عام بات ہے۔ آپ کے احساسات جائز ہیں۔",
        'tired': "آپ تھکے ہوئے لگ رہے ہیں۔ براہ کرم آرام کریں۔",
        'default': "میں سن رہا ہوں۔ براہ کرم جاری رکھیں۔"
    },
    'gu': {
        'greeting': "નમસ્તે! હું તમારો મમતા સહાયક છું. તમે કેમ છો?",
        'how_are_you': "હું મજામાં છું, આભાર! તમે કેમ છો?",
        'good': "તમે મજામાં છો તે જાણીને આનંદ થયો!",
        'sad': "તમે ઉદાસ છો તે જાણીને દુઃખ થયું. હું તમારી સાથે છું.",
        'stressed': "તમે તણાવમાં છો. કૃપા કરીને ઊંડા શ્વાસ લો.",
        'angry': "ગુસ્સો આવવો સામાન્ય છે. તમારી લાગણીઓ માન્ય છે.",
        'tired': "તમે થાકેલા લાગો છો. કૃપા કરીને આરામ કરો.",
        'default': "હું સાંભળી રહ્યો છું. કૃપા કરીને ચાલુ રાખો."
    },
    'kn': {
        'greeting': "ನಮಸ್ಕಾರ! ನಾನು ನಿಮ್ಮ ಮಮತಾ ಸಹಾಯಕ. ನೀವು ಹೇಗಿದ್ದೀರಿ?",
        'how_are_you': "ನಾನು ಚೆನ್ನಾಗಿದ್ದೇನೆ, ಧನ್ಯವಾದಗಳು! ನೀವು ಹೇಗಿದ್ದೀರಿ?",
        'good': "ನೀವು ಚೆನ್ನಾಗಿದ್ದೀರಿ ಎಂದು ಕೇಳಿ ಸಂತೋಷವಾಯಿತು!",
        'sad': "ನೀವು ದುಃಖಿತರಾಗಿದ್ದೀರಿ ಎಂದು ಕೇಳಿ ಬೇಸರವಾಯಿತು. ನಾನು ನಿಮ್ಮೊಂದಿಗಿದ್ದೇನೆ.",
        'stressed': "ನೀವು ಒತ್ತಡದಲ್ಲಿದ್ದೀರಿ. ದಯವಿಟ್ಟು ಆಳವಾಗಿ ಉಸಿರಾಡಿ.",
        'angry': "ಕೋಪ ಬರುವುದು ಸಹಜ. ನಿಮ್ಮ ಭಾವನೆಗಳು ಮಾನ್ಯವಾಗಿವೆ.",
        'tired': "ನೀವು ದಣಿದಿದ್ದೀರಿ. ದಯವಿಟ್ಟು ವಿಶ್ರಾಂತಿ ಪಡೆಯಿರಿ.",
        'default': "ನಾನು ಕೇಳುತ್ತಿದ್ದೇನೆ. ದಯವಿಟ್ಟು ಮುಂದುವರಿಸಿ."
    },
    'ml': {
        'greeting': "നമസ്കാരം! ഞാൻ നിങ്ങളുടെ മമത സഹായിയാണ്. നിങ്ങൾക്ക് സുഖമാണോ?",
        'how_are_you': "എനിക്ക് സുഖമാണ്, നന്ദി! നിങ്ങൾക്ക് സുഖമാണോ?",
        'good': "നിങ്ങൾക്ക് സുഖമാണെന്ന് കേൾക്കുന്നതിൽ സന്തോഷമുണ്ട്!",
        'sad': "നിങ്ങൾ വിഷമത്തിലാണെന്ന് കേൾക്കുന്നതിൽ സങ്കടമുണ്ട്. ഞാൻ നിങ്ങളോടൊപ്പമുണ്ട്.",
        'stressed': "നിങ്ങൾ സമ്മർദ്ദത്തിലാണെന്ന് മനസ്സിലാക്കുന്നു. ദയവായി ദീർഘമായി ശ്വസിക്കുക.",
        'angry': "ദേഷ്യം വരുന്നത് സാധാരണമാണ്. നിങ്ങളുടെ വികാരങ്ങൾ ന്യായമാണ്.",
        'tired': "നിങ്ങൾ ക്ഷീണിതനാണെന്ന് തോന്നുന്നു. ദയവായി വിശ്രമിക്കുക.",
        'default': "ഞാൻ കേൾക്കുന്നുണ്ട്. ദയവായി തുടരുക."
    },
    'pa': {
        'greeting': "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ! ਮੈਂ ਤੁਹਾਡਾ ਮਮਤਾ ਸਹਾਇਕ ਹਾਂ। ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?",
        'how_are_you': "ਮੈਂ ਠੀਕ ਹਾਂ, ਧੰਨਵਾਦ! ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?",
        'good': "ਇਹ ਸੁਣ ਕੇ ਖੁਸ਼ੀ ਹੋਈ ਕਿ ਤੁਸੀਂ ਠੀਕ ਹੋ!",
        'sad': "ਇਹ ਸੁਣ ਕੇ ਦੁੱਖ ਹੋਇਆ ਕਿ ਤੁਸੀਂ ਉਦਾਸ ਹੋ। ਮੈਂ ਤੁਹਾਡੇ ਨਾਲ ਹਾਂ।",
        'stressed': "ਤੁਸੀਂ ਤਣਾਅ ਵਿੱਚ ਹੋ। ਕਿਰਪਾ ਕਰਕੇ ਲੰਬੇ ਸਾਹ ਲਓ।",
        'angry': "ਗੁੱਸਾ ਆਉਣਾ ਆਮ ਗੱਲ ਹੈ। ਤੁਹਾਡੀਆਂ ਭਾਵਨਾਵਾਂ ਜਾਇਜ਼ ਹਨ।",
        'tired': "ਤੁਸੀਂ ਥੱਕੇ ਹੋਏ ਲੱਗਦੇ ਹੋ। ਕਿਰਪਾ ਕਰਕੇ ਆਰਾਮ ਕਰੋ।",
        'default': "ਮੈਂ ਸੁਣ ਰਿਹਾ ਹਾਂ। ਕਿਰਪਾ ਕਰਕੇ ਜਾਰੀ ਰੱਖੋ।"
    },
    'or': {
        'greeting': "ନମସ୍କାର! ମୁଁ ଆପଣଙ୍କର ମମତା ସହାୟକ। ଆପଣ କେମିତି ଅଛନ୍ତି?",
        'how_are_you': "ମୁଁ ଭଲ ଅଛି, ଧନ୍ୟବାଦ! ଆପଣ କେମିତି ଅଛନ୍ତି?",
        'good': "ଆପଣ ଭଲ ଅଛନ୍ତି ଶୁଣି ଖୁସି ଲାଗିଲା!",
        'sad': "ଆପଣ ଦୁଃଖିତ ଅଛନ୍ତି ଶୁଣି ଖରାପ ଲାଗିଲା। ମୁଁ ଆପଣଙ୍କ ସହ ଅଛି।",
        'stressed': "ଆପଣ ଚାପରେ ଅଛନ୍ତି। ଦୟାକରି ଗଭୀର ଶ୍ୱାସ ନିଅନ୍ତୁ।",
        'angry': "ରାଗିବା ସାଧାରଣ କଥା। ଆପଣଙ୍କ ଭାବନା ଠିକ୍।",
        'tired': "ଆପଣ ଥକି ଯାଇଛନ୍ତି। ଦୟାକରି ବିଶ୍ରାମ ନିଅନ୍ତୁ।",
        'default': "ମୁଁ ଶୁଣୁଛି। ଦୟାକରି ଜାରି ରଖନ୍ତୁ।"
    }
}
def detect_intent(text):
    text_lower = text.lower()
    greetings = ['hello', 'hi', 'hey', 'namaste', 'नमस्कार', 'नमस्ते', 'నమస్కారం']
    how_are_you = ['how are you', 'कसे आहात', 'ఎలా ఉన్నారు', 'how do you do']
    good_words = ['good', 'great', 'happy', 'fine', 'ठीक', 'బాగా', 'well']
    sad_words = ['sad', 'unhappy', 'depressed', 'दुःखी', 'బాధ', 'down']
    stress_words = ['stress', 'stressed', 'tension', 'तणाव', 'ఒత్తిడి', 'anxious', 'worry']
    angry_words = ['angry', 'mad', 'frustrated', 'राग', 'कोపం']
    tired_words = ['tired', 'exhausted', 'sleepy', 'थका', 'అలసట']
    
    if any(w in text_lower for w in greetings):
        return 'greeting'
    elif any(w in text_lower for w in how_are_you):
        return 'how_are_you'
    elif any(w in text_lower for w in good_words):
        return 'good'
    elif any(w in text_lower for w in sad_words):
        return 'sad'
    elif any(w in text_lower for w in stress_words):
        return 'stressed'
    elif any(w in text_lower for w in angry_words):
        return 'angry'
    elif any(w in text_lower for w in tired_words):
        return 'tired'
    else:
        return 'default'
def analyze_text_stress_offline(text):
    text_lower = text.lower()
    high_stress = ['sad', 'unhappy', 'depressed', 'दुःखी', 'బాధ', 'stress', 'stressed', 'tension', 'तणाव', 'ఒత్తిడి', 'anxious', 'worry', 'suicide', 'kill', 'die', 'pain']
    low_stress = ['good', 'great', 'happy', 'fine', 'ठीक', 'బాగా', 'well', 'calm', 'relaxed']
    
    if any(w in text_lower for w in high_stress):
        return 75
    elif any(w in text_lower for w in low_stress):
        return 25
    return 40
def get_offline_fallback(text, language, chat_history=None):
    try:
        import g4f
        from g4f.client import Client
        client = Client()
        
        lang_names = {
            'en': 'English', 'hi': 'Hindi', 'bn': 'Bengali', 'te': 'Telugu',
            'mr': 'Marathi', 'ta': 'Tamil', 'ur': 'Urdu', 'gu': 'Gujarati',
            'kn': 'Kannada', 'ml': 'Malayalam', 'pa': 'Punjabi', 'or': 'Odia'
        }
        target_lang = lang_names.get(language, 'English')
        
        system_prompt = (
            "You are MAMATHA, a warm, highly empathetic, and supportive AI mental health companion.\n"
            f"Provide your response to the user's message in {target_lang}.\n"
            "Keep your response warm, supportive, and concise (2-4 sentences)."
        )
        
        messages = [{"role": "system", "content": system_prompt}]
        if chat_history:
            for turn in chat_history[-5:]:
                messages.append({"role": "user", "content": turn.get('user_message', '')})
                messages.append({"role": "assistant", "content": turn.get('ai_response', '')})
        messages.append({"role": "user", "content": text})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response_text = response.choices[0].message.content.strip()
        stress_score = analyze_text_stress_offline(text)
        return response_text, stress_score
    except Exception as e:
        print("g4f fallback failed:", e)
        intent = detect_intent(text)
        stress_score = analyze_text_stress_offline(text)
        lang_responses = RESPONSES.get(language, RESPONSES['en'])
        response_text = lang_responses.get(intent, lang_responses['default'])
        return response_text, stress_score
# ============================================
# SARVAM AI LLM CONNECTOR
# ============================================
def query_sarvam_llm(user_message, language, chat_history=None):
    """
    Queries Sarvam AI's Chat Completion API with the user message and target language.
    Returns: (response_text, stress_score)
    """
    api_key = os.getenv("SARVAM_API_KEY")
    if not api_key:
        print("[WARNING] SARVAM_API_KEY not found in environment. Using offline fallback.")
        return get_offline_fallback(user_message, language, chat_history)
    url = "https://api.sarvam.ai/v1/chat/completions"
    headers = {
        "api-subscription-key": api_key,
        "Content-Type": "application/json"
    }
    # Map language codes to friendly names for the system prompt
    lang_names = {
        'en': 'English',
        'hi': 'Hindi',
        'bn': 'Bengali',
        'te': 'Telugu',
        'mr': 'Marathi',
        'ta': 'Tamil',
        'ur': 'Urdu',
        'gu': 'Gujarati',
        'kn': 'Kannada',
        'ml': 'Malayalam',
        'pa': 'Punjabi',
        'or': 'Odia'
    }
    target_lang = lang_names.get(language, 'English')
    # Construct system prompt to return output in JSON format containing the text response and stress score
    system_prompt = (
        "You are MAMATHA, a warm, highly empathetic, and supportive AI mental health companion.\n"
        f"Provide your response to the user's message in {target_lang}.\n"
        "If the user says a simple greeting (like 'hello', 'hi'), introduce yourself as MAMATHA. Otherwise, respond naturally and directly to their concern like a helpful assistant.\n"
        "Keep your response warm, supportive, and concise (2-4 sentences).\n"
        "Estimate the user's current stress level as a score between 0 and 100 based on their message.\n"
        "Format your output ONLY as a valid JSON object with the following structure:\n"
        "{\n"
        '  "response": "<supportive response in ' + target_lang + '>",\n'
        '  "stress_score": <estimated stress level of user\'s message from 0 to 100>\n'
        "}\n"
        "Do not include any Markdown backticks, HTML tags, or trailing text before or after the JSON.\n"
        "Example Output:\n"
        '{"response": "I hear you, how can I help?", "stress_score": 40}'
    )
    
    messages = [{"role": "system", "content": system_prompt}]
    if chat_history:
        for turn in chat_history[-5:]:
            messages.append({"role": "user", "content": turn.get('user_message', '')})
            messages.append({"role": "assistant", "content": turn.get('ai_response', '')})
    messages.append({"role": "user", "content": user_message})
    
    payload = {
        "model": "sarvam-105b-conversations",
        "messages": messages,
        "temperature": 0.5
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            content = data['choices'][0]['message']['content'].strip()
            
            # Use regex to extract JSON block in case LLM added extra text
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                content = json_match.group(0)
                
            try:
                parsed = json.loads(content)
                response_text = parsed.get("response", "")
                stress_score = int(parsed.get("stress_score", 40))
                return response_text, stress_score
            except Exception as pe:
                print(f"JSON parsing failed for LLM response: {pe}. Raw Content: {content}")
                return content, analyze_text_stress_offline(user_message)
        else:
            print(f"Sarvam LLM API returned error {response.status_code}: {response.text}")
            return get_offline_fallback(user_message, language, chat_history)
    except Exception as e:
        print(f"Exception during Sarvam LLM query: {e}")
        return get_offline_fallback(user_message, language, chat_history)

def generate_tts_audio(text, language, gender):
    """
    Generate audio for given text, language, and gender.
    Uses Sarvam AI TTS if key is present, otherwise falls back to gTTS.
    """
    api_key = os.getenv("SARVAM_API_KEY")
    audio_url = None
    
    if api_key:
        # Map frontend language code to Sarvam BCP-47 codes
        lang_map = {
            'hi': 'hi-IN', 'te': 'te-IN', 'ta': 'ta-IN', 'kn': 'kn-IN',
            'en': 'en-IN', 'bn': 'bn-IN', 'mr': 'mr-IN', 'gu': 'gu-IN',
            'ml': 'ml-IN', 'or': 'or-IN', 'pa': 'pa-IN', 'ur': 'ur-PK'
        }
        language_code = lang_map.get(language, 'en-IN')
        
        # Sarvam supports multiple speakers:
        # Female for bulbul:v3: priya, kavya, etc.
        # Male for bulbul:v3: rahul, amit, etc.
        speaker = 'rahul' if gender == 'male' else 'priya'
        
        url = "https://api.sarvam.ai/text-to-speech"
        payload = {
            "inputs": [text],
            "target_language_code": language_code,
            "speaker": speaker,
            "pace": 1.0,
            "speech_sample_rate": 8000,
            "enable_preprocessing": True,
            "model": "bulbul:v3"
        }
        headers = {
            "api-subscription-key": api_key,
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                resp_json = response.json()
                if 'audios' in resp_json and len(resp_json['audios']) > 0:
                    audio_b64 = resp_json['audios'][0]
                    audio_bytes = base64.b64decode(audio_b64)
                    audio_filename = f"response_{uuid.uuid4().hex}.wav"
                    audio_path = os.path.join('static', audio_filename)
                    with open(audio_path, 'wb') as f:
                        f.write(audio_bytes)
                    audio_url = f'/static/{audio_filename}'
                    return audio_url
            else:
                print(f"Sarvam TTS failed with {response.status_code}: {response.text}")
        except Exception as e:
            print(f"Exception during Sarvam TTS generation: {e}")
            
    try:
        from gtts import gTTS
        lang_map = {
            'mr': 'mr', 'hi': 'hi', 'te': 'te', 'ta': 'ta',
            'kn': 'kn', 'ml': 'ml', 'bn': 'bn', 'gu': 'gu',
            'en': 'en', 'pa': 'pa', 'ur': 'ur', 'or': 'or'
        }
        tts_lang = lang_map.get(language, 'en')
        tts = gTTS(text=text, lang=tts_lang, slow=False)
        audio_filename = f"response_{uuid.uuid4().hex}.mp3"
        audio_path = os.path.join('static', audio_filename)
        tts.save(audio_path)
        audio_url = f'/static/{audio_filename}'
    except Exception as e:
        print(f"gTTS Generation Error: {e}")
        
    return audio_url

# ============================================
# API ENDPOINTS
# ============================================
@app.route('/predict', methods=['POST'])
def predict():
    """Handle text chat messages and return LLM response with stress score"""
    message = request.form.get('message', '')
    language = request.form.get('language', 'en')
    
    if not message:
        return jsonify({'success': False, 'error': 'No message provided'}), 400
        
    history = load_history()
    # Call LLM
    response_text, stress_score = query_sarvam_llm(message, language, chat_history=history)
    
    # Save to history
    risk = "red" if stress_score > 70 else "orange" if stress_score > 40 else "green"
    history.append({
        'timestamp': datetime.now().isoformat(),
        'user_message': message,
        'ai_response': response_text,
        'stress_score': stress_score,
        'risk': risk
    })
    save_history(history)
    # Save to stress dashboard log
    emotion = "distressed" if stress_score > 70 else "stressed" if stress_score > 40 else "calm"
    add_stress_log(emotion, stress_score, source='text')
    # Generate voice response
    audio_url = generate_tts_audio(response_text, language, "female") # Default to female for text chat
    
    video_url = None
    if audio_url:
        import os
        audio_path = os.path.join(os.getcwd(), audio_url.lstrip('/'))
        if os.path.exists(audio_path):
            print("Generating D-ID Video for Text Chat...")
            video_url = generate_did_video_sync(audio_path, "female")
            if video_url:
                print("D-ID Video Generated:", video_url)
                
    return jsonify({
        'success': True,
        'user_text': message,
        'ai_response': response_text,
        'stress_score': stress_score,
        'audio_url': audio_url,
        'video_url': video_url,
        'suggestion': response_text,
        'risk': risk
    })

DID_IMAGE_CACHE = {}

def generate_did_video_sync(audio_path, gender):
    import requests
    import time
    import os
    
    # Use the provided D-ID API Key
    did_auth = ('cmVraGFidWpqaTUxMUBnbWFpbC5jb20', 'MFivKo1SAHWsgZNIVc3gr')
    
    # 1. Image Upload
    # Determine the local image path based on gender
    image_filename = 'doctor_male.png' if gender == 'male' else 'doctor_female.png'
    local_image_path = os.path.join('static', image_filename)
    
    if not os.path.exists(local_image_path):
        print(f"Error: Local image not found at {local_image_path}")
        return None
        
    image_s3_url = DID_IMAGE_CACHE.get(image_filename)
    if not image_s3_url:
        print(f"Uploading {image_filename} to D-ID...")
        try:
            with open(local_image_path, 'rb') as img_file:
                res_img = requests.post(
                    "https://api.d-id.com/images", 
                    auth=did_auth, 
                    files={"image": img_file}
                )
            if res_img.status_code == 201 or res_img.status_code == 200:
                image_s3_url = res_img.json().get('url')
                DID_IMAGE_CACHE[image_filename] = image_s3_url
                print("Image uploaded:", image_s3_url)
            else:
                print("Failed to upload image:", res_img.text)
                return None
        except Exception as e:
            print("Exception uploading image:", e)
            return None
            
    # 2. Audio Upload
    print(f"Uploading {audio_path} to D-ID...")
    try:
        with open(audio_path, 'rb') as audio_file:
            res_audio = requests.post(
                "https://api.d-id.com/audios", 
                auth=did_auth, 
                files={"audio": audio_file}
            )
        if res_audio.status_code == 201 or res_audio.status_code == 200:
            audio_url = res_audio.json().get('url')
            print("Audio uploaded:", audio_url)
        else:
            print("Failed to upload audio:", res_audio.text)
            return None
    except Exception as e:
        print("Exception uploading audio:", e)
        return None
        
    # 3. Create Talk
    payload = {
        "source_url": image_s3_url,
        "script": {
            "type": "audio",
            "audio_url": audio_url
        }
    }
    print("Creating D-ID talk...")
    try:
        res_talk = requests.post(
            "https://api.d-id.com/talks", 
            auth=did_auth, 
            json=payload
        )
        if res_talk.status_code == 201:
            talk_id = res_talk.json().get("id")
            print("Talk created. Polling for completion... ID:", talk_id)
            
            # Poll for completion
            for _ in range(60): # Max 120 seconds
                res_status = requests.get(
                    f"https://api.d-id.com/talks/{talk_id}", 
                    auth=did_auth
                )
                if res_status.status_code == 200:
                    status_data = res_status.json()
                    status = status_data.get("status")
                    if status == "done":
                        return status_data.get("result_url")
                    elif status == "error":
                        print("D-ID Video Failed:", status_data)
                        return None
                time.sleep(2)
            print("D-ID Video generation timed out.")
            return None
        else:
            print("Failed to create talk:", res_talk.text)
            return None
    except Exception as e:
        print("Exception creating talk:", e)
        return None


@app.route('/process_voice', methods=['POST'])
def process_voice():
    data = request.json
    user_text = data.get('text', '')
    language = data.get('language', 'en')
    gender = data.get('gender', 'female')
    
    if not user_text:
        return jsonify({'error': 'No text provided'}), 400
    
    history = load_history()
    # Get LLM response
    ai_response, stress_score = query_sarvam_llm(user_text, language, chat_history=history)
    
    # Generate voice response
    audio_url = generate_tts_audio(ai_response, language, gender)
    
    video_url = None
    if audio_url:
        import os
        audio_path = os.path.join(os.getcwd(), audio_url.lstrip('/'))
        if os.path.exists(audio_path):
            print("Generating D-ID Video...")
            video_url = generate_did_video_sync(audio_path, gender)
            if video_url:
                print("D-ID Video Generated:", video_url)
    
    # Add to stress logs
    emotion = "distressed" if stress_score > 70 else "stressed" if stress_score > 40 else "calm"
    add_stress_log(emotion, stress_score, source='voice')
    
    risk = "red" if stress_score > 70 else "orange" if stress_score > 40 else "green"
    history.append({
        'timestamp': datetime.now().isoformat(),
        'user_message': user_text,
        'ai_response': ai_response,
        'stress_score': stress_score,
        'risk': risk
    })
    save_history(history)
    
    return jsonify({
        'success': True,
        'user_text': user_text,
        'ai_response': ai_response,
        'stress_score': stress_score,
        'audio_url': audio_url,
        'video_url': video_url
    })
@app.route('/speak', methods=['POST'])
def speak():
    try:
        from gtts import gTTS
    except ImportError:
        return jsonify({'error': 'gTTS not installed'}), 500
    
    data = request.json
    text = data.get('text', '')
    language = data.get('language', 'en')
    
    if not text:
        return jsonify({'error': 'No text'}), 400
    
    lang_map = {'mr': 'mr', 'hi': 'hi', 'te': 'te', 'en': 'en', 'bn': 'bn', 'ta': 'ta', 'gu': 'gu', 'kn': 'kn', 'ml': 'ml'}
    tts_lang = lang_map.get(language, 'en')
    
    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang=tts_lang, slow=False)
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        
        return send_file(
            audio_data,
            mimetype='audio/mpeg',
            as_attachment=False,
            download_name='speech.mp3'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/analyze_voice_stress', methods=['POST'])
def analyze_voice_stress():
    """Endpoint to upload a WebM audio blob, transcribe it via Sarvam STT, and run LLM stress analysis"""
    if 'audio' not in request.files:
        return jsonify({'success': False, 'error': 'No audio file provided'}), 400
    
    audio_file = request.files['audio']
    language = request.args.get('language', 'en')
    
    temp_path = None
    try:
        # Save audio file temporarily
        temp_filename = f"temp_{uuid.uuid4().hex}.webm"
        temp_path = os.path.join('temp', temp_filename)
        audio_file.save(temp_path)
        
        transcript = ""
        api_key = os.getenv("SARVAM_API_KEY")
        # Map language code to Sarvam STT BCP-47 codes
        lang_map = {
            'en': 'en-IN', 'hi': 'hi-IN', 'te': 'te-IN', 'ta': 'ta-IN',
            'kn': 'kn-IN', 'ml': 'ml-IN', 'bn': 'bn-IN', 'gu': 'gu-IN',
            'mr': 'mr-IN', 'pa': 'pa-IN', 'ur': 'ur-IN', 'or': 'or-IN'
        }
        stt_lang = lang_map.get(language, 'unknown')
        # Use Sarvam STT REST API
        if api_key:
            try:
                url = "https://api.sarvam.ai/speech-to-text"
                headers = {
                    "api-subscription-key": api_key
                }
                
                # Read file as binary
                with open(temp_path, 'rb') as f:
                    files = {
                        'file': (temp_filename, f, 'audio/webm')
                    }
                    data = {
                        'language_code': stt_lang
                    }
                    response = requests.post(url, headers=headers, files=files, data=data, timeout=15)
                
                if response.status_code == 200:
                    result = response.json()
                    transcript = result.get('transcript', '')
                    print(f"STT Transcript: {transcript}")
                else:
                    print(f"Sarvam STT failed: {response.status_code} - {response.text}")
                    transcript = "I am feeling stressed and overwhelmed"
            except Exception as stt_err:
                print(f"Error calling Sarvam STT: {stt_err}")
                transcript = "I am feeling stressed and overwhelmed"
        else:
            # Fallback
            transcript = "I am feeling stressed and overwhelmed"
        # Query LLM with the transcribed text
        ai_response, stress_score = query_sarvam_llm(transcript, language)
        emotion = "distressed" if stress_score > 70 else "stressed" if stress_score > 40 else "calm"
        
        # Save to logs
        add_stress_log(emotion, stress_score, source='voice')
        
        return jsonify({
            'success': True,
            'transcript': transcript,
            'stress_score': stress_score,
            'emotion': emotion,
            'ai_response': ai_response,
            'suggestion': ai_response
        })
    except Exception as e:
        print(f"Voice stress analysis error: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass
# ============================================
# MOCK / ADDITIONAL DASHBOARD ROUTING
# ============================================
@app.route('/analyze_face', methods=['POST'])
def analyze_face():
    """Facial analysis endpoint supporting the post-login webcam dashboard feature."""
    try:
        data = request.json
        image_b64 = data.get('image')
        if not image_b64:
            return jsonify({'success': False, 'error': 'No image provided'}), 400
 
        if 'user' not in session:
            return jsonify({'success': False, 'error': 'Not logged in'}), 401
 
        current_user_email = session['user'].get('email')
 
        image_data = image_b64.split(",")[1]
        image_bytes = base64.b64decode(image_data)
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
 
        from face_service import get_all_faces
        from face_match import find_user
 
        faces = get_all_faces(image)
        if not faces or len(faces) == 0:
            return jsonify({'success': False, 'error': 'No face detected'}), 400
 
        recognized_face = None
        for face in faces:
            user = find_user(face.embedding)
            if user and user[2] == current_user_email:
                recognized_face = face
                break
 
        if not recognized_face:
            return jsonify({'success': False, 'error': 'Face not recognized as registered user'}), 403
 
        stress_score, dominant_emotion = compute_real_stress_from_image(image)
        if stress_score is None:
            return jsonify({'success': False, 'error': 'Could not analyze emotion'}), 400
 
        risk = "High" if stress_score > 70 else "Moderate" if stress_score > 40 else "Low"
        return jsonify({
            'success': True,
            'stress_score': stress_score,
            'emotion': dominant_emotion,
            'combined_stress_score': stress_score,
            'face_emotion': dominant_emotion,
            'combined_risk': risk
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
@app.route('/analyze_audio', methods=['POST'])
def analyze_audio():
    """Mock audio analysis endpoint"""
    try:
        stress_score = random.randint(20, 80)
        emotion = "neutral"
        return jsonify({
            'success': True,
            'transcript': "Hello",
            'speech_emotion': emotion,
            'speech_score': stress_score,
            'text_risk': 'green'
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
# ============================================
    
@app.route('/analyze_face_preview', methods=['POST'])
def analyze_face_preview():
    try:
        data = request.json
        image_b64 = data.get('image')
        if not image_b64:
            return jsonify({'success': False, 'error': 'No image provided'}), 400

        image_data = image_b64.split(",")[1]
        image_bytes = base64.b64decode(image_data)
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        stress_score, dominant_emotion = compute_real_stress_from_image(image)
        if stress_score is None:
            return jsonify({'success': False, 'error': 'No face detected'}), 400

        return jsonify({
            'success': True,
            'stress_score': stress_score,
            'emotion': dominant_emotion
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500   
# ============================================
# GUIDED DOCTOR SURVEY / INTAKE ENDPOINTS
@app.route('/get_greeting', methods=['GET'])
def get_greeting():
    language = request.args.get('language', 'en')
    lang_responses = RESPONSES.get(language, RESPONSES['en'])
    greeting_text = lang_responses.get('greeting', RESPONSES['en']['greeting'])
    audio_url = generate_tts_audio(greeting_text, language, "female")
    return jsonify({
        'success': True,
        'greeting': greeting_text,
        'audio_url': audio_url
    })
# ============================================
INTAKE_QUESTIONS = [
    {'id': 1, 'text': "How would you rate your overall mood today on a scale of 1-10?"},
    {'id': 2, 'text': "Have you been experiencing any trouble sleeping lately?"},
    {'id': 3, 'text': "How has your appetite been over the past few days?"},
    {'id': 4, 'text': "Have you felt more anxious or worried than usual?"},
    {'id': 5, 'text': "Is there anything specific that's been bothering you?"}
]
intake_sessions = {}
@app.route('/start_intake', methods=['POST'])
def start_intake():
    session_id = str(uuid.uuid4())
    intake_sessions[session_id] = {
        'current_question_index': 0,
        'answers': {},
        'started_at': time.time()
    }
    return jsonify({
        'first_question': INTAKE_QUESTIONS[0],
        'session_id': session_id
    })
@app.route('/next_question', methods=['GET'])
def next_question():
    session_id = request.args.get('session_id', 'default')
    if session_id not in intake_sessions:
        return jsonify({'done': True})
    
    session = intake_sessions[session_id]
    next_index = session['current_question_index']
    
    if next_index >= len(INTAKE_QUESTIONS):
        return jsonify({'done': True})
    
    return jsonify({
        'question': INTAKE_QUESTIONS[next_index],
        'done': False
    })
@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.json
    question_id = data.get('question_id')
    answer = data.get('answer', '')
    session_id = data.get('session_id', 'default')
    
    if session_id not in intake_sessions:
        session_id = 'default'
        if 'default' not in intake_sessions:
            intake_sessions['default'] = {
                'current_question_index': 0,
                'answers': {},
                'started_at': time.time()
            }
            
    session = intake_sessions[session_id]
    session['answers'][question_id] = answer
    session['current_question_index'] += 1
    
    # Generate supportive response via LLM
    question_idx = int(question_id) - 1
    question_text = INTAKE_QUESTIONS[question_idx]['text'] if 0 <= question_idx < len(INTAKE_QUESTIONS) else "Question"
    
    prompt = f"The user is undergoing a mental health intake survey. The question was: '{question_text}'. The user answered: '{answer}'. Provide a short, highly supportive and empathetic feedback sentence."
    reply, _ = query_sarvam_llm(prompt, 'en')
    # Urgency check
    urgent = False
    urgent_message = None
    urgent_keywords = ['suicide', 'kill', 'die', 'harm', 'hopeless', 'worthless']
    if any(w in answer.lower() for w in urgent_keywords):
        urgent = True
        urgent_message = "I am deeply concerned about what you shared. Please contact a mental health professional or call a crisis hotline immediately. You are not alone."
    next_question_index = session['current_question_index']
    next_q = INTAKE_QUESTIONS[next_question_index] if next_question_index < len(INTAKE_QUESTIONS) else None
    return jsonify({
        'reply': reply,
        'urgent': urgent,
        'urgent_message': urgent_message,
        'next_question': next_q,
        'done': next_q is None
    })
# ============================================
# DATABASE ACCESS ENDPOINTS
# ============================================

@app.route('/get_history', methods=['GET'])
def get_history():
    history = load_history()
    return jsonify({
        'success': True,
        'history': history[-20:]
    })
@app.route('/get_stress_data', methods=['GET'])
def get_stress_data():
    logs = load_stress_data()
    if logs:
        total_stress = sum(log.get('stress_score', 0) for log in logs)
        avg_stress = round(total_stress / len(logs))
    else:
        avg_stress = 0
    return jsonify({
        'success': True,
        'average_stress': avg_stress,
        'logs': logs[-10:] if logs else [],
        'total_logs': len(logs)
    })
# ============================================
# ACTUAL AUTHENTICATION & FACE RECOGNITION
# ============================================
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json(silent=True)
        if not data:
            email = request.form.get('email')
            password = request.form.get('password')
        else:
            email = data.get('email')
            password = data.get('password')
            
        conn = sqlite3.connect('mindmate.db')
        c = conn.cursor()
        c.execute("SELECT id, name, email, password_hash, age, location FROM users WHERE email=?", (email,))
        user = c.fetchone()
        conn.close()
        
        if user and user[3] == hashlib.sha256(password.encode()).hexdigest():
            session['user'] = {'email': user[2], 'name': user[1]}
            return jsonify({
                'success': True,
                'message': 'Login successful',
                'user': {
                    'name': user[1],
                    'email': user[2],
                    'age': user[4],
                    'location': user[5]
                }
            })
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': f'Server Error: {str(e)}'}), 500

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json(silent=True)
        if not data:
            data = request.form
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        age = data.get('age')
        location = data.get('location')
        alternate_phone = data.get('alternate_phone') or data.get('alternatePhone')
        embedding_str = data.get('embedding', '')
        image_b64 = data.get('image', '')

        print(f"[REGISTER] name={name}, email={email}, has_embedding={bool(embedding_str and embedding_str != '')}, has_image={bool(image_b64 and len(image_b64) > 100)}")

        # Extract face embedding from image if embedding_str is empty
        if (not embedding_str or embedding_str == '') and image_b64 and len(image_b64) > 100:
            try:
                print("[REGISTER] Extracting embedding from image...")
                image_data = image_b64.split(",")[1]
                image_bytes = base64.b64decode(image_data)
                image_array = np.frombuffer(image_bytes, dtype=np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
                if image is None:
                    print("[REGISTER] ERROR: cv2.imdecode returned None")
                    return jsonify({'success': False, 'message': 'Failed to decode image. Please try capturing your face again.'}), 400
                
                from face_service import get_all_faces
                faces = get_all_faces(image)
                print(f"[REGISTER] Faces detected: {len(faces) if faces else 0}")
                if not faces or len(faces) == 0:
                    return jsonify({'success': False, 'message': 'No face detected in registration image. Please position your face clearly in the camera frame.'}), 400
                if len(faces) > 1:
                    return jsonify({'success': False, 'message': 'Multiple faces detected. Please ensure only you are in frame.'}), 400
                
                embedding_str = json.dumps(faces[0].embedding.tolist())
                print(f"[REGISTER] Embedding extracted, length={len(embedding_str)}")
            except Exception as fe:
                print(f"[REGISTER] Error extracting embedding: {fe}")
                import traceback
                traceback.print_exc()
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        try:
            conn = sqlite3.connect('mindmate.db')
            c = conn.cursor()

            # Check if user already exists by email
            c.execute("SELECT id FROM users WHERE email=?", (email,))
            existing = c.fetchone()
            if existing:
                # Update existing user's embedding and details
                if embedding_str and len(embedding_str) > 10:
                    print(f"[REGISTER] Updating existing user id={existing[0]} with new embedding")
                    c.execute("UPDATE users SET name=?, password_hash=?, age=?, location=?, alternate_phone=?, embedding=? WHERE id=?",
                              (name, password_hash, age, location, alternate_phone, embedding_str, existing[0]))
                    conn.commit()
                    conn.close()
                    return jsonify({'success': True, 'message': 'Registration updated successfully with new face data'})
                else:
                    conn.close()
                    return jsonify({'success': False, 'message': 'Email already exists. Please use a different email or capture your face to update.'}), 400

            print(f"[REGISTER] Inserting new user, embedding_len={len(embedding_str) if embedding_str else 0}")
            c.execute("INSERT INTO users (name, email, password_hash, age, location, alternate_phone, embedding) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                      (name, email, password_hash, age, location, alternate_phone, embedding_str))
            conn.commit()
            print(f"[REGISTER] New user inserted with id={c.lastrowid}")
            conn.close()
            return jsonify({'success': True, 'message': 'Registration successful'})
        except sqlite3.IntegrityError:
            return jsonify({'success': False, 'message': 'Email already exists'}), 400
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': f'Server Error: {str(e)}'}), 500

@app.route('/register_face_test', methods=['POST'])
def register_face_test():
    data = request.json or {}
    image_b64 = data.get('image')
    email = data.get('email')
    name = data.get('name')
    
    if not image_b64:
        return jsonify({'success': False, 'message': 'No image provided'}), 400

    try:
        image_data = image_b64.split(",")[1]
        image_bytes = base64.b64decode(image_data)
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        from face_service import get_all_faces
        faces = get_all_faces(image)
        if not faces or len(faces) == 0:
            return jsonify({'success': False, 'message': 'No face detected'})
        if len(faces) > 1:
            return jsonify({'success': False, 'message': 'Multiple faces detected. Please ensure only you are in the frame.'})
            
        embedding = faces[0].embedding
        embedding_json = json.dumps(embedding.tolist())

        # If email or name is provided, update embedding in database immediately
        if email or name:
            try:
                conn = sqlite3.connect('mindmate.db')
                c = conn.cursor()
                if email:
                    c.execute("UPDATE users SET embedding = ? WHERE email = ?", (embedding_json, email))
                elif name:
                    c.execute("UPDATE users SET embedding = ? WHERE name = ?", (embedding_json, name))
                conn.commit()
                conn.close()
            except Exception as dberr:
                print(f"Error updating embedding in DB during face test: {dberr}")

        return jsonify({'success': True, 'embedding': embedding_json, 'message': 'Face embedding generated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/face_login', methods=['POST'])
def face_login():
    data = request.json
    image_b64 = data.get('image')
    try:
        image_data = image_b64.split(",")[1]
        image_bytes = base64.b64decode(image_data)
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        from face_service import get_all_faces
        faces = get_all_faces(image)
        
        if not faces or len(faces) == 0:
            return jsonify({'success': False, 'message': 'No face detected'})
            
        recognized_user = None
        for face in faces:
            user = find_user(face.embedding)
            if user:
                recognized_user = user
                break
                
        if recognized_user:
            user = recognized_user
            session['user'] = {'email': user[2], 'name': user[1]}
            # Fetch extra details to return
            conn = sqlite3.connect('mindmate.db')
            c = conn.cursor()
            c.execute("SELECT age, location FROM users WHERE email=?", (user[2],))
            extra = c.fetchone()
            conn.close()
            
            age = extra[0] if extra else 25
            location = extra[1] if extra else 'Unknown'
            
            return jsonify({
                'success': True, 
                'name': user[1], 
                'email': user[2],
                'user': {
                    'name': user[1],
                    'email': user[2],
                    'age': age,
                    'location': location
                }
            })
        else:
            return jsonify({'success': False, 'message': 'Face not recognized'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/face_login_with_stress', methods=['POST'])
def face_login_with_stress():
    """
    Combined endpoint used on the login page (before session exists).
    1. Recognises the registered user from their face embedding.
    2. Computes a real stress score from the same frame.
    Returns both the user identity and the stress result in a single response.
    Stress detection never blocks authentication.
    """
    data = request.json
    image_b64 = data.get('image')
    try:
        image_data  = image_b64.split(",")[1]
        image_bytes = base64.b64decode(image_data)
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)
        image       = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        from face_service import get_all_faces
        faces = get_all_faces(image)

        if not faces or len(faces) == 0:
            return jsonify({'success': False, 'message': 'No face detected', 'stress_score': None})

        # Step 1 – identify registered user
        recognized_user = None
        for face in faces:
            user = find_user(face.embedding)
            if user:
                recognized_user = user
                break

        # Step 2 – compute stress (always attempted, never blocks login)
        stress_score     = None
        dominant_emotion = None
        stress_risk      = None
        try:
            stress_score, dominant_emotion = compute_real_stress_from_image(image)
            if stress_score is not None:
                stress_risk = "High" if stress_score > 70 else "Moderate" if stress_score > 40 else "Low"
        except Exception:
            pass  # Stress failure must not block identification

        if recognized_user:
            user = recognized_user
            # Set session so the user is authenticated
            session['user'] = {'email': user[2], 'name': user[1]}

            conn = sqlite3.connect('mindmate.db')
            c    = conn.cursor()
            c.execute("SELECT age, location FROM users WHERE email=?", (user[2],))
            extra = c.fetchone()
            conn.close()
            age      = extra[0] if extra else 25
            location = extra[1] if extra else 'Unknown'

            return jsonify({
                'success':      True,
                'name':         user[1],
                'email':        user[2],
                'stress_score': stress_score,
                'emotion':      dominant_emotion,
                'stress_risk':  stress_risk,
                'user': {
                    'name':     user[1],
                    'email':    user[2],
                    'age':      age,
                    'location': location
                }
            })
        else:
            # Not recognised — still return stress if available
            return jsonify({
                'success':      False,
                'message':      'Face not recognized. Please use password login or register.',
                'stress_score': stress_score,
                'emotion':      dominant_emotion,
                'stress_risk':  stress_risk
            })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e), 'stress_score': None})

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    return redirect('/')

# ============================================
# FORGOT / RESET PASSWORD (email-based reset link)
# ============================================

password_reset_tokens = {}

def send_reset_email(to_email, reset_link):
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_APP_PASSWORD")

    if not smtp_email or not smtp_password:
        print("[RESET] SMTP_EMAIL / SMTP_APP_PASSWORD not set in .env — cannot send email.")
        return False

    subject = "Reset your MAMATHA password"
    body = f"""Hi,

We received a request to reset your MAMATHA password. Click the link below to set a new one:

{reset_link}

This link expires in 30 minutes. If you didn't request this, you can safely ignore this email.

— MAMATHA
"""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(smtp_email, smtp_password)
            server.sendmail(smtp_email, to_email, msg.as_string())
        return True
    except Exception as e:
        print(f"[RESET] Failed to send email: {e}")
        return False


@app.route('/forgot_password', methods=['POST'])
def forgot_password():
    data = request.get_json(silent=True) or request.form
    email = data.get('email')

    if not email:
        return jsonify({'success': False, 'message': 'Email is required'}), 400

    conn = sqlite3.connect('mindmate.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE email=?", (email,))
    user = c.fetchone()
    conn.close()

    if not user:
        return jsonify({'success': True, 'message': 'If that email is registered, a reset link has been sent.'})

    token = secrets.token_urlsafe(32)
    password_reset_tokens[token] = {
        'email': email,
        'expires': datetime.now().timestamp() + 1800
    }

    reset_link = f"{request.host_url.rstrip('/')}/reset_password/{token}"
    sent = send_reset_email(email, reset_link)

    if not sent:
        return jsonify({'success': False, 'message': 'Could not send reset email. Please try again later.'}), 500

    return jsonify({'success': True, 'message': 'If that email is registered, a reset link has been sent.'})


@app.route('/reset_password/<token>', methods=['GET'])
def reset_password_page(token):
    entry = password_reset_tokens.get(token)
    if not entry or entry['expires'] < datetime.now().timestamp():
        return "<h2>This reset link is invalid or has expired. Please request a new one.</h2>", 400

    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Reset Password - MAMATHA</title></head>
    <body style="font-family:sans-serif; max-width:400px; margin:60px auto;">
        <h2>Set a new password</h2>
        <form id="reset-form">
            <input type="password" id="new-password" placeholder="New password" required
                   style="width:100%; padding:10px; margin-bottom:10px;">
            <button type="submit" style="width:100%; padding:10px;">Reset Password</button>
        </form>
        <p id="msg"></p>
        <script>
            document.getElementById('reset-form').addEventListener('submit', async (e) => {{
                e.preventDefault();
                const password = document.getElementById('new-password').value;
                const res = await fetch('/reset_password/{token}', {{
                    method: 'POST',
                    headers: {{'Content-Type': 'application/json'}},
                    body: JSON.stringify({{password: password}})
                }});
                const data = await res.json();
                document.getElementById('msg').innerText = data.message;
                if (data.success) {{
                    setTimeout(() => window.location.href = '/', 1500);
                }}
            }});
        </script>
    </body>
    </html>
    """


@app.route('/reset_password/<token>', methods=['POST'])
def reset_password_submit(token):
    entry = password_reset_tokens.get(token)
    if not entry or entry['expires'] < datetime.now().timestamp():
        return jsonify({'success': False, 'message': 'This reset link is invalid or has expired.'}), 400

    data = request.get_json(silent=True) or {}
    new_password = data.get('password')
    if not new_password or len(new_password) < 6:
        return jsonify({'success': False, 'message': 'Password must be at least 6 characters.'}), 400

    password_hash = hashlib.sha256(new_password.encode()).hexdigest()

    conn = sqlite3.connect('mindmate.db')
    c = conn.cursor()
    c.execute("UPDATE users SET password_hash=? WHERE email=?", (password_hash, entry['email']))
    conn.commit()
    conn.close()

    del password_reset_tokens[token]

    return jsonify({'success': True, 'message': 'Password reset successfully! Redirecting to login...'})
# ============================================
# ADMIN AUTH, DASHBOARD, AND USER HISTORY ROUTES
# ============================================

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login_route():
    if request.method == 'GET':
        return send_from_directory('.', 'admin_login.html')

    email = request.form.get('email') or (request.get_json(silent=True) or {}).get('email')
    password = request.form.get('password') or (request.get_json(silent=True) or {}).get('password')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Email and password required'}), 400

    conn = sqlite3.connect('mindmate.db')
    c = conn.cursor()
    c.execute("SELECT id, name, email, password_hash FROM admins WHERE email=?", (email,))
    admin = c.fetchone()
    conn.close()

    if admin and admin[3] == hashlib.sha256(password.encode()).hexdigest():
        session['admin'] = {'id': admin[0], 'name': admin[1], 'email': admin[2]}
        return jsonify({'success': True, 'message': 'Login successful'})

    return jsonify({'success': False, 'message': 'Invalid admin credentials'}), 401


@app.route('/admin_dashboard', methods=['GET'])
def admin_dashboard_route():
    if not session.get('admin'):
        return redirect('/admin_login')
    return send_from_directory('.', 'admin_dashboard.html')


@app.route('/admin_logout', methods=['GET', 'POST'])
def admin_logout_route():
    session.pop('admin', None)
    return redirect('/admin_login')


@app.route('/api/admin/dashboard_data', methods=['GET'])
@admin_required
def api_admin_dashboard_data():
    conn = sqlite3.connect('mindmate.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users")
    total_users = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM admins")
    total_admins = c.fetchone()[0]
    c.execute("SELECT email FROM users")
    all_emails = [row[0] for row in c.fetchall()]
    conn.close()

    today_str = datetime.now().strftime('%Y-%m-%d')
    high_stress_count = 0
    sessions_today = 0

    for email in all_emails:
        logs = admin_load_stress_data(email)
        if logs and logs[-1].get('stress_score', 0) > 70:
            high_stress_count += 1

        history = admin_load_history(email)
        if history:
            last_ts = history[-1].get('timestamp', '')
            if last_ts.startswith(today_str):
                sessions_today += 1

    return jsonify({
        'success': True,
        'stats': {
            'total_users': total_users,
            'total_doctors': 0,
            'system_alerts': high_stress_count,
            'total_admins': total_admins,
            'sessions_today': sessions_today
        }
    })


@app.route('/api/admin/users', methods=['GET'])
@admin_required
def api_admin_users():
    conn = sqlite3.connect('mindmate.db')
    c = conn.cursor()
    c.execute("SELECT id, name, email, age, location FROM users ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    users = []
    for uid, name, email, age, location in rows:
        logs = admin_load_stress_data(email)
        history = admin_load_history(email)

        if logs:
            avg_stress = round(sum(l.get('stress_score', 0) for l in logs) / len(logs))
            last_score = logs[-1].get('stress_score', 0)
            last_ts = logs[-1].get('timestamp')
        else:
            avg_stress = 0
            last_score = 0
            last_ts = None

        level = 'High' if last_score > 70 else 'Moderate' if last_score > 40 else 'Low'

        users.append({
            'id': uid,
            'name': name,
            'email': email,
            'age': age,
            'location': location,
            'avg_stress': avg_stress,
            'last_stress_score': last_score,
            'stress_level': level,
            'last_session': last_ts or (history[-1]['timestamp'] if history else 'No sessions yet'),
            'total_messages': len(history)
        })

    return jsonify({'success': True, 'users': users})


@app.route('/api/admin/users/<int:user_id>/history', methods=['GET'])
@admin_required
def api_admin_user_history(user_id):
    conn = sqlite3.connect('mindmate.db')
    c = conn.cursor()
    c.execute("SELECT id, name, email, age, location FROM users WHERE id=?", (user_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        return jsonify({'success': False, 'message': 'User not found'}), 404

    uid, name, email, age, location = row
    history = admin_load_history(email)
    stress_logs = admin_load_stress_data(email)

    return jsonify({
        'success': True,
        'user': {'id': uid, 'name': name, 'email': email, 'age': age, 'location': location},
        'chat_history': history,
        'stress_logs': stress_logs
    })


@app.route('/api/admin/doctors', methods=['GET'])
@admin_required
def api_admin_doctors():
    return jsonify({'success': True, 'doctors': []})

@app.route('/api/admin/patients', methods=['GET'])
@admin_required
def api_admin_patients():
    return jsonify({'success': True, 'patients': []})

@app.route('/api/admin/alerts', methods=['GET'])
@admin_required
def api_admin_alerts():
    conn = sqlite3.connect('mindmate.db')
    c = conn.cursor()
    c.execute("SELECT name, email FROM users")
    rows = c.fetchall()
    conn.close()

    alerts = []
    for name, email in rows:
        logs = admin_load_stress_data(email)
        if logs and logs[-1].get('stress_score', 0) > 70:
            alerts.append({
                'type': 'High stress',
                'description': f'{name} ({email}) reported a high stress score',
                'status': 'Open',
                'created_at': logs[-1].get('timestamp', '')
            })
    return jsonify({'success': True, 'alerts': alerts})


# ============================================
# STATIC AND DOCK ROUTING
# ============================================
@app.route('/home')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    response = make_response(send_from_directory('.', 'login 2.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
# ============================================
# MAIN APPLICATION BOOT
# ============================================
if __name__ == '__main__':
    print("\n" + "="*60)
    print("[MAMATHA] CONSOLIDATED LLM MULTILINGUAL SYSTEM")
    print("="*60)
    print(f"[TTS] gTTS Available: {GTTS_AVAILABLE}")
    print(f"[AI]  Sarvam SDK: {'Available' if SARVAM_SDK_AVAILABLE else 'REST Mode (Fallback)'}")
    print("\n[SERVER] Launching at: http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)