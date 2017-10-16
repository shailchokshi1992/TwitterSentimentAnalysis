import csv
import json
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient(object):

    def __init__(self):

        ACCESS_TOKEN = "804432391-zqbTqPwkZIsxEx1KNnAPuqbtZTOqfu1JjwCeS7bI"
        ACCESS_SECRET = "b25qi2axGm7ZyHciSKkCFyQIDkX0ZqK7Kpc05NCFt9dHv"
        CONSUMER_KEY = "hDxZ0AfEVJk67h0736TZ80u74"
        CONSUMER_SECRET = "klNr0qNg83FGtIfcfuy60WDp8nyLy6PqhslKumqQNfnuEAfpWK"

        try:
            self.auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
            self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            self.api = tweepy.API(self.auth)

        except:
            print("Error: Authentication Failed. Check for credentials")
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweets(self, query, count):

        tweets = []

        try:
            fetched_tweets = self.api.search(q=query)
            count = 0
            MAXLIMIT = 20000
            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text
                parsed_tweet['user'] = tweet.user.name
                # parsed_tweet['hashtag'] = []
                # for hashtag in tweet.entities['hashtags']:
                #     parsed_tweet['hashtag'].append(hashtag['text'])
                parsed_tweet['location'] = tweet.user.location
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                if tweet.retweet_count>0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                    else:
                        tweets.append(parsed_tweet)
                count += 1
                if count == MAXLIMIT:
                    break
                print (count)
            return tweets
        except tweepy.TweepError as e:
            print ("ERROR : " + str(e))

    def get_tweet_sentiment(self,tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

def main():
    api = TwitterClient()
    query = ['#TakeTheKnee', '#boycottnfl', '#TakeAKnee','#TakeAKneeNFL']
    tweets = api.get_tweets(query=query,count = 20000)
    print (tweets)
#    keys = tweets[0].keys()
#    with open('tweetlist.csv','wb') as outputfile:
#        json.dump(tweets, outputfile)
#        dict_writer.writeheader()
#        dict_writer.writerow([unicode(tweets).encode("utf-8") for tweets in row])
#    print ("File Created..")

if __name__ == "__main__":
    main()
