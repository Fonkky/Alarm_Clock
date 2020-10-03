import datetime
import os
from playsound import playsound

os.system('cls')
desiredH = int(input('What hour you want alarm to ring? '))
desiredM = int(input('What minute you want alarm to ring? '))
os.system('cls')
print('Alarm set. Desired time: ', desiredH, desiredM)

while True:
    if (desiredH == datetime.datetime.now().hour and 
        desiredM == datetime.datetime.now().minute):
            print('Wake up Neo')
            playsound('./alarm/LifeandDeath.mp3')
            break