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


class StdOutListener(StreamListener):
    ''' handles Data received from stream '''
    #count = 0
    def on_status(self, status):
        try:
            # parsed_tweet = {}
            # parsed_tweet['text'] = status.text
            # parsed_tweet['user'] = status.user.name
            # parsed_tweet['location'] = status.user.location

            decoded = json.loads(status)
            file = open('tweet.json','a')
            json.dump(decoded,file,sort_keys= True, indent=4)
            print("Wrting tweets:")

            # parsed_tweet['sentiment'] = get_tweet_sentiment(status)
    #        print ('Tweet text: '+ status.text)
    #        for hashtag in status.entities['hashtags']:
    #            print (hashtag['text'])

            # with open('tweetlist.csv','wb') as outfile:
            #     json.dumps(data,outfile)
            #tweets.extend(parsed_tweet)
            #print parsed_tweet
            #count += 1
            # with open('tweetlist.csv','a') as f:
            #     header = ['text','user','location']
            #     dict_writer.writerow(header)
            #     dict_writer.writerow(parsed_tweet)
            #print ("%s tweets written" % str(count))
            # with open('tweet.json','a') as f:
            #     f.write(parsed_tweet)
            #     return True
        except BaseException as e:
            print("Error on data %s" %str(e))

        return True

    def on_error(self, status_code):
        print ("Got an error with status_code:" + str(status_code))
        return True

    def on_timeout(self):
        print("timout---")
        return true

    def get_tweet_sentiment(self,status):
        analysis = TextBlob(status)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    #api = tweepy.API(auth)


    stream = Stream(auth,listener)
    stream.filter(track = ['#TakeTheKnee', '#boycottnfl', '#TakeAKnee','#TakeAKneeNFL'])
