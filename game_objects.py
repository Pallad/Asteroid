import pygame
import random
from settings import *

class Player(pygame.sprite.Sprite):
    max_speed = 2
    cooldown  = 240
    curr_tick = cooldown

    def __init__(self, bullets, clock):
        super(Player, self).__init__()
        self.image = pygame.image.load(r'assets\player.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.bullets = bullets
        self.clock = clock

    def update(self):
        self.curr_tick -= self.clock.get_time()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.centerx -= Player.max_speed
            if self.rect.centerx < self.rect.width/2:
                self.rect.centerx = self.rect.width/2

        elif keys[pygame.K_RIGHT]:
            self.rect.centerx += Player.max_speed
            if self.rect.centerx > WIDTH - self.rect.width/2:
                self.rect.centerx = WIDTH - self.rect.width/2

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.curr_tick <= 0:
            self.curr_tick = self.cooldown
            self.bullets.add(Plasma_bullet(self.rect.midtop))

        for bullet in list(self.bullets):
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.image = pygame.image.load(r'assets\space.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT

    def update(self):
        self.scroll()

    def scroll(self):
        self.rect.bottom += 1
        if self.rect.bottom >= self.rect.height + HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, screen):
        rectA = self.image.get_rect()
        rectA.bottom = self.rect.bottom - self.rect.height
        if rectA.bottom > 0:
            screen.blit(self.image, rectA)

        screen.blit(self.image, self.rect)

class Plasma_bullet(pygame.sprite.Sprite):
    speed = - 4

    def __init__(self, position):
        super(Plasma_bullet, self).__init__()
        self.image = pygame.image.load(r'assets\plasma_bullet.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    def update(self):
        self.rect.move_ip((0, self.speed))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Asteroid(pygame.sprite.Sprite):
    speed = 4
    cooldown  = 240
    curr_tick = cooldown

    def __init__(self):
        super(Asteroid, self).__init__()
        self.image = pygame.image.load(r'assets\asteroid{}.png'.format(random.randint(0, 1)))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, WIDTH), 0)

    def update(self):
        self.rect.move_ip((self.speed - 2*random.randint(0, self.speed), self.speed))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.originImage, self.originImage.get_rect())

    @staticmethod
    def respoun(asteroids, clock):
        Asteroid.curr_tick -= clock.get_time()
        if Asteroid.curr_tick <= 0:
            asteroids.add(Asteroid())
            Asteroid.curr_tick = Asteroid.cooldown
        else:
            for asteroid in list(asteroids):
                if asteroid.rect.top > HEIGHT:
                    asteroids.remove(asteroid)


class BadaBoom(pygame.sprite.Sprite):
    def __init__(self, position):
        super(BadaBoom, self).__init__()
        self.image = pygame.image.load(r'assets\boom.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = position

    def update(self):
        self.rect.move_ip((0, self.speed))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
