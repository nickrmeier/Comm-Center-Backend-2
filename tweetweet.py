import tweepy
import time

auth = tweepy.OAuthHandler('IBrNk0I2vEkKrWnZwHQGCG4DT',
                           '9tdArBoqFqh8OXVPXFeE25C432CpepILSQCBSnS3W1mBCUNGFo')
auth.set_access_token('1330989669228580864-e3Xy6IdMqRtd0UsvMKbYIHjV3uKL2T',
                      '99GV4vpHByEhc6bAxdAeRpptI6qvL8LHcsnHf4DYBwZb7')

api = tweepy.API(auth)


# twitter name
twitter_names = api.me()

# screenname
screen_name = twitter_names.screen_name

# gathers tweets on home page
public_tweets = api.home_timeline()

home_results = []

for tweet in public_tweets:
    home_results.append(tweet.text)


# show friendships

twitter_friends = []

for friend in api.friends(screen_name):
    twitter_friends.append(friend.screen_name)


# def limit_handler(cursor):
#     try:
#         while True:
#             yield cursor.next()
#     except tweepy.RateLimitError:
#         time.sleep(1000)


# generous bot - will follow specific followers
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Nick Meier':
#         follower.follow()


# like a tweet based on a keyword
# search_string = 'hello'
# numberOfTweets = 5

# for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
#     try:
#         tweet.favorite()
#         print('I liked that tweet')
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break
