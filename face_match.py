import sqlite3
import json
import numpy as np

def cosine_similarity(a, b):
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))

def find_user(current_embedding):

    conn = sqlite3.connect("mindmate.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email, embedding FROM users"
    )

    users = cursor.fetchall()
    conn.close()

    best_score = 0.0
    best_user = None

    for user in users:
        if not user[3] or str(user[3]).strip() == "":
            continue
            
        try:
            saved_embedding = np.array(
                json.loads(user[3]),
                dtype=np.float32
            )
        except Exception as e:
            print(f"Error parsing embedding for user {user[1]}: {e}")
            continue

        score = cosine_similarity(
            np.array(current_embedding, dtype=np.float32),
            saved_embedding
        )

        print(f"Face match check: {user[1]} ({user[2]}) -> Score: {score:.4f}")

        if score > best_score:
            best_score = score
            best_user = user

    print(f"Best match result: score={best_score:.4f}, user={best_user[1] if best_user else 'None'}")

    if best_score > 0.40:
        return best_user

    return None