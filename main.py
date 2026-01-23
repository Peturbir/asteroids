import sys
import pygame
from constants import *
from player import Player
from logger import log_state, log_event 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #Game loop
    while True:

        #Limit framerate
        dt = clock.tick(60) / 1000

        #Log state
        log_state()

        #Check for player input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
            
        #Draw game
        screen.fill("black")

        #Draw player
        for obj in drawable:
            obj.draw(screen)

        #Refresh display
        pygame.display.flip()

if __name__ == "__main__":
    main()
