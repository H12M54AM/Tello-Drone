from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
high = drone.get_height()


# This is an experiment
def gHeight():
    while high == high:
        print("Drone is", high, "cm above ground")
        break

def main():
    drone.takeoff()
    sleep(2)
    gHeight()
    drone.land()