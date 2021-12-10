from djitellopy import tello

drone = tello.Tello()
drone.connect()
battery = drone.get_battery()

# This is an experiment
def baReminder():
    while battery == battery:
        print("Battery is at", battery, "%")
        if battery < 10 or battery == 10:
            print("Please charge me...")
        if battery == 20:
            print("Low Battery...")
        break
baReminder()