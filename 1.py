import tweepy

from tweepy import OAuthHandler

consumer_key = 'Jkpaxx4minqjC9LH2qKbqHZE6'
consumer_secret = 'AhRYe3jAYcgEq7G0bmhb1qoh2EXI082TgFL2IOKdj37mDBAhu1'
access_token = '839858792619732992-wo5isPogzXRM2z0XSLFVTp7sVRSTKnQ'
access_secret = 'ffFzy7CW2OscEev7qK8SvjWgeTnmEaDXkiUtzMKRZn2P3'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])

