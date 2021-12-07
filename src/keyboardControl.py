from modules import keyPressModule as kpm
# make the string in 'getKey' the selected key to use
kpm.init()

while True:
    print(kpm.getKey("s"))
