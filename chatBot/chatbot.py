#CHATBOt
from datetime import datetime
import webbrowser
import os
import glob

helloIntent = ["hi","hello","hie","hey","hey buddy","wassup"]
byeIntent = ["bye","bie","tata","see you"]
dateIntent = ["show me the date","date","whats the date","date please"]
timeIntent = ["show me the time","time","whats the time","time please"]

chat=True
while chat == True:
    msg = input("Enter your message : ").lower()

    if msg in helloIntent:
        print("Hello Sir....")
    elif msg in byeIntent:
        print("Bye....Catch you later...")
        chat=False
        
    elif msg in dateIntent:
        datetime = datetime.now()
        print(datetime.strftime("%d-%m-%y,%a"))

            
    elif msg in timeIntent:
        datetime = datetime.now()
        print(datetime.strftime("%H-%M-%S,%p"))


    elif msg.startswith("open"):
        msg=msg.split()[-1]
        webbrowser.open(f"https://www.{msg}.com/")

    elif msg.startswith("play"):
        
        songList = glob.glob("*.mp3")
        print(">>>>>>>>> PlayList <<<<<<<<<<")
        for i in range(len(songList)):
            print(f"{i+1}. --> {songList[i]}")
        choice = int(input("enter music number you wana play : "))
        os.startfile(songList[choice-1])


    else:
        print("Sorry , I dont Understand...")
