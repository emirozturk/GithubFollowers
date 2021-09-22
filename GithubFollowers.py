import requests
import json

pageCount = 3
followersJson = []
followingJson = []

for i in range(1,pageCount+1):
    followersJson += requests.get("https://api.github.com/users/emirozturk/followers?per_page=100&page="+str(i)).json()

for i in range(1,pageCount+1):
    followingJson += requests.get("https://api.github.com/users/emirozturk/following?per_page=100&page="+str(i)).json()

followers=set()
following=set()
for x in followersJson:
    followers.add(x["login"])
for x in followingJson:
    following.add(x["login"])

result = following.difference(followers)
if(len(result)==0):
    print("No conflicts.")
else:
    for r in result:
        print(r)