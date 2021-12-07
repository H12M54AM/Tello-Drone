from djitellopy import tello

drone = tello.Tello()
drone.connect()
battery = drone.get_battery()

# This is an experiment
def baReminder():
    while battery == battery:
        print("Battery is at", battery, "%")
        break
baReminder()