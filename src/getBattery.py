"""
    The baRemider() funtion uses a while loop to 
    check what the current battery is and will 
    stop after it has made the check. This file
    is often used and the baReminder() function
    is often called to check the current capacity
    the drone is at.
"""

from djitellopy import tello

drone = tello.Tello()
drone.connect()
battery = drone.get_battery()

def baReminder():
    while battery == battery:
        print("Battery is at", battery, "%")
        if battery == 20:
            print("Low Battery...")
        if battery < 10 or battery == 10:
            print("Please charge me...")
        break

baReminder()