// ======================== COMPLETE MULTI-LANGUAGE TRANSLATIONS (ALL 12 INDIAN LANGUAGES) ========================
const translations = {
  en: {
    appTitle: "MAMATHA: AI Based Companion Application",
    feeling: "How are you feeling today?",
    send: "Send", speak: "Speak", analyzeVoice: "Analyze My Voice Stress",
    startCam: "Start Camera", startSurvey: "Start Doctor Survey",
    pass: "Pass", reply: "Reply", mic: "Speak",
    placeholder: "Enter your thoughts..",
    intakePlaceholder: "Type your answer or click 'Pass'",
    stressTextPrefix: "Stress",
    userDetails: "User Details",
    avgStress: "Average Stress (Today):",
    recentStress: "Recent Stress Levels",
    historyTitle: "History",
    guidedIntake: "Guided Intake",
    analyzing: "Analyzing...",
    recording: "Recording...",
    name: "Name:", email: "Email:", age: "Age:", location: "Location:",
    intakeHelp: "We will ask a few gentle questions. Say 'pass' if you prefer not to answer.",
    stressDashboard: "Stress Dashboard"
  },
  hi: {
    appTitle: "MAMATHA: एआई आधारित साथी ऐप",
    feeling: "आज आप कैसा महसूस कर रहे हैं?",
    send: "भेजें", speak: "बोलें", analyzeVoice: "मेरी आवाज़ का तनाव विश्लेषण करें",
    startCam: "कैमरा शुरू करें", startSurvey: "डॉक्टर सर्वे शुरू करें",
    pass: "छोड़ें", reply: "जवाब दें", mic: "बोलें",
    placeholder: "अपने विचार लिखें..",
    intakePlaceholder: "अपना उत्तर टाइप करें या 'छोड़ें' दबाएं",
    stressTextPrefix: "तनाव",
    userDetails: "उपयोगकर्ता विवरण",
    avgStress: "औसत तनाव (आज):",
    recentStress: "हाल के तनाव स्तर",
    historyTitle: "इतिहास",
    guidedIntake: "मार्गदर्शित इंटेक",
    analyzing: "विश्लेषण हो रहा...",
    recording: "रिकॉर्डिंग...",
    name: "नाम:", email: "ईमेल:", age: "आयु:", location: "स्थान:",
    intakeHelp: "हम कुछ सौम्य प्रश्न पूछेंगे। यदि आप उत्तर नहीं देना चाहते तो 'छोड़ें' कहें।",
    stressDashboard: "तनाव डैशबोर्ड"
  },
  bn: {
    appTitle: "MAMATHA: এআই ভিত্তিক সহচর অ্যাপ",
    feeling: "আজ কেমন লাগছে?",
    send: "পাঠান", speak: "বলুন", analyzeVoice: "আমার ভয়েস স্ট্রেস বিশ্লেষণ করুন",
    startCam: "ক্যামেরা চালু করুন", startSurvey: "ডাক্তার জরিপ শুরু করুন",
    pass: "এড়িয়ে যান", reply: "উত্তর দিন", mic: "বলুন",
    placeholder: "আপনার চিন্তা লিখুন..",
    intakePlaceholder: "আপনার উত্তর টাইপ করুন বা 'এড়িয়ে যান' ক্লিক করুন",
    stressTextPrefix: "স্ট্রেস",
    userDetails: "ব্যবহারকারীর বিবরণ",
    avgStress: "গড় স্ট্রেস (আজ):",
    recentStress: "সাম্প্রতিক স্ট্রেস লেভেল",
    historyTitle: "ইতিহাস",
    guidedIntake: "নির্দেশিত ইনটেক",
    analyzing: "বিশ্লেষণ করা হচ্ছে...",
    recording: "রেকর্ডিং...",
    name: "নাম:", email: "ইমেইল:", age: "বয়স:", location: "অবস্থান:",
    intakeHelp: "আমরা কয়েকটি মৃদু প্রশ্ন জিজ্ঞাসা করব। উত্তর দিতে না চাইলে 'এড়িয়ে যান' বলুন।",
    stressDashboard: "স্ট্রেস ড্যাশবোর্ড"
  },
  te: {
    appTitle: "MAMATHA: AI ఆధారిత సహచర అప్లికేషన్",
    feeling: "ఈరోజు ఎలా ఉన్నారు?",
    send: "పంపండి", speak: "మాట్లాడండి", analyzeVoice: "నా వాయిస్ ఒత్తిడిని విశ్లేషించండి",
    startCam: "కెమెరా ప్రారంభించండి", startSurvey: "డాక్టర్ సర్వే ప్రారంభించండి",
    pass: "దాటవేయి", reply: "సమాధానం ఇవ్వండి", mic: "మాట్లాడండి",
    placeholder: "మీ ఆలోచనలను టైప్ చేయండి..",
    intakePlaceholder: "మీ సమాధానం టైప్ చేయండి లేదా 'పాస్' క్లిక్ చేయండి",
    stressTextPrefix: "ఒత్తిడి",
    userDetails: "వినియోగదారు వివరాలు",
    avgStress: "సగటు ఒత్తిడి (నేడు):",
    recentStress: "ఇటీవలి ఒత్తిడి స్థాయిలు",
    historyTitle: "చరిత్ర",
    guidedIntake: "మార్గదర్శక ఇంటెక్",
    analyzing: "విశ్లేషిస్తోంది...",
    recording: "రికార్డ్ చేస్తోంది...",
    name: "పేరు:", email: "ఇమెయిల్:", age: "వయస్సు:", location: "ప్రదేశం:",
    intakeHelp: "మేము కొన్ని సున్నితమైన ప్రశ్నలు అడుగుతాము. సమాధానం ఇవ్వకూడదనుకుంటే 'పాస్' చెప్పండి.",
    stressDashboard: "ఒత్తిడి డాష్బోర్డ్"
  },
  mr: {
    appTitle: "MAMATHA: एआय आधारित साथी अॅप",
    feeling: "आज तू कसा वाटतोयस?",
    send: "पाठवा", speak: "बोला", analyzeVoice: "माझ्या आवाजाचा ताण विश्लेषित करा",
    startCam: "कॅмера सुरू करा", startSurvey: "डॉक्टर सर्वे सुरू करा",
    pass: "वगळा", reply: "उत्तर द्या", mic: "बोला",
    placeholder: "तुमचे विचार टाइप करा..",
    intakePlaceholder: "तुमचे उत्तर टाइप करा किंवा 'पास' क्लिक करा",
    stressTextPrefix: "ताण",
    userDetails: "वापरकर्ता तपशील",
    avgStress: "सरासरी ताण (आज):",
    recentStress: "अलीकडील ताण पातळी",
    historyTitle: "इतिहास",
    guidedIntake: "मार्गदर्शित इंटेक",
    analyzing: "विश्लेषण करत आहे...",
    recording: "रेकॉर्डिंग...",
    name: "नाव:", email: "ईमेल:", age: "वय:", location: "स्थान:",
    intakeHelp: "आम्ही काही सौम्य प्रश्न विचारू. उत्तर द्यायचे नसेल तर 'पास' म्हणा.",
    stressDashboard: "ताण डॅशबोर्ड"
  },
  ta: {
    appTitle: "MAMATHA: AI அடிப்படையிலான துணை பயன்பாடு",
    feeling: "இன்று எப்படி உணர்கிறீர்கள்?",
    send: "அனுப்பு", speak: "பேசு", analyzeVoice: "என் குரல் மன அழுத்தத்தை பகுப்பாய்வு செய்யுங்கள்",
    startCam: "கேமராவைத் தொடங்குங்கள்", startSurvey: "டாக்டர் கணக்கெடுப்பைத் தொடங்குங்கள்",
    pass: "தவிர்க்கவும்", reply: "பதிலளி", mic: "பேசு",
    placeholder: "உங்கள் எண்ணங்களை உள்ளிடவும்..",
    intakePlaceholder: "உங்கள் பதிலைத் தட்டச்சு செய்யவும் அல்லது 'தவிர்க்கவும்' என்பதைக் கிளிக் செய்யவும்",
    stressTextPrefix: "மன அழுத்தம்",
    userDetails: "பயனர் விவரங்கள்",
    avgStress: "சராசரி மன அழுத்தம் (இன்று):",
    recentStress: "சமீபத்திய மன அழுத்த நிலைகள்",
    historyTitle: "வரலாறு",
    guidedIntake: "வழிகாட்டப்பட்ட உட்கொள்ளல்",
    analyzing: "பகுப்பாய்வு செய்கிறது...",
    recording: "பதிவு செய்கிறது...",
    name: "பெயர்:", email: "மின்னஞ்சல்:", age: "வயது:", location: "இடம்:",
    intakeHelp: "நாங்கள் சில மென்மையான கேள்விகளைக் கேட்போம். பதிலளிக்க விரும்பவில்லை என்றால் 'தவிர்க்கவும்' என்று சொல்லுங்கள்.",
    stressDashboard: "மன அழுத்த டாஷ்போர்டு"
  },
  gu: {
    appTitle: "MAMATHA: AI આધારિત સાથી એપ્લિકેશન",
    feeling: "આજે તમે કેવું અનુભવો છો?",
    send: "મોકલો", speak: "બોલો", analyzeVoice: "મારા અવાજનો તણાવ વિશ્લેષણ કરો",
    startCam: "કેમેરા શરૂ કરો", startSurvey: "ડૉક્ટર સર્વે શરૂ કરો",
    pass: "છોડી દો", reply: "જવાબ આપો", mic: "બોલો",
    placeholder: "તમારા વિચારો લખો..",
    intakePlaceholder: "તમારો જવાબ ટાઈપ કરો અથવા 'પાસ' ક્લિક કરો",
    stressTextPrefix: "તણાવ",
    userDetails: "વપરાશકર્તા વિગતો",
    avgStress: "સરેરાશ તણાવ (આજે):",
    recentStress: "તાજેતરના તણાવ સ્તરો",
    historyTitle: "ઇતિહાસ",
    guidedIntake: "માર્ગદર્શિત ઇન્ટેક",
    analyzing: "વિશ્લેષણ કરી રહ્યું છે...",
    recording: "રેકોર્ડિંગ...",
    name: "નામ:", email: "ઇમેઇલ:", age: "ઉંમર:", location: "સ્થાન:",
    intakeHelp: "અમે થોડા સૌમ્ય પ્રશ્નો પૂછીશું. જો તમે જવાબ ન આપવા માંગતા હો તો 'પાસ' કહો.",
    stressDashboard: "તણાવ ડેશબોર્ડ"
  },
  kn: {
    appTitle: "MAMATHA: AI ಆಧಾರಿತ ಸಹಚರ ಅಪ್ಲಿಕೇಶನ್",
    feeling: "ಇಂದು ನೀವು ಹೇಗೆ ಭಾವಿಸುತ್ತೀರಿ?",
    send: "ಕಳುಹಿಸಿ", speak: "ಮಾತನಾಡಿ", analyzeVoice: "ನನ್ನ ಧ್ವನಿ ಒತ್ತಡವನ್ನು ವಿಶ್ಲೇಷಿಸಿ",
    startCam: "ಕ್ಯಾಮೆರಾ ಪ್ರಾರಂಭಿಸಿ", startSurvey: "ಡಾಕ್ಟರ್ ಸಮೀಕ್ಷೆ ಪ್ರಾರಂಭಿಸಿ",
    pass: "ಬಿಟ್ಟುಬಿಡಿ", reply: "ಉತ್ತರಿಸಿ", mic: "ಮಾತನಾಡಿ",
    placeholder: "ನಿಮ್ಮ ಆಲೋಚನೆಗಳನ್ನು ಟೈಪ್ ಮಾಡಿ..",
    intakePlaceholder: "ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಟೈಪ್ ಮಾಡಿ ಅಥವಾ 'ಪಾಸ್' ಕ್ಲಿಕ್ ಮಾಡಿ",
    stressTextPrefix: "ಒತ್ತಡ",
    userDetails: "ಬಳಕೆದಾರರ ವಿವರಗಳು",
    avgStress: "ಸರಾಸರಿ ಒತ್ತಡ (ಇಂದು):",
    recentStress: "ಇತ್ತೀಚಿನ ಒತ್ತಡದ ಮಟ್ಟಗಳು",
    historyTitle: "ಇತಿಹಾಸ",
    guidedIntake: "ಮಾರ್ಗದರ್ಶಿತ ಇಂಟೇಕ್",
    analyzing: "ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ...",
    recording: "ರೆಕಾರ್ಡಿಂಗ್...",
    name: "ಹೆಸರು:", email: "ಇಮೇಲ್:", age: "ವಯಸ್ಸು:", location: "ಸ್ಥಳ:",
    intakeHelp: "ನಾವು ಕೆಲವು ಸೌಮ್ಯ ಪ್ರಶ್ನೆಗಳನ್ನು ಕೇಳುತ್ತೇವೆ. ಉತ್ತರಿಸಲು ಬಯಸದಿದ್ದರೆ 'ಪಾಸ್' ಎಂದು ಹೇಳಿ.",
    stressDashboard: "ಒತ್ತಡ ಡ್ಯಾಶ್ಬೋರ್ಡ್"
  },
  ml: {
    appTitle: "MAMATHA: AI അധിഷ്ഠിത സഹചാരി ആപ്ലിക്കേഷൻ",
    feeling: "ഇന്ന് എങ്ങനെ തോന്നുന്നു?",
    send: "അയയ്ക്കുക", speak: "സംസാരിക്കുക", analyzeVoice: "എന്റെ ശബ്ദ സമ്മർദ്ദം വിശകലനം ചെയ്യുക",
    startCam: "ക്യാമറ ആരംഭിക്കുക", startSurvey: "ഡോക്ടർ സർവേ ആരംഭിക്കുക",
    pass: "ഒഴിവാക്കുക", reply: "മറുപടി നൽകുക", mic: "സംസാരിക്കുക",
    placeholder: "നിങ്ങളുടെ ചിന്തകൾ ടൈപ്പ് ചെയ്യുക..",
    intakePlaceholder: "നിങ്ങളുടെ ഉത്തരം ടൈപ്പ് ചെയ്യുക അല്ലെങ്കിൽ 'പാസ്' ക്ലിക്ക് ചെയ്യുക",
    stressTextPrefix: "സമ്മർദ്ദം",
    userDetails: "ഉപയോക്തൃ വിശദാംശങ്ങൾ",
    avgStress: "ശരാശരി സമ്മർദ്ദം (ഇന്ന്):",
    recentStress: "സമീപകാല സമ്മർദ്ദ നിലകൾ",
    historyTitle: "ചരിത്രം",
    guidedIntake: "ഗൈഡഡ് ഇന്റേക്ക്",
    analyzing: "വിശകലനം ചെയ്യുന്നു...",
    recording: "റെക്കോർഡിംഗ്...",
    name: "പേര്:", email: "ഇമെയിൽ:", age: "പ്രായം:", location: "സ്ഥലം:",
    intakeHelp: "ഞങ്ങൾ കുറച്ച് സൗമ്യമായ ചോദ്യങ്ങൾ ചോദിക്കും. ഉത്തരം നൽകാൻ താൽപ്പര്യമില്ലെങ്കിൽ 'പാസ്' പറയുക.",
    stressDashboard: "സമ്മർദ്ദ ഡാഷ്ബോർഡ്"
  }
};

