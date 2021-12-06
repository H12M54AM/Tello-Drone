from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.get_current_state()
drone.connect()
drone.takeoff()
drone.rotate_clockwise(90)
drone.move_forward(20)
drone.land()

