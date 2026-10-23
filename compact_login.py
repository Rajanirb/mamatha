import os

project_dir = r"c:\Users\IIITDMK\Desktop\mindmatevoice"
filepath = os.path.join(project_dir, "login 2.html")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the page more compact

# 1. Container and ProjectDet width/height adjustments
content = content.replace("width: 400px;", "width: 360px;")
content = content.replace(".projectDet, .container { height: 640px; }", ".projectDet, .container { height: auto; max-height: 90vh; }")
content = content.replace("align-items: stretch;", "align-items: center;")

# 2. Adjust paddings and margins for more compactness
content = content.replace("padding: 24px 32px;", "padding: 16px 20px;")
content = content.replace(".projectDet { padding: 14px 18px;", ".projectDet { padding: 12px 14px;")
content = content.replace(".form { padding: 16px 18px;", ".form { padding: 12px 14px;")

# 3. Logo and inputs
content = content.replace("font-size: 30px;", "font-size: 22px;")
content = content.replace(".header-logo-img { width: 56px; height: 56px; }", ".header-logo-img { width: 44px; height: 44px; }")
content = content.replace(".header-logo-img { width: 100px; height: 100px;", ".header-logo-img { width: 44px; height: 44px;")

content = content.replace("margin-bottom: 20px;", "margin-bottom: 12px;")
content = content.replace("margin-bottom: 16px;", "margin-bottom: 10px;")
content = content.replace("margin-top: 12px;", "margin-top: 8px;")

# 4. Videos
content = content.replace("width: 190px !important; height: 145px !important;", "width: 160px !important; height: 120px !important;")
content = content.replace('width="250" height="190"', 'width="180" height="135"')
content = content.replace('width="250" autoplay', 'width="180" autoplay')

# 5. Inputs and buttons
content = content.replace("padding: 10px 12px;", "padding: 8px 10px;")
content = content.replace("padding: 10px 14px;", "padding: 8px 12px;")
content = content.replace("margin: 8px auto;", "margin: 6px auto;")

# 6. Additional smaller text/padding fixes
content = content.replace("padding: 24px;", "padding: 16px;")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Compacted login 2.html CSS")
