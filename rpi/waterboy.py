#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# GPIO setup
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    # TODO: notify listeners here
    if GPIO.input(channel):
        print("Water detected!")
    else:
        print("No water detected!")


# Add event listener
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

# Listen indefinitely
while True:
    time.sleep(1)
