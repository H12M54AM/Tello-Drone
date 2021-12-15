from djitellopy import tello

drone = tello.Tello()
drone.connect()
battery = drone.get_battery()

def baReminder():
    while battery == battery:
        print("Battery is at", battery, "%")
        if battery == 20:
            print("Low Battery...")
        if battery < 10 or battery == 10:
            print("Please charge me...")
        break
baReminder()