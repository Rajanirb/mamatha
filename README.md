# Mamatha

A Flask application with multilingual conversations, voice support, and face-based wellbeing check-ins.

## Local setup

Create and activate a Python 3.11 virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Enter your `SARVAM_API_KEY` in `.env`. The SMTP settings are optional and are used for password reset emails.

Initialize a new local database and start the application:

```powershell
python init_db.py
python app.py
```

Open `http://localhost:5000`.

The virtual environment, credentials, local database, user history, and generated audio are excluded from Git. Each installation creates its own runtime data.
