#Text Data Preprocessing Lib
import nltk
from nltk.stem import PortalStemmer
stemmer=PortalStemmer()
import json
import pickle
import numpy as np
words=[]
classes=[]
word_tags_list=[]
ignorewords=['?','!',',','.'," 's "," 'm "]

# function for appending stem words


train_data_file=open('intents.json').read()
intents=json.loads(train_data_file)
def get_stem_words(words,ignorewords):
    stem_words=[]
    for word in words:
        if word not in ignorewords:
            w=stemmer.stem(word.lower())
            stem_words.append(w)
    return stem_words   

for intent in intents['intents']:
    for pattern in intent['patterns']:
        pattern_word=nltk.word_tokenize(pattern)
        words.extend(pattern_word)
        # Add all words of patterns to list
        word_tags_list.append(pattern_word,intent['tag'])
    if intent['tag'] not in classes:
        classes.append(intent['tag'])
        stem_words=get_stem_words(words,ignorewords)
        # Add all tags to the classes list

print(stem_words)
print(word_tags_list[0])
print(classes)  

#Create word corpus for chatbot

