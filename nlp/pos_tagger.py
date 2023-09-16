import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from text import TEXT
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

corpus = TEXT
tokenized_sents = sent_tokenize(corpus)

def pos_tagger(tokenized_sents):
    pos_tagged_words = []

    for sentence in tokenized_sents:
        # 여기에 코드를 작성하세요
        token_sen = word_tokenize(sentence)
        pos_tagged = pos_tag(token_sen)
        pos_tagged_words.extend(pos_tagged)
    return pos_tagged_words

# 테스트 코드
pos_tagger(tokenized_sents)