# 🔐 Designing Secure Biometric Authentication System

A secure biometric authentication system built using Django and deployed on Vercel.

---

## 📌 Features

- User Authentication
- Secure Biometric Verification
- Django Backend
- Responsive UI
- Static File Handling with WhiteNoise
- Vercel Deployment Support
- Production Ready Configuration

---

# 📁 Project Structure

```bash
designing_secure_biometric/
│
├── manage.py
├── requirements.txt
├── vercel.json
├── README.md
│
├── biometric_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── biometric_app/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── migrations/
│
├── static/
└── media/
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/buddasreelatha57/designing_secure_biometric.git
cd designing_secure_biometric
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```


## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create a `requirements.txt` file with:

```txt
Django>=5.0
python
cryptography
opencv-contrib-python
 pillow
 pymysql
```

---

# ▶️ Run Development Server

```bash
python manage.py migrate
python manage.py runserver
```

Open in browser:

```txt
http://127.0.0.1:8000/
```

---

# 🚀 Deploy on Vercel

## Create `vercel.json`

```json
{
  "builds": [
    {
      "src": "biometric_project/wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "biometric_project/wsgi.py"
    }
  ]
}
```

> Replace `biometric_project` with your actual Django project folder name if different.

---

# 🛠 Static Files Configuration

Add this in `settings.py`:

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```

---

# 🔐 Environment Variables

For production deployment, configure:

```env
DEBUG=False
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=*
```

---

# 📋 Useful Commands

## Create Superuser

```bash
python manage.py createsuperuser
```

## Collect Static Files

```bash
python manage.py collectstatic
```

---

# 🧪 Common Error Fixes

## ❌ Error: No module named 'django'

### ✅ Solution

Make sure `requirements.txt` exists and contains:

```txt
Django>=5.0
```

Then redeploy the project on Vercel.

---

# 🧰 Tech Stack

- Python
- Django
- Vercel
- HTML/CSS/JavaScript

---

# 👩‍💻 Author

**Sreelatha Budda**

## GitHub Repository

https://github.com/buddasreelatha57/designing_secure_biometric

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
