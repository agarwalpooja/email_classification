import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re

# reding csv file
mail = pd.read_csv("mail1.csv")
# shape of file
print(mail.shape)
# removing empty valued records
mail=mail.dropna()


# nlp aplication begins
# tokenize and stopwords
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

stop_words = set(stopwords.words('english'))

mail['tokenized_sents'] = mail.apply(lambda row: word_tokenize(row['subject']), axis=1)
mail['sents_length'] = mail.apply(lambda row: len(row['tokenized_sents']), axis=1)
filtered_sentence = [w for w in mail['tokenized_sents'] if not w in stop_words]

filtered_sentence = []

for w in mail['tokenized_sent']:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence)

print(mail.head())
