import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    print GPIO.input(21)
    if(GPIO.input(21) == False):
        os.system("sudo shutdown -h now")
        break
    time.sleep(1)
