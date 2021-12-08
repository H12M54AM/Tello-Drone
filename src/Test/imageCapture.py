from djitellopy import tello
import cv2

# This file is used for the eyes of the drone. Some things might be missing but
# this should work

drone = tello.Tello()
# 'connect' will take care of the IP adress and connection
drone.connect()
drone.streamon()
def streamith():
    while True:
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (500, 350))
        cv2.imshow("Image", img)
        cv2.waitKey(1)

streamith()