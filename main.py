import os
from InstagramAPI import InstagramAPI

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

api = InstagramAPI(username, password)
api.login()

api.getSelfUsersFollowing()
response = api.LastJson
following = [user['pk'] for user in response['users']]

api.getSelfUserFollowers()
response = api.LastJson
followers = [user['pk'] for user in response['users']]

non_followers = list(set(following) - set(followers))

for user_id in non_followers:
    api.unfollow(user_id)

print("Finished unfollowing")