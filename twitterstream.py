import tweepy
import json
import csv
from textblob import TextBlob
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener



ACCESS_TOKEN = "804432391-zqbTqPwkZIsxEx1KNnAPuqbtZTOqfu1JjwCeS7bI"
ACCESS_SECRET = "b25qi2axGm7ZyHciSKkCFyQIDkX0ZqK7Kpc05NCFt9dHv"
CONSUMER_KEY = "hDxZ0AfEVJk67h0736TZ80u74"
CONSUMER_SECRET = "klNr0qNg83FGtIfcfuy60WDp8nyLy6PqhslKumqQNfnuEAfpWK"

count = 0
class StdOutListener(StreamListener):
    ''' handles Data received from stream '''

    def on_status(self, status):
        try:
            with open('tweet.json','a') as f:
                f.write(str(status))
                print ("Writing tweets, Press CTRL+C to stop.! ")
                return True

        except BaseException as e:
            print ("Error on data ; %s" %str(e))
        return True

    def on_error(self, status_code):
        print ("Got an error with status_code:" + str(status_code))
        return True

    def on_timeout(self):
        print("timout---")
        return true

    # def get_tweet_sentiment(self,status):
    #     analysis = TextBlob(status)
    #     if analysis.sentiment.polarity > 0:
    #         return 'positive'
    #     elif analysis.sentiment.polarity == 0:
    #         return 'neutral'
    #     else:
    #         return 'negative'

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    #api = tweepy.API(auth)


    stream = Stream(auth,listener)
    stream.filter(track = ['#TakeTheKnee', '#boycottnfl', '#TakeAKnee','#TakeAKneeNFL'])
