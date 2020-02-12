import requests
from PIL import ImageGrab
import time
from config import config
from keystrs import *

timetosleep=5
oldcommand=""
def analyse(command):
    global timetosleep,oldcommand
    try:
        if command=="r":
            command=oldcommand[:]
            oldcommand="r"
        else:oldcommand=command
        if command.startswith("tts"):
            timetosleep=int(command[4:])
        elif command.startswith("at"):
            num= int(command[3:])
            hold(key.alt)
            for i in range(num):
                press(key.tab)
            release(key.alt)
        else:
            exec(command)

    except:
        "Unexpected error. Retry"

while True:
    snapshot = ImageGrab.grab()
    save_path = "img.jpg"
    snapshot.save(save_path)
    with open('img.jpg',"rb") as f:
        plik=f.read()
    adress=f"http://{config.IP}:{str(config.PORT)}/inp"
    try:
        a=requests.post(adress,data={"img":str(str(plik))}).text
        if a!=oldcommand:analyse(a)
    except:
        print("Connection failed. Check your internet connection and if ip adress and port in config.py are correct. Retrying in 10s.")
        time.sleep(10)
    time.sleep(timetosleep)
