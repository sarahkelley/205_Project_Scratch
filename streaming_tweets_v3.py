from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd

#child of stream listener to print tweets.
class CreateStream(StreamListener):

    def on_data(self, data):
        print(data)
    def on_error(self, status):
        print(status)

auth = OAuthHandler('RwTQwNA1pbgNCV6jskt6VjDCW', 'BmDpJ6OoO4PJeVg00cRf3V0bdcr4qFSsLKVcVOTSHF5IJ2jk4y' )
auth.set_access_token('754931937211318272-Misc0ZncTo89mlfmmW92O3C21uiy3zg', 'TyllOgTMrOXuLCYW2L4kC9ZNlDEXu8XAoCOC34GMr0sPT')
stream = Stream(auth, CreateStream())

x = stream.filter(track=['asthma'])