const fallbackExtended = {
  ur: { name: "نام:", email: "ای میل:", age: "عمر:", location: "مقام:", feeling: "آج آپ کیسا محسوس کر رہے ہیں؟", send: "بھیجیں", speak: "بولیں", analyzeVoice: "میری آواز کا دباؤ تجزیہ کریں", startCam: "کیمرہ شروع کریں", startSurvey: "ڈاکٹر سروے شروع کریں", pass: "چھوڑیں", reply: "جواب دیں", mic: "بولیں", placeholder: "اپنے خیالات لکھیں..", intakePlaceholder: "اپنا جواب ٹائپ کریں یا 'پاس' کلک کریں", stressTextPrefix: "دباؤ", userDetails: "صارف کی تفصیلات", avgStress: "اوسط دباؤ (آج):", recentStress: "حالیہ دباؤ کی سطح", historyTitle: "تاریخ", guidedIntake: "رہنمائی شدہ انٹیک", analyzing: "تجزیہ ہو رہا ہے...", recording: "ریکارڈنگ...", intakeHelp: "ہم کچھ نرم سوالات پوچھیں گے۔ اگر آپ جواب نہیں دینا چاہتے تو 'پاس' کہیں۔", stressDashboard: "دباؤ ڈیش بورڈ", appTitle: "MAMATHA: AI پر مبنی ساتھی ایپلی کیشن" },
  pa: { name: "ਨਾਮ:", email: "ਈਮੇਲ:", age: "ਉਮਰ:", location: "ਸਥਾਨ:", feeling: "ਅੱਜ ਤੁਸੀਂ ਕਿਵੇਂ ਮਹਿਸੂਸ ਕਰ ਰਹੇ ਹੋ?", send: "ਭੇਜੋ", speak: "ਬੋਲੋ", analyzeVoice: "ਮੇਰੀ ਆਵਾਜ਼ ਦੇ ਤਣਾਅ ਦਾ విਸ਼ਲੇਸ਼ਣ ਕਰੋ", startCam: "ਕੈਮਰਾ ਸ਼ੁਰੂ ਕਰੋ", startSurvey: "ਡਾਕਟਰ ਸਰਵੇਖਣ ਸ਼ੁਰੂ ਕਰੋ", pass: "ਛੱਡੋ", reply: "ਜਵਾਬ ਦਿਓ", mic: "ਬੋਲੋ", placeholder: "ਆਪਣੇ ਵਿਚਾਰ ਲਿਖੋ..", intakePlaceholder: "ਆਪਣਾ ਜਵਾਬ ਟਾਈਪ ਕਰੋ ਜਾਂ 'ਪਾਸ' ਕਲਿੱक ਕਰੋ", stressTextPrefix: "ਤਣਾਅ", userDetails: "ਉਪਭੋਗਤਾ ਵੇਰਵੇ", avgStress: "ਔਸਤ ਤਣਾਅ (ਅੱਜ):", recentStress: "ਹਾਲੀਆ ਤਣਾਅ ਪੱਧਰ", historyTitle: "ਇਤਿਹਾས", guidedIntake: "ਗਾਈਡਡ ਇੰਟੇਕ", analyzing: "ਵਿਸ਼ਲੇਸ਼ਣ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...", recording: "ਰਿਕਾਰਡਿੰਗ...", intakeHelp: "ਅਸੀਂ ਕੁਝ ਕੋਮਲ ਸਵਾਲ ਪੁੱਛਾਂਗੇ। ਜੇਕਰ ਤੁਸੀਂ ਜਵਾਬ ਨਹੀਂ ਦੇਣਾ ਚਾਹੁੰਦੇ ਤਾਂ 'ਪਾਸ' ਕਹੋ।", stressDashboard: "ਤਣਾਅ ਡੈਸ਼ਬೋਰ್ڈ", appTitle: "MAMATHA: AI ਅਧਾਰਤ ਸਾਥੀ ਐਪਲੀਕੇਸ਼ਨ" },
  or: { name: "ନାମ:", email: "ଇମେଲ୍:", age: "ବୟସ:", location: "ସ୍ଥାନ:", feeling: "ଆଜି କେମିତି ଅନୁଭବ କରୁଛନ୍ତି?", send: "ପଠାନ୍ତୁ", speak: "କହନ୍ତୁ", analyzeVoice: "ମୋର ସ୍ୱର ଚାପ ବିଶ୍ଳେଷଣ କରନ୍ତୁ", startCam: "କ୍ୟାମେରା ଆରମ୍ଭ କରନ୍ତୁ", startSurvey: "ଡାକ୍ତର ସର୍ଭେ ଆରମ୍ଭ କରନ୍ତୁ", pass: "ଛାଡ଼ନ୍ତୁ", reply: "ଉତ୍ତର ଦିଅନ୍ତු", mic: "କହନ୍ତු", placeholder: "ଆପଣଙ୍କର ଚିନ୍ତାଧାରା ଟାଇପ୍ କରନ୍ତు..", intakePlaceholder: "ଆପଣଙ୍କର ଉତ୍ତର ଟାଇପ୍ କରନ୍ତు କିମ୍ବା 'ପାସ୍' କ୍ଲିକ୍ କରନ୍ତు", stressTextPrefix: "ଚାପ", userDetails: "ବ୍ୟବହାରକାରୀ ବିବରଣୀ", avgStress: "ହାରାହାରି ଚାପ (ଆଜି):", recentStress: "ସାମ୍ପ୍ରତିକ ଚାପ ସ୍ତର", historyTitle: "ଇତିହାସ", guidedIntake: "ଗାଇଡେଡ୍ ଇନ୍ଟେକ୍", analyzing: "ବିଶ୍ଳେଷଣ କରୁଛି...", recording: "ରେକର୍ଡିଂ...", intakeHelp: "ଆମେ କିଛି କୋମଳ ପ୍ରଶ୍ନ ପଚାରିବୁ। ଯଦି ଆପଣ ଉତ୍ତର ଦେବାକୁ ଚାହାଁନ୍ତି ନାହିଁ ତେବे 'ପାସ୍' କୁହନ୍ତୁ।", stressDashboard: "ଚାପ ଡ୍ୟାସବୋର୍ଡ", appTitle: "MAMATHA: AI ଆଧାରିତ ସାଥୀ ଆପ୍ଲିକେସନ୍" }
};

