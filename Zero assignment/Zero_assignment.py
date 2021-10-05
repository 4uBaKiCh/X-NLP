f = open('Text.txt', "r", encoding="utf-8")
text = f.read()
f.close
text = text.lower()
import string
spec_chars = string.punctuation + '\n\xa0«»\t1234567890'
text = "".join([ch for ch in text if ch not in spec_chars])
from nltk import word_tokenize
text_tokens = word_tokenize(text)
import nltk
text = nltk.Text(text_tokens)
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
from wordcloud import WordCloud
import matplotlib.pyplot as plt
text_raw = " ".join(text)
wordcloud = WordCloud(stopwords = russian_stopwords).generate(text_raw)
wordcloud.to_file('result.png')
