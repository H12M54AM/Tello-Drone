import pygame

def init():
    pygame.init()
    # Our window resolution
    win = pygame.display.set_mode((400, 400))


# Looks for keys pressed on keyboard
def getKey(key):
    ans = False
    for e in pygame.event.get(): pass
    input = pygame.key.get_pressed()
    # Formats to k_blank where blank is what key you want to be pressed
    myKey = getattr(pygame, 'k{}'.format(key))
    if input[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("Left Key Entered")
    if getKey("RIGHT"):
        print("Right Key Entered")
    if getKey("UP"):
        print("Up Key Entered")
    if getKey("Down"):
        print("Down Key Entered")

if __name__ == "__main__":
    init()
    while True:
        main()