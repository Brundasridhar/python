#sensor
from gpiozero import MotionSensor
import time
import os
import tweepy
pir=MotionSensor(4)
time.sleep(3)
if pir.motion_detected:

    print("Motion Detected")
else:
    print("no motion")

os.system("fswebcam  -F 3 --fps 20  -r 1200*800 /home/pi/desktop/csea2.jpg")
print("picture taken")

consumer_key= 'vxKlX4Wart7NHF3nRp2q23tSv'
consumer_secret= '9nf3zvLUAjYl368jJkHzUk5gkQ09wKzJ0oM9uSw64lMTQbUsLX'
access_token= '967251530196930560-1mfzpVeRilrRWUgRWenXjdLiDOMt82C'
access_token_secret= 'PSEACgq1qzdLIKVUeHG4JbMxi7QRMFkg11FCQnilDAavI'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)
b=1
a=0
while a<=2:
    img="/home/pi/Desktop/csea2.jpg"
    cmd="fswebcam -r 1280x720 -S 3 --jpeg 100 "+img
    os.system(cmd)
    print("pic taken")
    api.update_with_media(img, status="lol")
    print("wait")
    time.sleep(3)
    a+=1
    b+=1
    print("done")
