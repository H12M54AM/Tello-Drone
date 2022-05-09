"""
    A simple program where the drone will be grabbing
    the current height whether it is flying or not. 
    In combination with the function getHeight(), 
    the drone will do a simple flight route, testing
    if the getHeight function is working in main().
"""

from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
high = drone.get_height()


# This is an experiment
def getHeight():
    while high == high:
        print("Drone is", high, "cm above ground")
        break

def main():
    drone.takeoff()
    sleep(2)
    getHeight()
    drone.land()

main()