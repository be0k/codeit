import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from preprocess import pos_tagger
from preprocess import penn_to_wn
from text import TEXT
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

corpus = TEXT
tokenized_sents = sent_tokenize(corpus)
pos_tagged_words = pos_tagger(tokenized_sents)

lemmatizer = WordNetLemmatizer()

# 표제어 추출 함수
def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB

def words_lemmatizer(pos_tagged_words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []

    for word, tag in pos_tagged_words:
        wn_tag = penn_to_wn(tag)

        if wn_tag in (wn.NOUN, wn.ADJ, wn.ADV, wn.VERB):
            lemmatized_words.append(lemmatizer.lemmatize(word, wn_tag))
        else:
            lemmatized_words.append(word)
    return lemmatized_words

words_lemmatizer(pos_tagged_words)