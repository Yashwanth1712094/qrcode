import datetime   
from playsound import playsound
import os
alarmHour=int(input("enter Hour: "))
alarmMin=int(input("enter Minute: "))


while True:
    if alarmHour==datetime.datetime.now().hour   and alarmMin==datetime.datetime.now().minute:
        print("playing...")
        playsound("alarm.mp3")
        break

    