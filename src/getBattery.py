from djitellopy import tello

drone = tello.Tello()
drone.connect()
battery = drone.get_battery()

# Battery Reminder
def baReminder():
    if battery == 100:
        print("Battery at 100%")
        # 100%
    elif battery == 90:
        print("Battery is at 90%")
        # 90%
    elif battery == 80:
        print("Battery is at 80%")
        # 80%
    elif battery == 70:
        print("Battery is at 70%")
    elif battery == 60:
        print("Battery is at 60%:")
    elif battery == 50:
        print("Battery is at 50%")
    elif battery == 40:
        print("Battery at: less than 30%")
    elif battery == range(40, 30):
        print("Less than 30% Battery")
    elif battery == range(30, 20):
        print("Low Battery")
    elif battery < 10:
        print("Please Charge me...")
baReminder()

print(battery)
