from ctypes import resize
from djitellopy import tello
import cv2
t = tello.Tello()
# 'connect' will take care of the IP adress and connection
t.connect()
print("The Battery is: " + t.get_battery() + "percent")

t.stream_on()

while True:
    img = t.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)