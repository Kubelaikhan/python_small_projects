import datetime
from playsound import playsound

alarmHour = int(input("Enterh hour: "))
alarmMin = int(input("Enter Minutes: "))
alarmAm = input("am/pm:")

if alarmAm=="pm":
    alarmHour+=12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        print("playing:..")
        playsound("spongebob.mp3")
        break
    # else:
