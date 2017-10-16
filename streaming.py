from slistener import SListener
import time, tweepy, sys
from tweepy import OAuthHandler

ACCESS_TOKEN = "804432391-zqbTqPwkZIsxEx1KNnAPuqbtZTOqfu1JjwCeS7bI"
ACCESS_SECRET = "b25qi2axGm7ZyHciSKkCFyQIDkX0ZqK7Kpc05NCFt9dHv"
CONSUMER_KEY = "hDxZ0AfEVJk67h0736TZ80u74"
CONSUMER_SECRET = "klNr0qNg83FGtIfcfuy60WDp8nyLy6PqhslKumqQNfnuEAfpWK"
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

def main():
    track = ['#TakeAKnee', '#TakeAKneeNFL','#TakeTheKnee','#boycottnfl']

    listen = SListener(api, 'File1')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try:
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