let currentLang = "en";

function getTranslation(langCode, key) {
  if (translations[langCode] && translations[langCode][key] !== undefined) {
    return translations[langCode][key];
  }
  if (fallbackExtended[langCode] && fallbackExtended[langCode][key] !== undefined) {
    return fallbackExtended[langCode][key];
  }
  return translations.en[key] || key;
}

function applyLanguageToPage(langCode) {
  currentLang = langCode;

  const setElText = (id, text) => {
    const el = document.getElementById(id);
    if (el) el.innerText = text;
  };

  const setElHTML = (id, html) => {
    const el = document.getElementById(id);
    if (el) el.innerHTML = html;
  };

  const setElPlaceholder = (id, text) => {
    const el = document.getElementById(id);
    if (el) el.placeholder = text;
  };

  // Update all UI elements with translations
  const appTitleRaw = getTranslation(langCode, "appTitle");
  setElHTML("appTitle", appTitleRaw.replace("MAMATHA", "<span class='mamatha-brand'>MAMATHA</span>"));
  setElText("feelingQuestion", getTranslation(langCode, "feeling"));
  setElText("send-btn", getTranslation(langCode, "send"));
  setElText("voice-btn", getTranslation(langCode, "speak"));
  setElText("start-record-btn", getTranslation(langCode, "analyzeVoice"));
  setElText("start-cam-btn", getTranslation(langCode, "startCam"));
  setElText("start-doctor-survey-btn", getTranslation(langCode, "startSurvey"));
  setElText("intake-pass-btn", getTranslation(langCode, "pass"));
  setElText("intake-submit-btn", getTranslation(langCode, "reply"));
  setElText("intake-mic-btn", getTranslation(langCode, "mic"));

  setElPlaceholder("message", getTranslation(langCode, "placeholder"));
  setElPlaceholder("intake-answer", getTranslation(langCode, "intakePlaceholder"));

  setElText("userDetailsTitle", getTranslation(langCode, "userDetails"));
  setElHTML("avgStressLabel", getTranslation(langCode, "avgStress"));
  setElText("recentStressLabel", getTranslation(langCode, "recentStress"));
  setElText("historyTitle", getTranslation(langCode, "historyTitle"));
  setElText("guidedIntakeTitle", getTranslation(langCode, "guidedIntake"));
  setElText("stressDashboardTitle", getTranslation(langCode, "stressDashboard"));
  setElText("intake-help", getTranslation(langCode, "intakeHelp"));

  // Update stress text prefix
  const stressTextEl = document.getElementById("stress-text");
  if (stressTextEl) {
    const currentStressValue = stressTextEl.innerText.split(":")[1] || "0%";
    stressTextEl.innerText = getTranslation(langCode, "stressTextPrefix") + ": " + currentStressValue;
  }

  // Update user detail labels
  const user = JSON.parse(localStorage.getItem("user"));
  if (user) {
    setElText("userName", getTranslation(langCode, "name") + " " + user.name);
    setElText("userEmail", getTranslation(langCode, "email") + " " + user.email);
    setElText("userAge", getTranslation(langCode, "age") + " " + user.age);
    setElText("userLocation", getTranslation(langCode, "location") + " " + user.location);
  } else {
    setElText("userName", getTranslation(langCode, "name") + " ");
    setElText("userEmail", getTranslation(langCode, "email") + " ");
    setElText("userAge", getTranslation(langCode, "age") + " ");
    setElText("userLocation", getTranslation(langCode, "location") + " ");
  }

  localStorage.setItem("mindmate_language", langCode);
  syncAvatarWithLanguageVoice(langCode);
}
// ======================== LOCALIZED WELCOME GREETING ========================
async function showLocalizedGreeting(language) {
  try {
    const res = await fetch(`/get_greeting?language=${language}`);
    const data = await res.json();

    if (data.success && data.greeting) {
      const aiMsg = document.createElement("div");
      aiMsg.className = "AIreply";
      aiMsg.innerText = "⚛ " + data.greeting;
      responseEl.appendChild(aiMsg);
      responseEl.scrollTop = responseEl.scrollHeight;

      playAvatarResponse(data, data.greeting, language);

      awaitingCommandAfterWake = true;
      console.log("[WakeWord] Greeting done — now listening for the reply automatically.");
    }
  } catch (err) {
    console.log("Error loading localized greeting:", err);
  }
}

