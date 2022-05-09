"""
    swarm.py allows or should allow direct connection 
    to any avaliable drone that is pre-configuired to
    be used. You can code in this file to make the 
    drones do whatever you want in sync or not in 
    sync. 

    baReminder() is called to check the battery in all
    of the connected drones. 
"""

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
