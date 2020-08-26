import tweepy
import twitter_credentials
consumer_key = twitter_credentials.CONSUMER_KEY
consumer_secret = twitter_credentials.CONSUMER_SECRET
access_token = twitter_credentials.ACCESS_TOKEN
access_token_secret = twitter_credentials.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
new = []
for tweet in tweepy.Cursor(api.search,q="corona",count=50,
                           lang="en",
                           since="2020-08-21").items():
    new_d = {}
    print (tweet.created_at, tweet.retweet_count)

    new_d['screen_name'] = tweet.user.screen_name
    new_d['retweet_count'] = tweet.retweet_count
    with open("retweets.json",'a') as tf:
        tf.write(str(new_d)+",\n")