// Language selector event listener
// Language selector event listener
const langSelect = document.getElementById("languageSelect");
langSelect.addEventListener("change", (e) => {
  applyLanguageToPage(e.target.value);
  showLocalizedGreeting(e.target.value);   // <-- NEW LINE
});

// Load saved language on page load
// Load saved language on page load
document.addEventListener("DOMContentLoaded", () => {
  const savedLang = localStorage.getItem("mindmate_language");
  if (savedLang && langSelect.querySelector(`option[value="${savedLang}"]`)) {
    langSelect.value = savedLang;
    applyLanguageToPage(savedLang);
  } else {
    applyLanguageToPage("en");
  }

  showLocalizedGreeting(currentLang);   // <-- NEW LINE
  enableWakeWordListening();
  loadHistory();
  startCamera();
  loadStressDashboard();

  const user = JSON.parse(localStorage.getItem("user"));
  if (user) {
    const t = (tObj) => getTranslation(currentLang, tObj);
    document.getElementById("userName").innerText = t("name") + " " + user.name;
    document.getElementById("userEmail").innerText = t("email") + " " + user.email;
    document.getElementById("userAge").innerText = t("age") + " " + user.age;
    document.getElementById("userLocation").innerText = t("location") + " " + user.location;
  }
});
// ======================== APP DOM ELEMENTS ========================
const form = document.getElementById("chat-form");
const messageInput = document.getElementById("message");
const responseEl = document.getElementById("response");
const voiceBtn = document.getElementById("voice-btn");
const startRecordBtn = document.getElementById("start-record-btn");
const stressBar = document.getElementById("stress-bar");
const stressTextEl = document.getElementById("stress-text");
const video = document.getElementById("userCam");
const speechStatus = document.getElementById("speech-status");
let videoStream = null;

let mediaRecorder = null;
let recordedChunks = [];
let isRecordingVoice = false;

// ======================== TEXT CHAT INTERACTION ========================
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = messageInput.value.trim();
  if (!message) return;

  // Show user message
  const userMsg = document.createElement("div");
  userMsg.className = "messageIn";
  userMsg.innerText = "👤 " + message;
  responseEl.appendChild(userMsg);

  // Show loading indicator
  const loadingMsg = document.createElement("div");
  loadingMsg.className = "AIreply";
  loadingMsg.innerText = "⚛ Thinking...";
  responseEl.appendChild(loadingMsg);
  responseEl.scrollTop = responseEl.scrollHeight;

  // Send message along with selected language
  const formData = new FormData();
  formData.append("message", message);
  formData.append("language", currentLang);

  try {
    const res = await fetch("/predict", { method: "POST", body: formData });
    const data = await res.json();

    loadingMsg.remove();

    const responseText = data.suggestion || "Thank you for sharing. I'm here to support you.";

    // AI reply
    const aiMsg = document.createElement("div");
    aiMsg.className = "AIreply";
    aiMsg.innerText = "⚛ " + responseText;
    responseEl.appendChild(aiMsg);
    messageInput.value = "";
    responseEl.scrollTop = responseEl.scrollHeight;

    // Update stress levels
    if (data.stress_score !== undefined) {
      updateStressBar(data.stress_score);
    }

    // Speak AI Response — the doctor always responds out loud, one way or another
    playAvatarResponse(data, responseText, currentLang);

    loadStressDashboard();
  } catch (err) {
    console.error("Chat error:", err);
    loadingMsg.innerText = "❌ Connection error";
  }
});

// ======================== AVATAR LIP-SYNC & GENDER SWITCHING ========================
let currentAvatarGender = "female";

