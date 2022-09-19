from fgwcg import Game
import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 60

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0, 0, 255)
BROWN = (190, 65, 0)

BG_COLOR = WHITE
GAME_CAPTION = "The Farmer, The Goat, The Wolf, and The Cabbage Game"
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, RED)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_CAPTION)


class Farmer(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/farmer.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 400)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Wolf(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/wolf.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Goat(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/goat.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 200)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Cabbage(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/cabbage.png")
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class RiverBank(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = (SCREEN_HEIGHT, SCREEN_WIDTH/2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class GUI(pygame.sprite.Sprite):

    def action(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
def main():
    P = Farmer()
    W = Wolf()
    G = Goat()
    C = Cabbage()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        P.action()
        screen.fill(BG_COLOR)
        P.draw(screen)
        W.draw(screen)
        G.draw(screen)
        C.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
