# NLP_StopWordFromTextInput
This script tokenizes input text into sentences and words, removes English stop words, and displays the filtered tokens and removed stop words.

This Python script tokenizes user-entered text into sentences and words, then removes stop words from the word tokens, displaying both filtered and removed words.
Steps:
1. Library Setup: Downloads necessary NLTK data files (punkt for tokenization and stopwords for filtering).
2. Tokenization: Prompts the user to input text, then tokenizes the text into sentences and words using sent_tokenize and word_tokenize.
3. Stop Word Filtering: Defines English stop words and filters them out from the word tokens. Outputs both the filtered word tokens (excluding stop words) and the list of removed stop words.
Examples: For input text, the script outputs sentence tokens, word tokens, filtered tokens, and removed stop words for easy reference.
This code helps in basic text preprocessing tasks, useful for Natural Language Processing (NLP) applications.
