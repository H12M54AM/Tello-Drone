from djitellopy import tello
from getBattery import baReminder
from time import sleep

drone = tello.Tello()
drone.connect()

baReminder()
drone.takeoff()
drone.move_forward(30)
drone.rotate_clockwise(90)
drone.move_forward(30)
drone.get_barometer()
drone.land()
baReminder()