function updateAvatarGender(gender) {
  if (currentAvatarGender === gender) return;
  currentAvatarGender = gender;

  const avatarImg = document.getElementById("ai-avatar-img");
  const avatarTalking = document.getElementById("ai-avatar-talking");
  if (!avatarImg) return;

  if (gender === 'male') {
    avatarImg.src = "/static/doctor_male.png";
    if (avatarTalking) avatarTalking.src = "/static/doctor_male_talking.png";
  } else {
    avatarImg.src = "/static/doctor_female.png";
    if (avatarTalking) avatarTalking.src = "/static/doctor_female_talking.png";
  }
}

function detectVoiceGender(voiceName) {
  const name = voiceName.toLowerCase();
  if (name.includes("male") || name.includes("david") || name.includes("mark") || name.includes("george") || name.includes("ravi") || name.includes("harsh") || name.includes("standard-b") || name.includes("wavenet-b") || name.includes("neural-b")) {
    return "male";
  }
  return "female";
}

function syncAvatarWithLanguageVoice(language) {
  if (!('speechSynthesis' in window)) {
    if (language === 'en') {
      updateAvatarGender('male');
    } else {
      updateAvatarGender('female');
    }
    return;
  }
  const voices = window.speechSynthesis.getVoices();
  const langMap = {
    'en': 'en-US', 'hi': 'hi-IN', 'te': 'te-IN', 'ta': 'ta-IN',
    'kn': 'kn-IN', 'ml': 'ml-IN', 'bn': 'bn-IN', 'gu': 'gu-IN',
    'mr': 'mr-IN', 'pa': 'pa-IN', 'ur': 'ur-PK', 'or': 'or-IN'
  };
  const targetLang = langMap[language] || 'en-US';
  const nativeVoice = voices.find(v => v.lang.toLowerCase().replace('_', '-').startsWith(language.toLowerCase()));
  if (nativeVoice) {
    const gender = detectVoiceGender(nativeVoice.name);
    updateAvatarGender(gender);
  } else {
    if (language === 'en') {
      updateAvatarGender('male');
    } else {
      updateAvatarGender('female');
    }
  }
}

// ---- Real, audio-driven lip-sync -----------------------------------------
// Crossfades between two real photos of the doctor — one mouth-closed
// (#ai-avatar-img, always the base layer) and one mouth-open mid-speech
// (#ai-avatar-talking, layered on top) — driven by the actual amplitude of
// the spoken audio. Because both photos share the same pose/lighting/crop,
// the crossfade reads as genuine talking rather than a stretched/warped
// mouth. Falls back to a natural randomized flap pattern if the browser
// can't analyse the audio stream (e.g. autoplay/CORS restrictions).
let audioCtx = null;
let audioAnalyser = null;
let lipSyncAnimFrame = null;
let isAnalysing = false;
let simulateInterval = null;

function startLipSync(audioElement = null) {
  stopLipSync();
  const container = document.getElementById("vid-res");
  const avatarTalking = document.getElementById("ai-avatar-talking");

  if (container) container.classList.add("speaking");

  if (audioElement && (window.AudioContext || window.webkitAudioContext)) {
    try {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }

      if (!audioElement.mediaElementSource) {
        audioElement.mediaElementSource = audioCtx.createMediaElementSource(audioElement);
      }

      if (!audioAnalyser) {
        audioAnalyser = audioCtx.createAnalyser();
        audioAnalyser.fftSize = 256;
      }

      audioElement.mediaElementSource.disconnect();
      audioElement.mediaElementSource.connect(audioAnalyser);
      audioAnalyser.connect(audioCtx.destination);

      const bufferLength = audioAnalyser.frequencyBinCount;
      const dataArray = new Uint8Array(bufferLength);

      isAnalysing = true;
      let smoothed = 0;

      function renderFrame() {
        if (!isAnalysing) return;
        lipSyncAnimFrame = requestAnimationFrame(renderFrame);
        audioAnalyser.getByteFrequencyData(dataArray);

        // Focus on the speech-relevant frequency band that tracks vowel
        // energy (open-mouth sounds), skipping the very low hum/plosive bins.
        let sum = 0;
        for (let i = 2; i < 45; i++) {
          sum += dataArray[i];
        }
        let average = sum / 43;

        let level = Math.min(average / 95, 1);
        level = Math.max(0, level - 0.05);
        // Slight curve so quiet moments snap closed and louder syllables
        // reach a fully-open mouth, instead of hovering half-blended.
        level = Math.pow(level, 0.65);

        // Exponential smoothing avoids single-frame flicker while staying
        // responsive enough to look like real syllables.
        smoothed += (level - smoothed) * 0.5;

        if (avatarTalking) {
          avatarTalking.style.opacity = smoothed.toFixed(2);
        }
      }

      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      renderFrame();

    } catch (e) {
      console.warn("Audio analyser could not be attached, falling back:", e);
      simulateLipSync(avatarTalking);
    }
  } else {
    simulateLipSync(avatarTalking);
  }
}

function simulateLipSync(avatarTalking) {
  simulateInterval = setInterval(() => {
    const level = Math.random() > 0.3 ? Math.random() * 0.9 : 0;
    if (avatarTalking) {
      avatarTalking.style.opacity = level.toFixed(2);
    }
  }, 130);
}

function stopLipSync() {
  const container = document.getElementById("vid-res");
  const avatarTalking = document.getElementById("ai-avatar-talking");

  if (container) container.classList.remove("speaking");

  isAnalysing = false;
  if (lipSyncAnimFrame) cancelAnimationFrame(lipSyncAnimFrame);
  if (simulateInterval) clearInterval(simulateInterval);
  simulateInterval = null;

  if (avatarTalking) avatarTalking.style.opacity = '0';
}

if ('speechSynthesis' in window) {
  window.speechSynthesis.onvoiceschanged = () => {
    syncAvatarWithLanguageVoice(currentLang);
  };
}

// ---- Single entry point for "make the doctor respond" --------------------
// Every place that used to duplicate the video/audio playback logic now
// calls this instead. Order of preference: talking-head video (if the
// backend sent one) → generated speech audio → last-resort browser TTS.
// Crucially, if a preferred option fails or its element is missing, we
// fall through to the next one instead of silently doing nothing (this was
// the bug causing the doctor to sometimes just sit there after a reply).
function playAvatarResponse(data, fallbackText, language) {
  const avatarImg = document.getElementById("ai-avatar-img");
  const avatarVid = document.getElementById("ai-avatar-video");
  const container = document.getElementById("vid-res");

  if (data && data.video_url && avatarImg && avatarVid) {
    avatarImg.style.display = "none";
    avatarVid.style.display = "block";
    avatarVid.src = data.video_url;
    avatarVid.crossOrigin = "anonymous";
    avatarVid.onplay = () => { if (container) container.classList.add("speaking"); };
    avatarVid.onended = () => {
      if (container) container.classList.remove("speaking");
      avatarVid.style.display = "none";
      avatarImg.style.display = "block";
    };
    avatarVid.onerror = () => {
      avatarVid.style.display = "none";
      avatarImg.style.display = "block";
      playWithAudioOrTTS(data, fallbackText, language);
    };
    avatarVid.play().catch(() => {
      avatarVid.style.display = "none";
      avatarImg.style.display = "block";
      playWithAudioOrTTS(data, fallbackText, language);
    });
    return;
  }

  playWithAudioOrTTS(data, fallbackText, language);
}

