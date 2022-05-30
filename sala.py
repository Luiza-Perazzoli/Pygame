#from curses import window
from random import*
import pygame


imagem_fundo=r"imagem/fundo do mar - Copia.webp"
imagem_fundo2= r"imagem/fundo do mar2.webp"
imagem_peixe=r"imagem/peixe_amarelo.png"
imagem_alga=r"imagem\alga-png-real.png"
WIDTH = 700
HEIGHT = 400

class alga(pygame.sprite.Sprite):
    def __init__(self,WIDTH,HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.alturas_alga = [100,150,200,250,300]
        self.escala_y = self.alturas_alga[randint(0,4)]
        self.image = pygame.image.load(imagem_alga).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, self.escala_y))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = HEIGHT-self.escala_y
        self.speedx = -10
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.x = WIDTH
            self.alturas_alga = [100,150,200,250,300]
            self.escala_y = self.alturas_alga[randint(0,4)]
            self.rect.y = HEIGHT-self.escala_y
            self.image = pygame.transform.scale(self.image, (60, self.escala_y))
            self.speedx = -10
            self.speedy = 0


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
       

class fundo(pygame.sprite.Sprite):
    def __init__(self,WIDTH,HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagem_fundo).convert()
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedx = -10
        self.speedy = 0
        self.largura= WIDTH

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x + self.largura == 0:
            self.rect.x= self.largura
 
class fundo2(pygame.sprite.Sprite):
    def __init__(self,WIDTH,HEIGHT):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(imagem_fundo2).convert()
            self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
            self.rect = self.image.get_rect()
            self.rect.x = WIDTH
            self.rect.y = 0
            self.speedx = -10
            self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x + WIDTH == 0:
            self.rect.x = WIDTH