from djitellopy import tello
from getBattery import baReminder

t = tello.Tello()
t.connect()

# height = tello.get_height()

def fly():
    t.takeoff()
    baReminder()
    
fly()
