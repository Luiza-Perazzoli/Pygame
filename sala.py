#from curses import window
from random import*
import pygame

imagem_fundo=r"imagem/fundo do mar - Copia.webp"
imagem_peixe=r"imagem/peixe_amarelo.png"
imagem_alga=r"imagem/alga.png"
WIDTH = 700
HEIGHT = 400

class peixe(pygame.sprite.Sprite):
    def __init__(self,vel_x,vel_y,WIDTH,HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(imagem_peixe).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT/2
        self.speedx = 0
        self.speedy = 0
        self.count = 2

    def update(self):
        self.speedy += self.count
        self.rect.y += self.speedy

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.y < 40:
            self.rect.y = 40
    
    def pulo(self):
        self.speedy = -20