## Tello-Drone

*This Repository will contain the source code for Tello which is the name of the drone I am going to use for educational purposes. I am working with Python and a few lirbraries to suit the Tello Drone and operate it correctly. I am also learning a little bit more of Python in the process to improve under a short time frame. I am currently using Visual Studio Code as my code editor and I want to mention that the tutorial video I have linked uses Pycharm, which is great too, but I am much more comfortable with Vscode. Plus the installations are not that different too. So I would say, go with what you are comfortable with because these just are tools. I can just get this done faster with vscode*

##### The modules needed to be installed are:
* djitellopy
* pygame
* cv2

The version of Python used is 3.7.6

Install normally if you use pip
```
    pip install djitellopy
    
    pip install pygame

    pip install cv2
```

For those who use Python3, use pip3
```
    pip3 install djitellopy

    pip3 install pygame

    pip3 install cv2
```

When making your files
```python
    from djitellopy import tello

    import pygame

    import cv2
```

##### Extra modulues used:
* time
* keyPressModule

```python
    from time import sleep

    import keyPressModule as kpm

    import manuveur

    from getBattery import baReminder
```

###### *Resources*
[Tello-Drones](https://www.ryzerobotics.com/tello
"Website for Drones") 

[Tutorial](https://www.youtube.com/watch?v=LmEcyQnfpDA
"Approx 3 hours long")

[DJI-Drone-Interface](https://github.com/damiafuentes/DJITelloPy
"GitHub Repository")

![Python Logo](https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png)
