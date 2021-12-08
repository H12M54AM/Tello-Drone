from time import sleep
from djitellopy import tello
from getBattery import baReminder
import datetime
from Test.imageCapture import streamith

# the absolute main file for the main activity
curD = datetime.datetime.now()
drone = tello.Tello()

drone.connect()
drone.takeoff()
drone.rotate_clockwise(90)
sleep(1)

print(drone.get_height())
drone.move_forward(40)
drone.rotate_clockwise(90)
drone.land()
print(curD)

# Function checks the battery status and prints out the exact percentage
baReminder()


