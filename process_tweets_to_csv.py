import pandas as pd
import json
tweets_data = []

tweets_file = open("tweet_data_1.txt", "r")

for line in tweets_file:

    try:

        tweet = json.loads(line)

        tweets_data.append(tweet)

    except:

        continue


##getting the parts we want into a data fram 

tweets = pd.DataFrame()

text = []
place = []
lang = []
location = []
geo_enabled = []
coordinates = []
for tweet in tweets_data:
    text_to_join = tweet['text']
    place_to_join = tweet['place']
    lang_to_join = tweet['lang']
    loc_to_join = tweet['user']['location']
    geo_to_join = tweet['user']['geo_enabled']
    coord_to_join = tweet ['coordinates']
    text.append(text_to_join)
    place.append(place_to_join)
    lang.append(lang_to_join)
    location.append(loc_to_join)
    geo_enabled.append(geo_to_join)
    coordinates.append(coord_to_join)
    

tweets['place'] = place
tweets['text'] = text

tweets['lang'] = lang
tweets['location']= location
tweets['geo'] = geo_enabled
tweets['coord'] = coordinates

tweets.to_csv("tweet_output_1.csv")