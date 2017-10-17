import json
import re
import pandas as pd
from textblob import TextBlob

def clean_text(txt):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", txt).split())

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

#print len(tweets_data)

tweets = pd.DataFrame(tweets_data)

############## Get text and location for TWEETS #############
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['location'] = map(lambda tweet: tweet['user']['location'], tweets_data)


sentiment_df = pd.DataFrame([tweets['text'],tweets['location']]).T
#print sentiment_df

tweets_by_location = sentiment_df['location'].value_counts()
print tweets_by_location[:10]

df1= sentiment_df.loc[sentiment_df['location'] == 'United States', 'text']
print df1
print ("Polarity score and subjectivity score : " + str(get_tweet_sentiment(df1)))
df2= sentiment_df.loc[sentiment_df['location'] == 'Montana, USA', 'text']
print ("Polarity score and subjectivity score : " + str(get_tweet_sentiment(df2)))
df3= sentiment_df.loc[sentiment_df['location'] == 'Texas, USA', 'text']
print ("Polarity score and subjectivity score : " + str(get_tweet_sentiment(df3)))
df4= sentiment_df.loc[sentiment_df['location'] == 'Florida, USA', 'text']
print ("Polarity score and subjectivity score : " + str(get_tweet_sentiment(df4)))
df5= sentiment_df.loc[sentiment_df['location'] == 'California, USA', 'text']
print ("Polarity score and subjectivity score : " + str(get_tweet_sentiment(df5)))

# print positive
#
# print ("\n")
# print negative



#tweets['text'] = map(lambda tweet: tweets['text'], tweets_data)
# print (tweets['text'])

# tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
# tweets['location'] = map(lambda tweet: tweet.user.location, tweets_data)
# tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
