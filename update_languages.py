import re
import os

project_dir = r"c:\Users\IIITDMK\Desktop\mindmatevoice"
filepath = os.path.join(project_dir, 'app.py')

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "माइंडमेट": "ममता",
    "మైండ్మేట్": "మమత",
    "মাইন্ডমেট": "মমতা",
    "மைண்ட்மேட்": "மமதா",
    "مائنڈ میٹ": "ممتا",
    "માઇન્ડમેટ": "મમતા",
    "ಮೈಂಡ್‌ಮೇಟ್": "ಮಮತಾ",
    "മൈൻഡ്മേറ്റ്": "മമത",
    "ਮਾਈਂਡਮੇਟ": "ਮਮਤਾ",
    "ମାଇଣ୍ଡମେଟ୍": "ମମତା"
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated app.py")
