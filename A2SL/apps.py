from django.apps import AppConfig
import nltk
import os

class A2SlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'A2SL'

    def ready(self):
        # Create a directory for nltk_data if it doesn't exist
        nltk_path = os.path.join(os.getcwd(), 'nltk_data')
        if not os.path.exists(nltk_path):
            os.makedirs(nltk_path)
        
        # Tell nltk to look in this directory
        nltk.data.path.append(nltk_path)

        # Download the necessary packages
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', download_dir=nltk_path)
            
        try:
            nltk.data.find('taggers/averaged_perceptron_tagger')
        except LookupError:
            nltk.download('averaged_perceptron_tagger', download_dir=nltk_path)

        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet', download_dir=nltk_path)
            
        try:
            nltk.data.find('corpora/omw-1.4')
        except LookupError:
            nltk.download('omw-1.4', download_dir=nltk_path)