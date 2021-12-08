from djitellopy import tello
from time import sleep 
from modules import baReminder


drone = tello.Tello()
drone.connect()

# Make a function that displays the height of the drone when it's off of the ground

def movement():
    drone.takeoff()
    drone.move_forward(20)
    sleep(1.5)

    drone.rotate_counter_clockwise(90)
    sleep(1.5)

    drone.move_forward(20)
    drone.rotate_clockwise(90)
    sleep(1.5)

    drone.land()

movement()
baReminder()