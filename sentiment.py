import json
import re
import pandas as pd
from textblob import TextBlob




# def get_tweet_sentiment(df):
#     positive = 0
#     negative = 0
#     neutral = 0
#     for line in df:
#         line = clean_text(line)
#         analysis = TextBlob(line)
#         if analysis.sentiment.polarity > 0:
#             #return 'positive'
#             positive +=1
#         elif analysis.sentiment.polarity == 0:
#             #return 'neutral'
#             neutral +=1
#         else:
#             negative +=1
#             #return 'negative'
#     return positive, negative

### Funciton to preprocess/ cleant tweets ###
def clean_text(txt):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", txt).split())

#### Function to get tweet sentimetn using textblob ####
def get_tweet_sentiment(df):
    sum_polarity=0.00
    sum_subjectivity=0.00
    for line in df:
        line = clean_text(line)
        analysis = TextBlob(line)
        sum_polarity += analysis.sentiment.polarity
        sum_subjectivity += analysis.sentiment.subjectivity
    return sum_polarity,sum_subjectivity



path = 'File1.20171016-124918.txt'

tweets_data = []
with open(path, "r") as tweets_file:
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue

tweets = pd.DataFrame(tweets_data)
print tweets
############## Get text and location for TWEETS #############
#tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
#tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['location'] = map(lambda tweet: tweet['user']['location'], tweets_data)


sentiment_df = pd.DataFrame([tweets['text'],tweets['location']]).T
print sentiment_df

#### Get 5 states with maximum tweets ####
tweets_by_location = sentiment_df['location'].value_counts()
print tweets_by_location[:10]
### Sample Output ####
# United States          55
# Montana, USA           30
# USA                    22
# Texas, USA             15
# Florida, USA           14
# OLD ENGLISH 800        13
# California, USA        12
# Michigan, USA           7
# South Carolina, USA     5
# New York, NY            5

for location in sentiment_df['location']:
    df = sentiment_df.loc[sentiment_df['location'] == location, 'text']
    print ("Polarity score and subjectivity score for %s is %s  " %(location, str(get_tweet_sentiment(df))))
### Sample Output ###

# Polarity score and subjectivity score for United States : (3.4, 10.33888888888889)
# Polarity score and subjectivity score for Montana, USA: (0.0, 0.0)
# Polarity score and subjectivity score for Texas,USA : (-0.10714285714285693, 4.502579365079365)
# Polarity score and subjectivity score for Florida, USA: (1.7333333333333334, 1.7666666666666668)
# Polarity score and subjectivity score for Califoria, USA: (1.0500000000000003, 4.233333333333333)
# Polarity score and subjectivity score for Delaware is (0.39999999999999997, 0.5000000000000001)
# Polarity score and subjectivity score for Los Angeles is (-0.275, 1.65)
# Polarity score and subjectivity score for pennsylvania is (0.34285714285714286, 0.6678571428571429)
# Polarity score and subjectivity score for California, USA is (1.0500000000000003, 4.233333333333333)
# Polarity score and subjectivity score for average anime enthusiast is (-0.4, 0.4)
# Polarity score and subjectivity score for United States is (3.4, 10.33888888888889)
# Polarity score and subjectivity score for Montana, USA is (0.0, 0.0)
# Polarity score and subjectivity score for Florida, USA is (1.7333333333333334, 1.7666666666666668)
# Polarity score and subjectivity score for Sacramento, CA is (0.26785714285714285, 0.43452380952380953)
# Polarity score and subjectivity score for Connecticut, USA is (0.0, 0.0)
# Polarity score and subjectivity score for Paradise😉 is (0.0, 0.03333333333333333)
# Polarity score and subjectivity score for None is (0.0, 0.0)
# Polarity score and subjectivity score for At Home in the Heartland is (0.0, 0.0)
# Polarity score and subjectivity score for None is (0.0, 0.0)
# Polarity score and subjectivity score for Illinois - the Blue part is (0.5, 0.5)
# Polarity score and subjectivity score for None is (0.0, 0.0)
# Polarity score and subjectivity score for None is (0.0, 0.0)
# Polarity score and subjectivity score for None is (0.0, 0.0)
# Polarity score and subjectivity score for Maryland, USA is (0.30000000000000004, 1.3)
# Polarity score and subjectivity score for Texas, USA is (-0.10714285714285693, 4.502579365079365)
# Polarity score and subjectivity score for None is (0.0, 0.0)
# Polarity score and subjectivity score for OLD ENGLISH 800 is (-0.09999999999999998, 2.65)
# Polarity score and subjectivity score for Atlanta, GA is (0.25, 0.25)
# Polarity score and subjectivity score for None is (0.0, 0.0)
# Polarity score and subjectivity score for Tucson, AZ is (0.0, 0.0)
# Polarity score and subjectivity score for Big Comfy Chair in Iowa. is (-0.2, 0.3)
# Polarity score and subjectivity score for PA is (0.5, 0.625)
# Polarity score and subjectivity score for Montana, USA is (0.0, 0.0)
# Polarity score and subjectivity score for United States is (3.4, 10.33888888888889)
# Polarity score and subjectivity score for None is (0.0, 0.0)
# Polarity score and subjectivity score for Barrie, Ontario, Canada is (-0.5, 0.5)
# Polarity score and subjectivity score for Rio Grande Valley, Tx is (0.5, 0.8888888888888888)
# Polarity score and subjectivity score for Southern by choice, USA is (0.5, 0.8888888888888888)
# Polarity score and subjectivity score for OLD ENGLISH 800 is (-0.09999999999999998, 2.65)
# Polarity score and subjectivity score for Paradise😉 is (0.0, 0.03333333333333333)

## Reference used##
#1) http://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
