import json

with open('following.json') as file:
    following_json = json.load(file)

with open('followers.json') as file:
    followers_json = json.load(file)

people_not_following = []
for following in following_json["relationships_following"]:
    people_not_following.append(following["string_list_data"][0]["value"])

for follower in followers_json["relationships_followers"]:
    follower = follower["string_list_data"][0]["value"]
    if follower in people_not_following:
        people_not_following.remove(follower)

print("LIST OF PEOPLE WHO UNFOLLOWED ME:")
for user in people_not_following:
    print("- " + user)