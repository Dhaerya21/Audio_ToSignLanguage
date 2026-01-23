from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles import finders
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from googletrans import Translator
import re  # <--- NEW: Regular Expressions for text cleaning

# --- HELPER FUNCTIONS ---

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    return wordnet.NOUN

def clean_text(text):
    """
    Expands contractions and removes special characters.
    I'm -> I am
    It's -> It is
    """
    text = text.lower()
    
    # Expand common English contractions
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    
    # Remove any remaining punctuation (keeping only letters and numbers)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    return text

# --- VIEWS ---

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

@login_required(login_url="login")
def animation_view(request):
    if request.method == 'POST':
        original_text = request.POST.get('sen')
        if not original_text:
            return render(request, 'animation.html')

        # 1. Translation Layer (Multilingual Support)
        try:
            translator = Translator()
            translation = translator.translate(original_text, dest='en')
            text_en = translation.text
        except Exception:
            text_en = original_text

        # 2. Text Cleaning (The Fix for "Nan nalam")
        # "I'm fine" becomes "i am fine"
        clean_en = clean_text(text_en)

        # 3. Tokenization & Tagging
        words = word_tokenize(clean_en)
        tagged = nltk.pos_tag(words)

        # 4. Glossing (English -> ASL Logic)
        lr = WordNetLemmatizer()
        gloss_words = []

        for w, tag in tagged:
            # Skip stopwords (including "am" which we just expanded from 'm)
            if w in ['a', 'an', 'the', 'is', 'am', 'are', 'was', 'were', 'to', 'do', 'does', 'did', 'done']:
                continue

            if w == 'i':
                gloss_words.append('me')
                continue	
            wn_tag = get_wordnet_pos(tag)
            lemma = lr.lemmatize(w, pos=wn_tag)
            gloss_words.append(lemma)

        # 5. Animation Matching
        final_words = []
        for w in gloss_words:
            path = w + ".mp4"
            if finders.find(path):
                final_words.append(w)
            else:
                for char in w:
                    final_words.append(char)

        return render(request, 'animation.html', {
            'words': final_words, 
            'text': original_text,
            'translated': clean_en 
        })
    else:
        return render(request, 'animation.html')

# ... (Keep existing auth views: signup_view, login_view, logout_view) ...
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('animation')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('animation')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("home")