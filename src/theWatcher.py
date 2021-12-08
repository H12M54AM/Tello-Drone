from djitellopy import tello
from modules import keyPressModule as kpm
import time  
from getBattery import baReminder 
import cv2

# This is the combination of both keyboardControl and imageCapture
# make the string in 'getKey' the selected key to use
kpm.init()
drone = tello.Tello()
drone.connect()
baReminder()
drone.streamon()
global img

def getKeyBoardInput():
    # lr is left & right
    # fb is front & back
    # ud is up & down
    # yv is yaw & velocity
    lr, fb, ud,  yv = 0, 0, 0, 0
    speed = 40

    # Move Left
    if kpm.getKey("LEFT"): lr  = -speed 
    # Move Right
    elif kpm.getKey("RIGHT"): lr  = speed 

    # Forward
    if kpm.getKey("w"): fb  = speed 
    # Backward
    elif kpm.getKey("s"): fb  = -speed

    # Up 
    if kpm.getKey("UP"): ud  = speed
    # Down
    elif kpm.getKey("DOWN"): ud  = -speed

    # Turn Left
    if kpm.getKey("d"): yv  = speed
    # Turn Right
    elif kpm.getKey("a"): yv  = -speed

    # Takeoff
    if kpm.getKey("t"): drone.takeoff()
    # Land
    if kpm.getKey("l"): drone.land()

    # screenshots img
    if kpm.getKey("c"): 
        cv2.iamwrite(f'imgs/{time.time()}.jpg',img)
        # Delay
        time.sleep(0.3)
        
    return [lr, fb, ud, yv]


while True:
    vals = getKeyBoardInput() 
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (500, 350))
    cv2.imshow("Image", img)
    cv2.waitKey(1)