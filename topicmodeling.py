# a conventional alias
import pandas as pd
import json
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora, models
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

### Function to clean/preprocess tweet###

def clean_text(txt):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", txt).split())

path = 'File1.20171016-124918.txt'

tweets_data = []
with open(path, "r") as tweets_file:
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue

#print len(tweets_data)
#
tweets = pd.DataFrame(tweets_data)
tweet_doc = []
for tweet_txt in tweets['text']:
    try:
        tweet_doc.append(tweet_txt)
    except:
        continue

    tweet_clean_doc = []
df = pd.DataFrame([tweets['text']]).T

for line in df['text']:
    line = clean_text(line)
    tweet_clean_doc.append(line)

tweet_clean_doc = [str(tweet_clean_doc[x]) for x in range(len(tweet_clean_doc))]
print tweet_clean_doc
#for line in tweet_doc:


documents = tweet_clean_doc
no_features = 1000

# NMF is able to use tf-idf
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(documents)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()

no_topics=20
nmf = NMF(n_components=no_topics, random_state=1).fit(tfidf)

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic %d:" % (topic_idx)
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]])

no_top_words = 15
display_topics(nmf, tfidf_feature_names, no_top_words)


### References used ###
# 1) https://medium.com/@aneesha/topic-modeling-with-scikit-learn-e80d33668730
# 2) https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/
