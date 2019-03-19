from tkinter import *
import json
import urllib.request
#Please don't pretent you made this!
key = "AIzaSyBvUUkjmIBL2JLDPFpOA6VCVVB0WBaEXCQ"
a = input("hello please enter username: ")
root = Tk()
root.title("SubCount")
root.geometry("225x50")
lab = Label()
username = Label(text="Username: " + a)
username.pack()
def task():
    username_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + a + "&key=" + key
    username_data = urllib.request.urlopen(username_url).read()
    username_subs = json.loads(username_data)["items"][0]["statistics"]["subscriberCount"]
    print("{:,d}".format(int(username_subs)))
    lab.pack()
    lab.config(text="SubCount: " + "(" +"{:,d}".format(int(username_subs)) + ")")
    root.after(1000, task) 
root.after(1000, task)
root.mainloop()
