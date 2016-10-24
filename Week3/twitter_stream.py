#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "781528393582018564-TNkDGOD0haTwaDZYUuAtkXjMka7IHaE"
access_token_secret = "iQQ92rkwlKxf0gtEKNO7oeX0kbgUgYXAeE2fa3uzjKoOz"
consumer_key = "6CikPdBMsGnO4SPjYVR8XLfjk"
consumer_secret = "BbYEu8o6eTDz97XdskOjpsnJJZ5f6ahTQVnlFOndSu22M3kyEW"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)
        if status == 420:
            return False


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['#debate'])
