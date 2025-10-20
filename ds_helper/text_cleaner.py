import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

class TextCleaner:
    """
    A utility class for cleaning and preprocessing text data.
    This handles unstructured data by removing noise.
    
    Features:
    - Remove punctuations.
    - Remove filler words (e.g., "uh", "um", "like").
    - Remove stopwords.
    - Lowercasing & lemmatization (optional).
    """

    def __init__(self, custom_filler_words=None):
        """
        Initializes the TextCleaner with necessary resources.
        """
        # Define the set of filler/junk words
        default_fillers = ["uh", "um", "like", "y'know", "ahem", "er"]
        
        if custom_filler_words:
            default_fillers.extend(custom_filler_words)
        
        self.filler_words = set(default_fillers)
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        # Create a translation table to quickly remove punctuation
        self.punc_remover = str.maketrans('', '', string.punctuation)

    def _remove_punctuation(self, text):
        """Removes all standard English punctuation from a string."""
        return text.translate(self.punc_remover)

    def _tokenize_and_clean(self, text):
        """Tokenizes text and removes stopwords and filler words."""
        
        
        tokens = word_tokenize(text.lower()) 
        
        
        cleaned_tokens = [
            word for word in tokens 
            if word not in self.stop_words and word not in self.filler_words and word.isalpha()
        ]
        return cleaned_tokens

    def clean_text(self, text, do_lemmatize=True):
        """
        The main method to clean a single string of text.

        :param text: The input string (unstructured text).
        :param do_lemmatize: Boolean flag to apply lemmatization.
        :return: A single string of cleaned, processed text.
        """
        if not isinstance(text, str) or not text:
            return ""

        
        text_no_punc = self._remove_punctuation(text)
        
        
        tokens = self._tokenize_and_clean(text_no_punc)
        
        
        if do_lemmatize:
            tokens = [self.lemmatizer.lemmatize(word) for word in tokens]

    
        return " ".join(tokens)



if __name__ == "__main__":
    
    # 1. Initialize the cleaner with some extra custom fillers
    cleaner = TextCleaner(custom_filler_words=['totally', 'sorta', 'like'])
    
    # 2. Example Messy Text
    messy_text = (
        "Um, the quick brown foxes are totally jumping over the lazy dog, y'know? "
        "Like, it's very important to clean 99% of this noisy data."
    )

    print("--- Text Preprocessing Utility ---")
    print(f"\nOriginal Text:\n'{messy_text}'")
    print("-" * 50)
    
    # 3. Clean and Lemmatize
    cleaned_output = cleaner.clean_text(messy_text, do_lemmatize=True)
    print("Cleaned & Lemmatized Output:")
    print(f"'{cleaned_output}'")
    
    # 4. Clean WITHOUT Lemmatization
    cleaned_no_lem = cleaner.clean_text(messy_text, do_lemmatize=False)
    print("-" * 50)
    print("Cleaned (No Lemmatization) Output:")
    print(f"'{cleaned_no_lem}'")

