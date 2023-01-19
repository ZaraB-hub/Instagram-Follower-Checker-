import json

with open('followers.json') as json_file:
    followers_data = json.load(json_file)

with open('following.json') as json_file:
    following_data = json.load(json_file)


# my_followers_ids = []
# for follower in followers_data['users']:
#     my_followers_ids.append(follower['pk'])

my_followers_ids = [follower['pk'] for follower in followers_data['users']]
i_am_following_ids = [follower['pk'] for follower in following_data['users']]

# list of accounts that I am following but not followed back
not_following_back = list(set(i_am_following_ids) - set(my_followers_ids))

for user_id in not_following_back:
    user = next((u for u in following_data['users'] if u["pk"] == user_id), None)
    print(user["username"])
