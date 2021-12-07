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