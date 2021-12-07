from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
high = drone.get_height()

drone.takeoff()
sleep(2)

# This is an experiment
def gHeight():
    while high == high:
        print("Drone is", high, "cm above ground")
        break
gHeight()

drone.land()