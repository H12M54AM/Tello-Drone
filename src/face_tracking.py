from ast import While
import cv2
import numpy as np
import getBattery as GB
from djitellopy import tello

# -----------------------
WIDTH = 320
HEIGHT = 240
START_COUNTER = 1
# 0 is when the drone will fly, 1 is not
# -----------------------

# Connection
drone = tello.Tello()
drone.connect()
drone.send_rc_control(0, 0, 0, 0)
# Left/Right, Forward/Backward, Up/Down, Yaw Left/Yaw Right
drone.set_speed(0)

# Streaming
drone.streamoff
drone.streamon
GB.baReminder()

while True:
    # Get image from drone
    frame_read = drone.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (WIDTH, HEIGHT))

    if START_COUNTER == 0:
        drone.takeoff()
        drone.send_rc_control(-50, 0, 0, 0)
        # Left/Right, Forward/Backward, Up/Down, Yaw Left/Yaw Right
        drone.rotate_clockwise(90)
        START_COUNTER = 1
        