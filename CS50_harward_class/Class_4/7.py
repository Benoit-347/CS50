#API -> application proggraming interface
#3rd party services used to talk to while writing code, they mostly live on the internet
#how it happens is we write a program that pretends to be a browser that interacts with the 
# 3rd party API on a server and downloads some data that you can incorporate

#how to do this in py? has a module called requests module, helps make web requests, internet requests
#when we use API the downloaded info (txt) is often in json (JavaScript Object Notation) format, used to communicate with other computers
import requests 
#syn: request.get(<link>)
#fecthes the data, .json() uses json format to print content
print(requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer").json())
