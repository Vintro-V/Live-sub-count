import json
import urllib.request
#https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=Vintro&key=
a = input("hello please enter username: ")
key = "AIzaSyBvUUkjmIBL2JLDPFpOA6VCVVB0WBaEXCQ"
while True:
    username_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + a + "&key=" + key
    username_data = urllib.request.urlopen(username_url).read()
    username_subs = json.loads(username_data)["items"][0]["statistics"]["subscriberCount"]
    print(a + " has " +  "{:,d}".format(int(username_subs)))
