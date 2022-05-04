"""
This program gets the height of the drone while it is
in the air, output the current height and land with
the battery reminder checking the current battery.
"""

from djitellopy import tello
from time import sleep
from getBattery import baReminder

drone = tello.Tello()
drone.connect()
height = drone.get_height()

drone.takeoff()
drone.move_forward(40)

# Displays the height between the bottom of the drone to the ground
print(height, "cm")
sleep(1)

drone.move_back(40)

# Displays the height between the bottom of the drone to the ground
print(height, "cm")
sleep(1)

drone.land()
baReminder()