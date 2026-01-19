import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state 
def main():
    #Initialize Pygame
    pygame.init()

    #Clock time
    clock = pygame.time.Clock()
    dt = 0

    #Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Game loop
    while True:

        #Log state
        log_state()

        #Check for player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)
            
        #Draw game
        screen.fill("black")

        #Draw player
        player.draw(screen)

        #Refresh display
        pygame.display.flip()

        #Limit framerate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
