import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Download the NLTK data files (only the first time you run this program)
nltk.download('punkt')
nltk.download('stopwords')

if __name__ == "__main__":
    # Prompt the user to enter text instead of a file path
    text_input = input("Enter the text: ")
    
    # Tokenize sentences and words from the input text
    sentence_tokens = sent_tokenize(text_input)
    word_tokens = word_tokenize(text_input)
    
    # Define stop words in English
    stop_words = set(stopwords.words('english'))
    
    # Filter out stop words from the word tokens
    filtered_word_tokens = [word for word in word_tokens if word.lower() not in stop_words]
    removed_stop_words = [word for word in word_tokens if word.lower() in stop_words]
    
    # Output the results
    print("Sentence Tokens:\n", sentence_tokens)
    print("Word Tokens:\n", word_tokens)
    print("Filtered Word Tokens (without stop words):\n", filtered_word_tokens)
    print("Removed Stop Words:\n", removed_stop_words)

# OUTPUT
# Enter the text: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
# Sentence Tokens:
#  ['Lorem Ipsum is simply dummy text of the printing and typesetting industry.', "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.", 'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.', 'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.']
# Word Tokens:
#  ['Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'has', 'been', 'the', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', 'the', '1500s', ',', 'when', 'an', 'unknown', 'printer', 'took', 'a', 'galley', 'of', 'type', 'and', 'scrambled', 'it', 'to', 'make', 'a', 'type', 'specimen', 'book', '.', 'It', 'has', 'survived', 'not', 'only', 'five', 'centuries', ',', 'but', 'also', 'the', 'leap', 'into', 'electronic', 'typesetting', ',', 'remaining', 'essentially', 'unchanged', '.', 'It', 'was', 'popularised', 'in', 'the', '1960s', 'with', 'the', 'release', 'of', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages', ',', 'and', 'more', 'recently', 'with', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'of', 'Lorem', 'Ipsum', '.']
# Filtered Word Tokens (without stop words):
#  ['Lorem', 'Ipsum', 'simply', 'dummy', 'text', 'printing', 'typesetting', 'industry', '.', 'Lorem', 'Ipsum', 'industry', "'s", 'standard', 'dummy', 'text', 'ever', 'since', '1500s', ',', 'unknown', 'printer', 'took', 'galley', 'type', 'scrambled', 'make', 'type', 'specimen', 'book', '.', 'survived', 'five', 'centuries', ',', 'also', 'leap', 'electronic', 'typesetting', ',', 'remaining', 'essentially', 'unchanged', '.', 'popularised', '1960s', 'release', 'Letraset', 'sheets', 'containing', 'Lorem', 'Ipsum', 'passages', ',', 'recently', 'desktop', 'publishing', 'software', 'like', 'Aldus', 'PageMaker', 'including', 'versions', 'Lorem', 'Ipsum', '.']
# Removed Stop Words:
#  ['is', 'of', 'the', 'and', 'has', 'been', 'the', 'the', 'when', 'an', 'a', 'of', 'and', 'it', 'to', 'a', 'It', 'has', 'not', 'only', 'but', 'the', 'into', 'It', 'was', 'in', 'the', 'with', 'the', 'of', 'and', 'more', 'with', 'of']