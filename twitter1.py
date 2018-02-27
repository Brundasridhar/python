#twitter
import tweepy
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)
def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "gYn8waBv6PlDZAIkQSQ3M6Vuk",
    "consumer_secret"     : "41a7Rpm89QLEeEQn1zMMDJISgoMOQeXNCAxzCGn0UDQwe2asJl",
    "access_token"        : "3690426372-p2NyukpM9i9IlEGiLz6pGdlycAp6rzHPdXjW9t0",
    "access_token_secret" : "zZjC75eVbTKVfBPvLieeXo0jibxZGkNFIkHgQ08SSW3nR" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

