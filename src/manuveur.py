from djitellopy import tello
from time import sleep

# Plan:
# - Takeoff
# - Move Forward
# - Rotate counter-clockwise 90˚
# - Move Forward
# - Rotate clockwise 90˚
# - Land

drone = tello.Tello()

def connnection():
    drone.connect()
    print("The Battery is: " + drone.get_battery() + "percent")

# Make a function that displays the height of the drone when it's off of the ground
def heightDisplay():
    while drone.takeoff == True:
        print(drone.get_height())

def movement():
    drone.takeoff()
    drone.move_forward(20)
    drone.sleep()

    drone.rotate_counter_clockwise(90)
    drone.sleep()

    drone.move_forward(20)
    drone.rotate_clockwise(90)
    drone.sleep()

    drone.land()