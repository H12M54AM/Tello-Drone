# This code is directly from the provided repository in the 
# README file, from the module, djitellopy

import cv2
from djitellopy import Tello
import time

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
cv2.imwrite(f"{time.time()}.jpg", frame_read.frame)

tello.land()