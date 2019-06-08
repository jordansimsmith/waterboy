#!/usr/bin/python3
import os
import time
import RPi.GPIO as GPIO
from dotenv import load_dotenv
from listeners.email import EmailListener

# read .env file
load_dotenv()

# GPIO setup
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# list of registered listeners
# notify(event) will be called on each listener
listeners = []

# register email listener
username = os.environ['EMAIL_USERNAME']
password = os.environ['EMAIL_PASSWORD']
destination = os.environ['EMAIL_DESTINATION']
email_listener = EmailListener(username, password, destination)
listeners.append(email_listener)


def callback(channel):

    water = not GPIO.input(channel)
    if water:
        print('Water detected.')
    else:
        print('No water detected.')

    # structure event
    event = {'water': water}

    # notify listeners
    for l in listeners:
        try:
            l.notify(event)
        except Exception as e:
            print(e)


# Add event listener
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=1000)
GPIO.add_event_callback(channel, callback)

# Listen indefinitely
print("Listening on GPIO {} for changes.".format(channel))
while True:
    time.sleep(1)
