# 🗣️ A2SL: Audio to Sign Language Converter

**A real-time accessibility tool that translates spoken language into Indian & American Sign Language (ISL/ASL) using Natural Language Processing.**

## 🚀 Overview
Bridging the communication gap for the Deaf and Hard of Hearing community. This application listens to live speech, processes the natural language, and instantly renders the corresponding sign language animations using a dictionary of over 2,000+ real human signs.

## ✨ Key Features
- **🎙️ Live Speech Recognition:** Uses the Web Speech API to capture audio in real-time.
- **🌍 Multilingual Support:** Supports English, Hindi, Tamil, Telugu, and other global languages using `googletrans`.
- **🧠 NLP Engine:** Intelligent parsing (NLTK) to remove stop words and lemmatize sentences for accurate signing.
- **🎥 High-Fidelity Assets:** Integrated with the **WLASL (Word-Level American Sign Language)** dataset for realistic human gestures.
- **⏯️ Playback Control:** Full Pause/Play/Stop functionality with a visual queue buffer.
- **🛡️ Enterprise Backend:** Powered by **PostgreSQL** for robust data management.

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3 (Dark Theme), JavaScript (ES6), Bootstrap 4.
- **Backend:** Python, Django 4.1.
- **Database:** PostgreSQL.
- **AI/ML:** NLTK (Natural Language Toolkit), Web Speech API.
- **Dataset:** WLASL (Video Assets).

## ⚙️ Installation Guide

### Prerequisites
- Python 3.8+
- PostgreSQL installed locally

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Audio_ToSignLanguage.git](https://github.com/YOUR_USERNAME/Audio_ToSignLanguage.git)
cd Audio_ToSignLanguage
 
### 2. Set up Virtual Environment
python -m venv urop
# Windows
urop\Scripts\activate
# Mac/Linux
source urop/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Database Setup
Open your PostgreSQL Shell (psql) or pgAdmin and run:

CREATE DATABASE a2sl_db;

### 5. Run Migrations & Server
python manage.py migrate
python manage.py runserver

Visit http://127.0.0.1:8000/animation/ to start the tool.

Contact
Dhaerya Khanna 📧 dhaeryakhanna1@gmail.com

"We would love to see the world as a better place—one where no voice goes unheard and no sign goes unseen."