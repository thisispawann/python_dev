'''
Tokenization: A fundamental strp in NLP involves converting out text into smaller units through a process
              known as tokenization
'''
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
sentences = "The red jacket's clearly seen in a huge crowd. And the person wears from his own product."
tokenized_sentences = word_tokenize(sentences)
print(tokenized_sentences)