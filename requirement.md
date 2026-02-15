# Project Requirements: A2SL (Audio to Sign Language)

## 1. Purpose
A Django web application that converts live speech (and images) into sign language animation tokens using NLP and a video asset dictionary. It also provides user authentication and a simple website UI.

## 2. Scope
- Speech/text to sign animation tokens (ASL/ISL-style glossing).
- Image captioning to sign tokens (BLIP model).
- Web UI pages for home, about, contact, animation, image upload, login, signup.
- User authentication for protected routes.

## 3. Functional Requirements
### 3.1 Speech/Text to Sign
- Accept user text input (including text produced by client-side speech recognition).
- Translate input text to English (auto-detect source language).
- Clean and normalize text (lowercase, expand contractions, remove punctuation).
- Tokenize, POS-tag, lemmatize, and remove stop words.
- Convert pronoun "i" to "me" during glossing.
- Resolve each gloss token to a sign video asset if present; otherwise, fall back to per-character spelling.
- Return results as HTML render or JSON when requested via AJAX.

### 3.2 Image to Sign
- Accept a single image file upload.
- Generate a caption using a BLIP image-captioning model.
- Run the same normalization, tokenization, lemmatization, and asset-matching pipeline as speech/text.
- Return a JSON response containing tokens and cleaned text.

### 3.3 Authentication
- Provide user signup, login, and logout.
- Protect animation and image upload pages with login requirement.

### 3.4 Pages
- Home, About, Contact, Animation, Image Upload, Login, Signup.

## 4. Non-Functional Requirements
- Python 3.8+ runtime.
- Django 4.1.
- PostgreSQL database.
- NLTK corpora required for tokenization/lemmatization and POS tagging.
- BLIP model dependencies for image captioning (transformers, torch, pillow).
- Environment-based secret key configuration.

## 5. External Dependencies
From requirements.txt and code usage:
- Django
- psycopg2-binary (PostgreSQL connector)
- nltk
- deep-translator
- transformers
- torch
- pillow
- matplotlib, numpy, tqdm, regex, click, etc.

## 6. Data Requirements
- PostgreSQL database named `a2sl_db`.
- WLASL or similar sign video assets in the static assets directory.
- NLTK data in `nltk_data/` or downloaded at runtime.

## 7. Configuration Requirements
- `.env` file with `SECRET_KEY`.
- Database credentials configured in `A2SL/settings.py`.
  - Default: user `postgres`, password `Project@123`, host `localhost`, port `5432`.
- Static assets directory: `assets/`.

## 8. Deployment/Run Requirements
- Create and activate a virtual environment.
- Install dependencies from `requirements.txt`.
- Ensure PostgreSQL is running and the database exists.
- Run Django migrations and start the server.

## 9. Assumptions and Constraints
- Client uses Web Speech API for speech recognition (browser-dependent).
- Sign video assets are available and named using token `.mp4` files.
- If token assets do not exist, the system falls back to per-character spelling.

## 10. Out of Scope
- Real-time video synthesis or avatar generation.
- Production-grade security hardening and deployment configuration.
- Automated provisioning of PostgreSQL or NLTK datasets.
