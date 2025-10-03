import nltk
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

import string
import re
from typing import List, Optional

try:
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
except ImportError:
    stopwords = type('MockStopwords', (object,), {'words': lambda x: set()})
    WordNetLemmatizer = type('MockLemmatizer', (object,), {'__init__': lambda x: None, 'lemmatize': lambda x, y=None: x})
except LookupError:
    stopwords = type('MockStopwords', (object,), {'words': lambda x: set()})
    WordNetLemmatizer = type('MockLemmatizer', (object,), {'__init__': lambda x: None, 'lemmatize': lambda x, y=None: x})


class TextPreprocessor:
    
    def __init__(self, custom_filler_words: Optional[List[str]] = None):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

        default_fillers = {"uh", "um", "like", "you know", "ahem", "er", "ah", "hmm", "gonna", "wanna", "sorta", "kinda"}
        self.filler_words = default_fillers
        
        if custom_filler_words:
            self.filler_words.update(set(w.lower() for w in custom_filler_words))


    def _remove_punctuation(self, text: str) -> str:
        return text.translate(str.maketrans('', '', string.punctuation))

    
    def _lemmatize_and_lowercase(self, text: str) -> str:
        tokens = text.split()
        lemmatized_tokens = [self.lemmatizer.lemmatize(token.lower()) for token in tokens]
        return " ".join(lemmatized_tokens)


    def _filter_tokens(self, text: str) -> str:
        tokens = text.split()
        
        filtered_tokens = [
            token for token in tokens
            if token not in self.filler_words and token not in self.stop_words
        ]
        
        return " ".join(filtered_tokens)


    def clean_text(self, text: str, do_lemmatize: bool = True) -> str:
        if not text or not isinstance(text, str):
            return ""

        text = self._remove_punctuation(text)

        if do_lemmatize:
            text = self._lemmatize_and_lowercase(text)
        else:
            text = text.lower() 

        text = self._filter_tokens(text)
        
        text = re.sub(r'\s+', ' ', text).strip()

        return text

# --- Example Usage ---
if __name__ == '__main__':
    cleaner = TextPreprocessor(custom_filler_words=['totally'])
    raw_text = "Um, the students totally went for a really better idea, like, to build a new library! They were running fast. I'm gonna help."
    
    cleaned_lem = cleaner.clean_text(raw_text, do_lemmatize=True)
    
    print(cleaned_lem)