import requests 
a = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=weezer").json()
#outputs a dict with 2 keys "result Count" and "results". "results" has a list type has value pair with
#nested dicts where each is a element of seach result
b = a["results"] #cannot use multiple index
c = b[0]
print(c["trackName"]) #N capital

#or

for i in a["results"]:
    print(i["trackName"])