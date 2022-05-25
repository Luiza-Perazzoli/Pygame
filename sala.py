from curses import window
from game import HEIGHT, WIDTH, imagem_peixe
import pygame
from random import*

class peixe:
    def __init__(self,vel_x,vel_y,WIDTH,HEIGHT):
        self.vel_x=vel_x
        self.vel_y=vel_y
        self.coord_x=WIDTH/2
        self.coord_y=HEIGHT/2
        self.pulando = False
        self.cont = 10
        self.image = pygame.image.load(imagem_peixe).convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
    
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

