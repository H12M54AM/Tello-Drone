from djitellopy import tello
from time import sleep

t = tello.Tello()
# 'connect' will take care of the IP adress and connection
t.connect()
print("The Battery is: f{t.get_battery()}")