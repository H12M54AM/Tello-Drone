from ctypes import resize
from djitellopy import tello
import cv2

drone = tello.Tello()
# 'connect' will take care of the IP adress and connection
drone.stream_on()

while True:
    img = drone.get_frame_read().frame()
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)