function playWithAudioOrTTS(data, fallbackText, language) {
  if (data && data.audio_url) {
    const audio = new Audio(data.audio_url);
    audio.crossOrigin = "anonymous";
    audio.addEventListener("play", () => startLipSync(audio));
    audio.addEventListener("ended", () => stopLipSync());
    audio.addEventListener("pause", () => stopLipSync());
    audio.addEventListener("error", () => {
      stopLipSync();
      speakText(fallbackText, language);
    });
    audio.play().catch(() => {
      speakText(fallbackText, language);
    });
    return;
  }
  speakText(fallbackText, language);
}

// ======================== AUDIO OUTPUT (TTS) ========================
function speakText(text, language) {
  if (!text) return;
  stopLipSync();

  fetch('/speak', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: text, language: language })
  })
    .then(response => {
      if (!response.ok) throw new Error('Audio generation failed');
      return response.blob();
    })
    .then(blob => {
      const audioUrl = URL.createObjectURL(blob);
      const audio = new Audio(audioUrl);
      audio.crossOrigin = "anonymous";
      audio.addEventListener("play", () => startLipSync(audio));
      audio.addEventListener("ended", () => stopLipSync());
      audio.addEventListener("pause", () => stopLipSync());
      audio.addEventListener("error", () => {
        stopLipSync();
        fallbackToBrowserTTS(text, language);
      });
      audio.play().catch(e => {
        console.log("Audio play failed", e);
        fallbackToBrowserTTS(text, language);
      });
    })
    .catch(error => {
      console.error('Error fetching TTS:', error);
      fallbackToBrowserTTS(text, language);
    });
}

function fallbackToBrowserTTS(text, language) {
  if (!('speechSynthesis' in window)) return;
  const utterance = new SpeechSynthesisUtterance(text);
  const speechLangMap = {
    'en': 'en-IN', 'hi': 'hi-IN', 'bn': 'bn-IN', 'te': 'te-IN',
    'mr': 'mr-IN', 'ta': 'ta-IN', 'gu': 'gu-IN', 'kn': 'kn-IN',
    'ml': 'ml-IN', 'pa': 'pa-IN', 'ur': 'ur-IN', 'or': 'or-IN'
  };
  utterance.lang = speechLangMap[language] || 'en-US';
  
  const voices = window.speechSynthesis.getVoices();
  let selectedVoice = null;
  
  const femaleNames = ['female', 'zira', 'samantha', 'swara', 'kalpana', 'shruti', 'neerja', 'sushma', 'tulsi', 'veena', 'meera', 'bina', 'kavya', 'pallavi', 'anjali'];
  const maleNames = ['male', 'david', 'mark', 'hemant', 'ravi', 'vallabh', 'madhur', 'nitin', 'rahul', 'amit'];

  const isFemaleVoice = (voice) => {
    const name = voice.name.toLowerCase();
    // Exclude known male names
    if (maleNames.some(m => name.includes(m))) return false;
    // Prefer known female names or Google defaults (which are usually female)
    if (femaleNames.some(f => name.includes(f)) || name.includes('google')) return true;
    return false;
  };
  
  // 1. Try to find a definitively female voice for the target language
  selectedVoice = voices.find(v => v.lang.includes(utterance.lang) && isFemaleVoice(v));
  
  // 2. Try any voice for the target language that isn't explicitly male
  if (!selectedVoice) {
    selectedVoice = voices.find(v => v.lang.includes(utterance.lang) && !maleNames.some(m => v.name.toLowerCase().includes(m)));
  }
  
  // 3. Try ANY voice for the target language
  if (!selectedVoice) {
    selectedVoice = voices.find(v => v.lang.includes(utterance.lang));
  }
  
  // 4. Last resort: any female English voice
  if (!selectedVoice) {
    selectedVoice = voices.find(v => isFemaleVoice(v) && v.lang.includes('en'));
  }
  
  if (selectedVoice) {
    utterance.voice = selectedVoice;
  }
  
  utterance.onstart = () => startLipSync();
  utterance.onend = () => stopLipSync();
  utterance.onerror = () => stopLipSync();
  
  window.speechSynthesis.speak(utterance);
}

// ======================== VOICE CONVERSATION (SPEAK BUTTON) ========================
let recognition = null;
let isListeningBrowser = false;

if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  recognition = new SpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = true;

  recognition.onstart = () => {
    isListeningBrowser = true;
    voiceBtn.innerText = "🔴 Listening... Speak now";
    voiceBtn.style.background = "#dc2626";
    speechStatus.innerText = "🎙️ Hearing your voice...";
  };

  recognition.onend = () => {
    isListeningBrowser = false;
    voiceBtn.innerText = getTranslation(currentLang, "speak");
    voiceBtn.style.background = "";
    if (typeof enableWakeWordListening === "function") {
      enableWakeWordListening();
    }
  };

  recognition.onresult = async (event) => {
    const result = event.results[event.results.length - 1];
    const transcript = result[0].transcript;

    if (result.isFinal) {
      speechStatus.innerText = `✅ Transcript: "${transcript}"`;

      // Render user transcript in chat
      const userMsg = document.createElement("div");
      userMsg.className = "messageIn";
      userMsg.innerText = "👤 " + transcript;
      responseEl.appendChild(userMsg);
      responseEl.scrollTop = responseEl.scrollHeight;

      // Send to process_voice
      const loadingMsg = document.createElement("div");
      loadingMsg.className = "AIreply";
      loadingMsg.innerText = "⚛ Thinking...";
      responseEl.appendChild(loadingMsg);
      responseEl.scrollTop = responseEl.scrollHeight;

      try {
        const res = await fetch("/process_voice", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: transcript, language: currentLang, gender: currentAvatarGender })
        });
        const data = await res.json();

        loadingMsg.remove();

        if (data.success) {
          const aiMsg = document.createElement("div");
          aiMsg.className = "AIreply";
          aiMsg.innerText = "⚛ " + data.ai_response;
          responseEl.appendChild(aiMsg);
          responseEl.scrollTop = responseEl.scrollHeight;

          updateStressBar(data.stress_score);

          // The doctor always speaks back — video, generated audio, or
          // browser TTS, whichever is available, in the user's language.
          playAvatarResponse(data, data.ai_response, currentLang);

          loadStressDashboard();
        }
      } catch (err) {
        loadingMsg.innerText = "❌ Connection error";
      }
    } else {
      speechStatus.innerText = `🎙️ Hearing: "${transcript}"`;
    }
  };

  recognition.onerror = (e) => {
    console.error("SpeechRecognition error:", e);
    if (e.error === 'aborted') {
      speechStatus.innerText = "🎙️ Microphone stopped.";
    } else if (e.error === 'no-speech') {
      speechStatus.innerText = "🎙️ No speech detected. Try again.";
    } else {
      speechStatus.innerText = `❌ Error: ${e.error}`;
    }
    isListeningBrowser = false;
    voiceBtn.innerText = getTranslation(currentLang, "speak");
    voiceBtn.style.background = "";
  };
}

voiceBtn.addEventListener("click", () => {
  if (!recognition) {
    alert("Speech Recognition API is not supported in this browser. Please use Google Chrome.");
    return;
  }
  if (isListeningBrowser) {
    recognition.stop();
  } else {
    // Temporarily pause wake word listener to free up the microphone
    if (typeof disableWakeWordListening === "function") {
      disableWakeWordListening();
    }
    const speechLangMap = {
      'en': 'en-US', 'hi': 'hi-IN', 'bn': 'bn-IN', 'te': 'te-IN',
      'mr': 'mr-IN', 'ta': 'ta-IN', 'gu': 'gu-IN', 'kn': 'kn-IN',
      'ml': 'ml-IN', 'pa': 'pa-IN', 'ur': 'ur-IN', 'or': 'or-IN'
    };
    recognition.lang = speechLangMap[currentLang] || 'en-US';
    
    // Start after a slight delay to ensure wake word released the mic
    setTimeout(() => {
      try {
        recognition.start();
      } catch (err) {
        console.error("Could not start recognition:", err);
      }
    }, 300);
  }
});

