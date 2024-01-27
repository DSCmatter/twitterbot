import tweepy

#keys and tokens should be given by twitter developer account 

api_key = " "
api_secret = " "
bearer_token = " "
access_token = " "
access_token_secret = " "
client_id= " "
client_secret = ""
    
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth) 

client.create_tweet(text="Hi, I am a bot under you")
client.create_tweet(in_reply_to_tweet_id=, text="Fr") #id should be inserted here 
print("Tweet posted successfully")

# Path to the media file (image, video, etc.) you want to upload
# media_path = "E:/twitterbot/cool cat.jpg"  # Update with your media file path

# Upload media
# media = api.media_upload(media_path)

# Text of the tweet
# tweet_text = "Check out this awesome picture!"

# Post tweet with media
# api.update_status(status=tweet_text, media_ids=[media.media_id])



# client.retweet(1750093022451413034)

# person = client.get_user(username="OracleRadia").data.id

# for tweet in client.get_users_tweets(person).data:
#     print(tweet.text)