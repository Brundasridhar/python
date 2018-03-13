import os
import time
import tweepy
consumer_key= 'gYn8waBv6PlDZAIkQSQ3M6Vuk'
consumer_secret= '41a7Rpm89QLEeEQn1zMMDJISgoMOQeXNCAxzCGn0UDQwe2asJl'
access_token= '3690426372-p2NyukpM9i9IlEGiLz6pGdlycAp6rzHPdXjW9t0'
access_token_secret= 'zZjC75eVbTKVfBPvLieeXo0jibxZGkNFIkHgQ08SSW3nR'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)
b=1
a=0
while a<=2:
    img="/home/cs2017a113/Desktop/img"+str(b)+".jpg"
    cmd="fswebcam -r 1024x720 -S 3 --jpeg 100 "+img
    os.system(cmd)
    print("pic taken")
    api.update_with_media(img, status="lol")
    print("wait")
    time.sleep(3)
    a+=1
    b+=1
    print("done")
