import requests

pageCount = 5
followersJson = []
followingJson = []
userName = "emirozturk"
for i in range(1,pageCount+1):
    followersJson += requests.get(f"https://api.github.com/users/{userName}/followers?per_page=100&page="+str(i)).json()

for i in range(1,pageCount+1):
    followingJson += requests.get(f"https://api.github.com/users/{userName}/following?per_page=100&page="+str(i)).json()

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
if len(onlyMe)>0:
    print("Non-followers that i am following")
    for r in onlyMe:
        print(r)
if len(onlyThem)>0:
    print("Followers that i am not following")
    for r in onlyThem:
        print(r)
