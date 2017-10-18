import tweepy
import json
import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
# Authentication details. To  obtain these visit dev.twitter.com
ACCESS_TOKEN = "804432391-zqbTqPwkZIsxEx1KNnAPuqbtZTOqfu1JjwCeS7bI"
ACCESS_SECRET = "b25qi2axGm7ZyHciSKkCFyQIDkX0ZqK7Kpc05NCFt9dHv"
CONSUMER_KEY = "lFqoWFDZmVWg21NXO8Qer93J4"
CONSUMER_SECRET = "jR91Sz66ENAhGyyyuGVSI87S9PfaexGRUc1J3HOvbAOfX7ZPdo"

# This is the listener, resposible for receiving data


auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#TakeAKnee', '#TakeAKneeNFL','#TakeTheKnee','#boycottnfl'])
