import json
import urllib.request
import time

# SCRIPT BY VINTRO SUBSCRIBE TO VINTRO AND PEWDIEPIE https://www.youtube.com/channel/UCvibZyT7CfNU8i10kc9_5Aw

key = "AIzaSyBvUUkjmIBL2JLDPFpOA6VCVVB0WBaEXCQ"
while True:
    PewDiePie_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key=" + key
    T_Series_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=TSeries&key=" + key

    PewDiePie_data = urllib.request.urlopen(PewDiePie_url).read()
    T_Series_data = urllib.request.urlopen(T_Series_url).read()

    PewDiePie_subs = json.loads(PewDiePie_data)["items"][0]["statistics"]["subscriberCount"]
    T_Series_subs = json.loads(T_Series_data)["items"][0]["statistics"]["subscriberCount"]

    print("---------------------------------------------------------------")
    print ("PewDiePie" + " has " + "{:,d}".format(int(PewDiePie_subs)) + " subs")
    print("---------------------------------------------------------------")
    print ("T-Series" + " has " + "{:,d}".format(int(T_Series_subs)) + " subs")
    print("---------------------------------------------------------------")
    difference = int(PewDiePie_subs) - int(T_Series_subs)
    print("the difference is {:,d}".format(int(difference)))
    print("---------------------------------------------------------------")
    print ("""                                                                             
                                                                                         
                                                                                         
                                                                                             
                                                                                         
                                                                                         
                                                                                         
                                                                                             
                                                                                             
                                                                                             
                                                                                             
                                                                                         
                                                                                             
                                                                                         
                                                                                         
                                                                                         
                                                                                             
                                                                                             

                                                                                             

    """)
