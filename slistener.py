from tweepy import StreamListener
import json, time, sys

class SListener(StreamListener):

    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.counter = 0
        self.fprefix = fprefix
        self.output  = open(fprefix + '.' + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')

    def on_data(self, data):

        if  'in_reply_to_status' in data:
            self.on_status(data)

    def on_status(self, status):
        self.output.write(status + "\n")

        self.counter += 1
        print ("Writing tweet number :" +self.counter)
        if self.counter >= 20000: ## Close the file if tweet count exceeds 20000
            self.output.close()
            self.counter = 0

        return True

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return True

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return
