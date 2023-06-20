import sys
import pygame

from settings import SIZE, COLOR_BACKGROUND, COLOR_TRANSPARENT
from game_objects import Player, Background, Plasma_bullet, Asteroid, BadaBoom


def start_game():
    pygame.init()
    pygame.display.set_caption('TestGame')
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    # Group objects
    objects = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Game objects
    player = Player(bullets, clock)
    background = Background()

    objects.add(background)
    objects.add(player)

    active = True
    game_started = False

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        # Respoun asteroid
        Asteroid.respoun(asteroids, clock)

        if game_started:
            # Change state player
            objects.update()
            bullets.update()
            asteroids.update()
        elif pygame.key.get_pressed()[pygame.K_SPACE]:
            game_started = True

        # Collise
        pygame.sprite.groupcollide(bullets, asteroids, True, True)

        if pygame.sprite.spritecollide(player, asteroids, True):
            badaboom = BadaBoom(player.rect.midtop)
            badaboom.draw(screen)
            pygame.display.flip()
            pygame.time.delay(1000)
            active = False

        # Fill background
        screen.fill(COLOR_BACKGROUND)

        # Draw Background
        background.draw(screen)

        # Draw player
        player.draw(screen)

        # Draw bullet
        bullets.draw(screen)

        # Draw asteroid
        asteroids.draw(screen)

        # Show frame
        pygame.display.flip()

        # Delay game loop -- frame per second
        clock.tick(60)

    pygame.quit()
    sys.exit(0)


if __name__ == '__main__':
    start_game()
