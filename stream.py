import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
ACCESS_TOKEN = "804432391-zqbTqPwkZIsxEx1KNnAPuqbtZTOqfu1JjwCeS7bI"
ACCESS_SECRET = "b25qi2axGm7ZyHciSKkCFyQIDkX0ZqK7Kpc05NCFt9dHv"
CONSUMER_KEY = "hDxZ0AfEVJk67h0736TZ80u74"
CONSUMER_SECRET = "klNr0qNg83FGtIfcfuy60WDp8nyLy6PqhslKumqQNfnuEAfpWK"

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Parsing
        decoded = json.loads(data)
        #open a file to store the status objects
        file = open('stream.json', 'a')
        #write json to file
        json.dump(decoded,file,sort_keys = True,indent = 4)
        #show progress
        print "Writing tweets to file,CTRL+C to terminate the program"


        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    #Hashtag to stream
    stream.filter(track=["#love"])
