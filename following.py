import tweepy

## See here for example : https://www.digitalocean.com/community/tutorials/how-to-authenticate-a-python-application-with-twitter-using-tweepy-on-ubuntu-14-04

CONSUMER_KEY = raw_input('Enter CONSUMER_KEY: ')
CONSUMER_SECRET = raw_input('Enter CONSUMER_SECRET: ')
ACCESS_TOKEN = raw_input('Enter ACCESS_TOKEN: ')
ACCESS_TOKEN_SECRET = raw_input('Enter ACCESS_TOKEN_SECRET: ')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

user_id = 'ddelmoli' #raw_input('Enter the user_id: ')
list_id = 'wit-women-in-tech' #raw_input('Enter the list_id: ')

for member in api.list_members(owner_screen_name=username, slug=list_id):
    api.create_friendship(member.screen_name)
