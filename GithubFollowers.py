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

onlyMe = following.difference(followers)
onlyThem =  followers.difference(following)
if(len(onlyMe)==0 and len(onlyThem)==0):
    print("No conflicts.")
elif len(onlyMe)>0:
    for r in onlyMe:
        print(r)
elif len(onlyThem)>0:
    for r in onlyThem:
        print(r)