// ======================== VOICE STRESS ANALYSIS ========================
startRecordBtn.addEventListener("click", () => {
  if (isRecordingVoice) {
    stopVoiceRecording();
  } else {
    startVoiceRecording();
  }
});

async function startVoiceRecording() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recordedChunks = [];
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = e => {
      if (e.data.size > 0) recordedChunks.push(e.data);
    };

    mediaRecorder.onstop = async () => {
      stream.getTracks().forEach(track => track.stop());
      const audioBlob = new Blob(recordedChunks, { type: "audio/webm" });

      speechStatus.innerText = "📊 Analyzing voice stress...";

      const loadingMsg = document.createElement("div");
      loadingMsg.className = "AIreply";
      loadingMsg.innerText = "⚛ Analyzing your voice...";
      responseEl.appendChild(loadingMsg);
      responseEl.scrollTop = responseEl.scrollHeight;

      try {
        const formData = new FormData();
        formData.append("audio", audioBlob);

        const res = await fetch(`/analyze_voice_stress?language=${currentLang}`, {
          method: "POST",
          body: formData
        });
        const data = await res.json();

        loadingMsg.remove();

        if (data.success) {
          speechStatus.innerText = `🎧 ${data.emotion} • Stress: ${data.stress_score}%`;

          // Append transcript
          const userMsg = document.createElement("div");
          userMsg.className = "messageIn";
          userMsg.innerText = `👤 [Voice] ${data.transcript}`;
          responseEl.appendChild(userMsg);

          // Append AI response
          const aiMsg = document.createElement("div");
          aiMsg.className = "AIreply";
          aiMsg.innerText = "⚛ " + data.ai_response;
          responseEl.appendChild(aiMsg);
          responseEl.scrollTop = responseEl.scrollHeight;

          updateStressBar(data.stress_score);
          playAvatarResponse(data, data.ai_response, currentLang);
          loadStressDashboard();
        } else {
          speechStatus.innerText = "❌ Analysis failed";
        }
      } catch (err) {
        console.error("STT error:", err);
        loadingMsg.innerText = "❌ Connection error";
      }
    };

    mediaRecorder.start();
    isRecordingVoice = true;
    startRecordBtn.innerText = "⏹ Stop Recording";
    startRecordBtn.style.background = "#dc2626";
    speechStatus.innerText = "🎙️ Recording audio (speak for stress analysis)...";

    // Auto-stop recording after 10 seconds
    setTimeout(() => {
      if (isRecordingVoice) stopVoiceRecording();
    }, 10000);
  } catch (err) {
    console.error("Microphone capture failed:", err);
    speechStatus.innerText = "❌ Microphone access denied";
  }
}

function stopVoiceRecording() {
  if (mediaRecorder && isRecordingVoice) {
    mediaRecorder.stop();
    isRecordingVoice = false;
    startRecordBtn.innerText = getTranslation(currentLang, "analyzeVoice");
    startRecordBtn.style.background = "";
  }
}

// ======================== CAMERA EMOTION ANALYSIS ========================
async function startCamera() {
  try {
    videoStream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = videoStream;
    setInterval(sendFrameForAnalysis, 5000);
  } catch (err) {
    console.warn("Webcam access declined or not available:", err);
  }
}

async function sendFrameForAnalysis() {
  if (!videoStream || video.paused || video.ended) return;

  const canvas = document.createElement("canvas");
  canvas.width = video.videoWidth || 320;
  canvas.height = video.videoHeight || 240;
  const ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  const imgData = canvas.toDataURL("image/jpeg");

  try {
    const res = await fetch("/analyze_face", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image: imgData })
    });
    const data = await res.json();
    if (data.success) {
      const stress = data.stress_score || 0;
      updateStressBar(stress);
    }
  } catch (err) {
    console.log("Facial analysis API offline");
  }
}

function updateStressBar(stress) {
  stressBar.style.width = `${stress}%`;
  stressBar.style.background = stress > 70 ? '#ef4444' : (stress > 40 ? '#f97316' : '#22c55e');
  stressTextEl.innerText = `${getTranslation(currentLang, "stressTextPrefix")}: ${stress}%`;
}

document.getElementById('start-cam-btn').addEventListener("click", startCamera);

// ======================== GUIDED DOCTOR SURVEY ========================
let currentIntakeQuestion = null;
let intakeSessionId = null;

async function startIntake() {
  try {
    const res = await fetch("/start_intake", { method: "POST" });
    const j = await res.json();
    intakeSessionId = j.session_id;
    if (j.first_question) {
      showQuestion(j.first_question);
    }
  } catch (err) {
    console.error("Intake start error:", err);
  }
}

function showQuestion(q, skipSpeak = false) {
  currentIntakeQuestion = q;
  document.getElementById("intake-question").innerText = q.text || "";
  document.getElementById("intake-progress").innerText = `Question ${q.id} of 5`;
  if (!skipSpeak) {
    speakText(q.text, currentLang);
  }
}

async function submitIntakeAnswer(ans = null) {
  const ansInput = document.getElementById("intake-answer");
  const answerVal = ans || ansInput.value.trim();
  if (!answerVal && answerVal !== "pass") return;

  // Render user response in chat
  const userMsg = document.createElement("div");
  userMsg.className = "messageIn";
  userMsg.innerText = `📋 Survey Q${currentIntakeQuestion?.id || ""}: ` + answerVal;
  responseEl.appendChild(userMsg);
  responseEl.scrollTop = responseEl.scrollHeight;

  ansInput.value = "";

  try {
    const res = await fetch("/submit_answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question_id: currentIntakeQuestion?.id,
        answer: answerVal,
        session_id: intakeSessionId
      })
    });
    const data = await res.json();

    // Render AI feedback
    const aiMsg = document.createElement("div");
    aiMsg.className = "AIreply";
    aiMsg.innerText = "⚛ " + data.reply;
    responseEl.appendChild(aiMsg);
    responseEl.scrollTop = responseEl.scrollHeight;

    let feedbackText = data.reply || "";
    if (data.urgent && data.urgent_message) {
      feedbackText += ". Warning: " + data.urgent_message;
    }

    if (data.urgent && data.urgent_message) {
      const alertMsg = document.createElement("div");
      alertMsg.className = "AIreply";
      alertMsg.style.borderColor = "red";
      alertMsg.innerText = "⚠️ " + data.urgent_message;
      responseEl.appendChild(alertMsg);
      responseEl.scrollTop = responseEl.scrollHeight;
    }

    // Fetch next or complete
    if (data.next_question) {
      showQuestion(data.next_question, true);
      feedbackText += ". " + data.next_question.text;
    } else if (data.done) {
      document.getElementById("intake-question").innerText = "✅ Intake complete! Thank you for sharing.";
      document.getElementById("intake-progress").innerText = "Completed";
      document.getElementById("intake-answer").disabled = true;
      document.getElementById("intake-submit-btn").disabled = true;
      document.getElementById("intake-pass-btn").disabled = true;
      document.getElementById("intake-mic-btn").disabled = true;
      feedbackText += ". Intake complete! Thank you for sharing.";
    }

    if (feedbackText) {
      speakText(feedbackText, currentLang);
    }
  } catch (err) {
    console.error("Intake submit error:", err);
  }
}

