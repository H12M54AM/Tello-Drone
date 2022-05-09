"""
    The purpose of this file is to see placed landing and 
    takeoff pads the drones came with. It should take 
    off, then find the pads, then move towards it, then 
    land on the pad
"""

from djitellopy import tello
from time import sleep
from imageCapture import streamith
import getBattery

drone = tello.Tello()
drone.connect()
drone.takeoff()

# Battery chaecker
getBattery.baReminder()

# Streams video
drone.enable_mission_pads()
