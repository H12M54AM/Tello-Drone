"""
    Here, the main route for the general movement for this
    drone will be done here and all needed modules will 
    be imported here. 

"""
from time import sleep
from djitellopy import tello
from getBattery import baReminder

drone = tello.Tello()
drone.connect()

def main():
    drone.takeoff()
    drone.rotate_clockwise(90)
    sleep(1)

    print(drone.get_height())
    drone.rotate_clockwise(90)
    drone.land()

    # Function checks the battery status and prints out the exact percentage
    baReminder()

main()