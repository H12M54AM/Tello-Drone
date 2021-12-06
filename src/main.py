from djitellopy import tello
from time import sleep
from getBattery import baReminder

drone = tello.Tello()
drone.connect()
drone.takeoff()
drone.rotate_clockwise(90)
sleep(1)
drone.get_barometer()
drone.move_forward(40)
drone.rotate_clockwise(90)
drone.land()

# Function checks the battery status and prints out for every 10% decresed
baReminder()

