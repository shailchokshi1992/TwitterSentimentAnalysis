from slistener import SListener
import time, tweepy, sys
from tweepy import OAuthHandler

### CREDENTIALS TO E OBTAINED FROM http://apps.twitter.com ###########
### Steps to be followed as per references https://bdthemes.com/support/knowledge-base/generate-api-key-consumer-token-access-key-twitter-oauth/ ########

ACCESS_TOKEN = "************************************************"
ACCESS_SECRET = "***********************************************"
CONSUMER_KEY = "********************"
CONSUMER_SECRET = "********************************************"


auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

## Tweepy Stream API usinf StreamListener to download tweets ########

def main():
    listen = SListener(api, 'FILE2')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try:
        ### Track tweets for foloowing hastags ###
        stream.filter(track = ['#TakeAKnee', '#TakeAKneeNFL','#TakeTheKnee','#boycottnfl'])
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()

# '''
# References :
# 1) http://adilmoujahid.com/posts/2014/07/twitter-analytics/
# '''
