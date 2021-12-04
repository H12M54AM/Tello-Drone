from djitellopy import tello
from time import sleep

t = tello.Tello()
# 'connect' will take care of the IP adress and connection
t.connect()
print("The Battery is: " + t.get_battery() + "percent")

t.takeoff()
# Left-Right Velocity, Forward-Backward Velocity, Up and Down Velocity, Yaw Velocity
t.send_rc_control(0, 20, 10, 0)
# Stays still
t.sleep(2)
t.send_rc_control(0, 0, 0, 0)
t.land() 