# Healthy Programmer:
# Working Time is 9 a.m. - 5 p.m.
# Water - water.wav(3.5 litres)-Drank-log
#Eye-eyes.mp3-every 30 min- Eyedone -log
# Physical activity - physical .mp3 every-45 min-ExDone-log

from pygame import mixer
from datetime import datetime
from time import time,sleep

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        a=input()
        if a.lower()==stopper.lower():
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    #musiconloop("water.mp3","stop")
    init_water=time() # give number i.e. in seconds
    init_eyes=time()
    init_physical_exercise=time()
    water_secs=1800
    eyes_secs=2100
    phyex_secs=2700


    while True:
        now=datetime.now()
        current_hour=now.hour
        if 9<=current_hour <=17:

           if time()-init_water>water_secs:
               print("Water drinking time. Enter 'drank' to stop the alarm.")
               musiconloop("water.mp3", "drank")
               init_water = time()
               log_now("Drank water at")

           if time() - init_eyes > eyes_secs:
                print("Eyes exercise time. Enter 'Eyedone' to stop the alarm.")
                musiconloop("eyes.mp3", "Eyedone")
                init_eyes = time()
                log_now("Eyes exercises are done at")

           if time() - init_physical_exercise > phyex_secs:
               print("Physical exercise time. Enter 'Exdone' to stop the alarm.")
               musiconloop("eyes.mp3", "Exdone")
               init_physical_exercise = time()
               log_now("Physical exercises are done at")

        else:
            print("Outside working hours (9 a.m. to 5 p.m.).Waiting...")
            sleep(60)