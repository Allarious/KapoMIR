from __future__ import unicode_literals
import hazm
import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

def persian_normalizer(text):
    hazm_normalizer = hazm.Normalizer()
    return hazm_normalizer.normalize(text)

def persian_tokenize(text):
    return hazm.word_tokenize(text)

def delete_persian_stop_words(list):
    stop_words = '،!?'
    output = []
    for token in list:
        if(token in stop_words):
            continue
        else:
            output.append(token)
    return output

def persian_stemmer(list):
    hazm_stemmer = hazm.Stemmer()
    output = []
    for token in list:
        output.append(hazm_stemmer.stem(token))
    return output

def persian_preprocess(text):
    for i in persian_stemmer(delete_persian_stop_words(persian_tokenize(persian_normalizer(text)))):
        print(i)
    
    
def english_normalizer(text):
    return text.lower()

def english_tokenize(text):
    return nltk.word_tokenize(text)

def delete_english_stop_words(list):
    stop_words = ',!?'
    output = []
    for token in list:
        if(token in stop_words):
            continue
        else:
            output.append(token)
    return output

def english_stemmer(list):
    output = []
    for token in list:
        output.append(ps.stem(token))
    return output

def english_preprocess(text):
    for i in english_stemmer(delete_english_stop_words(english_tokenize(english_normalizer(text)))):
        print(i)