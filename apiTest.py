
import tweepy
from google.cloud import vision
import wget

 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# image_uri = 'gs://cloud-samples-data/vision/using_curl/shanghai.jpeg'

# client = vision.ImageAnnotatorClient()
# image = vision.types.Image()
# image.source.image_uri = image_uri

# response = client.label_detection(image=image)

# print('Labels (and confidence score):')
# print('=' * 79)
# for label in response.label_annotations:
#     print(f'{label.description} ({label.score*100.:.2f}%)')
 
api = tweepy.API(auth)
 
tweets = api.home_timeline()
for tweet in tweets:
    print('{real_name} (@{name}) said {tweet}\n\n'.format(
        real_name=tweet.author.name, name=tweet.author.screen_name,
        tweet=tweet.text))

# media_files = set()
# for status in tweets:
#     media = status.entities.get('media', [])
#     if(len(media) > 0):
#         media_files.add(media[0]['media_surl'])

# for media_file in media_files:
#     wget.download(media_file)