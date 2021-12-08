from djitellopy import tello
from modules import keyPressModule as kpm
import time  
from getBattery import baReminder 
import cv2

# This is the combination of both keyboardControl and imageCapture
# make the string in 'getKey' the selected key to use
kpm.init()
drone = tello.Tello()
sleep = time.sleep()
drone.connect()
baReminder()
drone.streamon
global img

def getKeyBoardInput():
    # lr is left & right
    # fb is front & back
    # ud is up & down
    # yv is yaw & velocity
    lr, fb, ud,  yv = 0, 0, 0, 0
    speed = 50

    if kpm.getKey("LEFT"): lr  = -speed 
    elif kpm.getKey("RIGHT"): lr  = speed 

    if kpm.getKey("UP"): fb  = speed 
    elif kpm.getKey("DOWN"): fb  = -speed

    if kpm.getKey("w"): ud  = speed
    elif kpm.getKey("s"): ud  = -speed

    if kpm.getKey("a"): yv  = speed
    elif kpm.getKey("d"): yv  = -speed

    if kpm.getKey("q"): drone.land()
    if kpm.getKey("t"): drone.takeoff()

    # screenshots img
    if kpm.getKey("c"): 
        cv2.iamwrite(f'imgs/{time.time()}.jpg',img)
        # Delay
        sleep(0.3)
        
    return [lr, fb, ud, yv]


while True:
    vals = getKeyBoardInput() 
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = drone.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)