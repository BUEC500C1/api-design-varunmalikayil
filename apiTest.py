
import tweepy
 
consumer_key = 'WkF9CRxFhhBAkQAS3FewRH6KD'
consumer_secret = 'e5sAfbtPmEWPORlxKxjYH1QPfrRiXIaYMT8z60rqoxuxlByESp'
access_token = '834240241-S5AUNUxfbuDoQBtJc6XIqKhdRZq8Zhm0qacQKxGZ'
access_secret = 'QmxfcbWLTN77W1gtnOFMuLITA61jVwowgxXBYAgirUU9b'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
 
tweets = api.home_timeline()
print(tweets)
for tweet in tweets:
    print('{real_name} (@{name}) said {tweet}\n\n'.format(
        real_name=tweet.author.name, name=tweet.author.screen_name,
        tweet=tweet.text))