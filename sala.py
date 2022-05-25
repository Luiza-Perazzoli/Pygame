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
        self.vel_x=vel_x
        self.vel_y=vel_y
        self.coord_x=WIDTH/2
        self.coord_y=HEIGHT/2
        self.pulando = False
        self.cont = 10
        self.image = pygame.image.load(imagem_peixe).convert_alpha()
        self.image = pygame.transform.scale(self.image, (110, 70))
    
    def pulo(self):
        if self.pulando:
            if self.cont >= -10:
                neg = 1
                if self.cont < 0:
                    neg = -1
                self.coord_y -= self.cont**2 * 0.1 * neg
                self.cont -= 1
            else:
                self.pulando = False
                self.cont = 10


