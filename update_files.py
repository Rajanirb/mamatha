import os

project_dir = r"c:\Users\IIITDMK\Desktop\mindmatevoice"

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Common user-visible replacements (case-sensitive to avoid breaking variables/files which are lowercase mindmate)
    content = content.replace("MindMate", "MAMATHA")
    content = content.replace("MINDMATE", "MAMATHA")
    
    # Fix the email address that might have been accidentally replaced
    content = content.replace("admin@MAMATHA.com", "admin@mindmate.com")
    content = content.replace("admin@mamatha.com", "admin@mindmate.com")
    
    # Make MAMATHA bold/styled in places where it's a logo or wordmark
    # In login 2.html, the logo is `<div class="logo">MAMATHA</div>`
    # In other places, maybe `<div class="wordmark">... MAMATHA</div>` or similar
    # Let's add <strong> for MAMATHA in standard places if it's not inside a tag attribute
    # Actually, the user asked to "Make MAMATHA bold and aesthetically styled where it appears as the main logo/wordmark."
    # We can do this with CSS updates or by finding the logo class.
    # We'll handle the styling manually or through specific replacements.
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

# Update HTML files
html_files = [
    "admin_dashboard.html", "admin_login.html", "admin_register.html", 
    "doctor_dashboard.html", "doctor_login.html", "doctor_register.html", 
    "entry.html", "index.html", "login 2.html"
]

for filename in html_files:
    filepath = os.path.join(project_dir, filename)
    if os.path.exists(filepath):
        replace_in_file(filepath)

# Update app.py
replace_in_file(os.path.join(project_dir, "app.py"))

# Update i18n.js
replace_in_file(os.path.join(project_dir, "static", "i18n.js"))

print("Branding update script complete.")
