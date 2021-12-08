from djitellopy import tello
from getBattery import baReminder
from time import sleep
import datetime

curD = datetime.datetime.now()

# This file contains code that will always or most of the time, check the height 
# between the bottom of the drone to the ground. It is just a test and if it 
# works, then it will go into 'main.py'
drone = tello.Tello()
drone.connect()
baReminder()
drone.takeoff()
drone.move_forward(30)
sleep(1.5)
drone.rotate_clockwise(90)
drone.move_forward(40)
sleep(1.5)
print(drone.get_height())
drone.land()
baReminder()
# Formats the time to be readable to the user
print(curD.strftime('%c'))