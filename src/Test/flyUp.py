"""
    This program is a test to utilize the motors 
    capabilities and allows the user to visually
    check the current state of the propellers in
    case of any impacts or potential failure 
    that may occur in the future.
"""

from djitellopy import tello
from getBattery import baReminder

t = tello.Tello()
t.connect()

# height = tello.get_height()

def fly():
    baReminder()
    t.takeoff()
    t.move_up(20)
    t.land()
    baReminder()
    
fly()
