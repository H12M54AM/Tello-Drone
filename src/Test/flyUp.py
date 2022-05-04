from djitellopy import tello
from getBattery import baReminder

t = tello.Tello()
t.connect()

# height = tello.get_height()

def fly():
    baReminder()
    t.takeoff()
    t.move_up(20)
    t.land()
    baReminder()
    
fly()