// Intake Speech Input
function startIntakeSpeech() {
  if (!('webkitSpeechRecognition' in window || 'SpeechRecognition' in window)) return;
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recog = new SpeechRecognition();
  const speechLangMap = {
    'en': 'en-US', 'hi': 'hi-IN', 'bn': 'bn-IN', 'te': 'te-IN',
    'mr': 'mr-IN', 'ta': 'ta-IN', 'gu': 'gu-IN', 'kn': 'kn-IN',
    'ml': 'ml-IN', 'pa': 'pa-IN', 'ur': 'ur-IN', 'or': 'or-IN'
  };
  recog.lang = speechLangMap[currentLang] || 'en-US';
  recog.onstart = () => {
    document.getElementById("intake-mic-btn").innerText = "🎙️ Listening...";
  };
  recog.onend = () => {
    document.getElementById("intake-mic-btn").innerText = getTranslation(currentLang, "mic");
  };
  recog.onresult = (e) => {
    const transcript = e.results[0][0].transcript;
    document.getElementById("intake-answer").value = transcript;
  };
  recog.start();
}

document.getElementById("start-doctor-survey-btn").addEventListener("click", startIntake);
document.getElementById("intake-submit-btn").addEventListener("click", () => submitIntakeAnswer());
document.getElementById("intake-pass-btn").addEventListener("click", () => submitIntakeAnswer("pass"));
document.getElementById("intake-mic-btn").addEventListener("click", startIntakeSpeech);

// ======================== HISTORY AND DASHBOARDS ========================
async function loadHistory() {
  try {
    const res = await fetch("/get_history");
    const data = await res.json();
    if (data.success && data.history) {
      const historyCont = document.getElementById("historyCont");

      // Clear older elements except header
      const title = document.getElementById("historyTitle");
      historyCont.innerHTML = "";
      historyCont.appendChild(title);

      data.history.forEach(chat => {
        const userMsg = document.createElement("div");
        userMsg.className = "messageIn";
        userMsg.innerText = "👤 " + chat.user_message;
        const aiMsg = document.createElement("div");
        aiMsg.className = "AIreply";
        aiMsg.innerText = "⚛ " + chat.ai_response;
        historyCont.appendChild(userMsg);
        historyCont.appendChild(aiMsg);
      });
    }
  } catch (err) {
    console.log("Error loading history logs");
  }
}

async function loadStressDashboard() {
  try {
    const res = await fetch("/get_stress_data");
    const data = await res.json();
    if (data.success) {
      document.getElementById("avgStressValue").innerText = data.average_stress ? data.average_stress + "%" : "0%";
      const list = document.getElementById("recentStressList");
      if (list) {
        list.innerHTML = "";
        (data.logs || []).forEach(entry => {
          const item = document.createElement("div");
          item.innerText = `${entry.timestamp?.split(" ")[1] || ""} — ${entry.emotion || "Neutral"} (${entry.stress_score || 0}%)`;
          list.appendChild(item);
        });
      }
    }
  } catch (err) {
    console.log("Error loading stress logs");
  }
}

// Auto-update dashboard periodically
setInterval(loadStressDashboard, 10000);
// ======================== "HEY MINDMATE" WAKE-WORD LISTENING ========================
// Runs continuous browser speech recognition and watches for "hey mindmate"
// (or common mispronunciations) in what it hears. On detection, the doctor
// responds "How can I help you?" and then treats the *next* thing the person
// says as their actual message — same as pressing the Speak button, just
// without needing to find or read a button first.

let wakeWordRecognition = null;
let isWakeWordListening = false;
let awaitingCommandAfterWake = false;

const WAKE_PHRASES = ["hey mamatha", "hi mamatha", "hello mamatha", "mamatha"];

function containsWakePhrase(transcript) {
  const t = transcript.toLowerCase();
  return WAKE_PHRASES.some(phrase => t.includes(phrase));
}

function startWakeWordListening() {
  if (!('webkitSpeechRecognition' in window || 'SpeechRecognition' in window)) {
    console.warn("Speech recognition not supported — wake word disabled.");
    return;
  }
  if (isWakeWordListening) return;

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  wakeWordRecognition = new SpeechRecognition();
  wakeWordRecognition.continuous = true;
  wakeWordRecognition.interimResults = true;
  wakeWordRecognition.lang = 'en-US'; // wake phrase itself stays in English regardless of UI language

  wakeWordRecognition.onstart = () => {
    isWakeWordListening = true;
  };

  wakeWordRecognition.onresult = async (event) => {
    const result = event.results[event.results.length - 1];
    const transcript = result[0].transcript;

    if (awaitingCommandAfterWake && result.isFinal) {
      awaitingCommandAfterWake = false;
      handleWakeWordCommand(transcript);
      return;
    }

    if (!awaitingCommandAfterWake && containsWakePhrase(transcript)) {
      awaitingCommandAfterWake = true;

      const wakeReplyText = getTranslation(currentLang, "wakeReply") || "How can I help you?";
      const aiMsg = document.createElement("div");
      aiMsg.className = "AIreply";
      aiMsg.innerText = "⚛ " + wakeReplyText;
      responseEl.appendChild(aiMsg);
      responseEl.scrollTop = responseEl.scrollHeight;

      speakText(wakeReplyText, currentLang);
    }
  };

  wakeWordRecognition.onerror = (e) => {
    console.warn("Wake word recognition error:", e.error);
  };

  // Browser speech recognition auto-stops after a period of silence —
  // restart it immediately so listening is effectively continuous.
  wakeWordRecognition.onend = () => {
    isWakeWordListening = false;
    if (wakeWordShouldRun) {
      setTimeout(() => startWakeWordListening(), 300);
    }
  };

  wakeWordRecognition.start();
}

async function handleWakeWordCommand(transcript) {
  const userMsg = document.createElement("div");
  userMsg.className = "messageIn";
  userMsg.innerText = "👤 " + transcript;
  responseEl.appendChild(userMsg);
  responseEl.scrollTop = responseEl.scrollHeight;

  const loadingMsg = document.createElement("div");
  loadingMsg.className = "AIreply";
  loadingMsg.innerText = "⚛ Thinking...";
  responseEl.appendChild(loadingMsg);
  responseEl.scrollTop = responseEl.scrollHeight;

  try {
    const res = await fetch("/process_voice", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: transcript, language: currentLang, gender: currentAvatarGender })
    });
    const data = await res.json();
    loadingMsg.remove();

    if (data.success) {
      const aiMsg = document.createElement("div");
      aiMsg.className = "AIreply";
      aiMsg.innerText = "⚛ " + data.ai_response;
      responseEl.appendChild(aiMsg);
      responseEl.scrollTop = responseEl.scrollHeight;

      updateStressBar(data.stress_score);
      playAvatarResponse(data, data.ai_response, currentLang);
      loadStressDashboard();
    }
  } catch (err) {
    loadingMsg.innerText = "❌ Connection error";
  }
}

let wakeWordShouldRun = false;

function enableWakeWordListening() {
  wakeWordShouldRun = true;
  startWakeWordListening();
}

function disableWakeWordListening() {
  wakeWordShouldRun = false;
  if (wakeWordRecognition) {
    wakeWordRecognition.stop();
  }
}
