from djitellopy import TelloSwarm
import getBattery
from time import sleep

emergent = TelloSwarm.fromIps([
    "192.168.10.1"
])

emergent.connect()

emergent.sync()

emergent.takeoff()
sleep(1)
emergent.land()

for i in emergent:
    getBattery.baReminder()
