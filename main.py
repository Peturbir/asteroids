import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state 
def main():
    #Initialize Pygame
    pygame.init()

    #Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Game loop
    while True:
        #Log state
        log_state()
        #Check for player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Draw game
        screen.fill("black")
        #Refresh display
        pygame.display.flip()

if __name__ == "__main__":
    main()
