# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mir3rdbEyZEWX3NUx4vjEIWOdDNDkoBr
"""

import nltk
from nltk.tokenize import word_tokenize
nltk.download('all')

text ='hello, simple sample text'
tokens = word_tokenize(text)
print('tokens:', tokens)

text = 'hello, abFFjs'
lowercase_text = text.lower()
print('lowercase text:', lowercase_text)

uppercase_text = text.upper()
print('uppercase text:', uppercase_text)

import string
import re
text = 'hellooo!!!!,  heyyy!!! how??? why?'
cleaned_text = re.sub(r'[^\w\s]', '', text)
print('cleaned text:', cleaned_text)

from nltk.corpus import stopwords
text = 'hellooo!!!!,  heyyy!!! how??? why?.hellooo!!!!,  heyyy!!! how??? why?'
text = 'hellooo!!!!,  heyyy!!! whereeeee??? why?'
text = 'hellooo!!!!,  heyyy!!! hiiii??? why?'
words = text.split()
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
filtered_text = ' '.join(filtered_words)
print('filtered text:', filtered_text)

from nltk.stem import PorterStemmer
words = ['running', 'better', 'run', 'runs', 'ran']
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print('stemmed words:', stemmed_words)

c = [1,5]
g = [43,67,88,90]
k = 6
j= g+c
h= k*c
print(j)
print(h)

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
      for j in range