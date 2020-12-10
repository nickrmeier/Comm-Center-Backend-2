import pymongo
from pymongo import MongoClient

from tweetweet import twitter_names, screen_name, home_results, twitter_friends

cluster = MongoClient(
    "mongodb+srv://commConUser:Fldrycleaning233@cluster0.03c5w.mongodb.net/commConDB?retryWrites=true&w=majority")
db = cluster["commConDB"]
collection = db["users"]

# post1 = {"_id": 3, "comm_username": "Nick",
#          "twitter_name": twitter_names.name, "twitter_screenname": screen_name, "home_tweets": home_results[0:4], "friends": twitter_friends}

post2 = {"_id": 5, "comm_username": "Noo-noo",
         "twitter_name": twitter_names.name, "twitter_screenname": screen_name, "home_tweets": home_results[0:4], "friends": twitter_friends}

collection.insert_one(post2)


# results = collection.find({"name": "Tim"})

# for result in results:
#     print(result)
