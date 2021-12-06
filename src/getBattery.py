from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery())