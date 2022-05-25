import pygame
from random import*

imagem_fundo=r"imagem/fundo do mar - Copia.webp"
imagem_peixe=r"imagem/peixe_amarelo.png"
imagem_alga=r"imagem/alga.png"
WIDTH = 700
HEIGHT = 400

pygame.init()

class peixe:
    def __init__(self,vel_x,vel_y,WIDTH,HEIGHT):
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

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('flappy fish')

game = True

image = pygame.image.load(imagem_fundo).convert()
image = pygame.transform.scale(image, (WIDTH, HEIGHT)) 

font = pygame.font.SysFont("Times", 20)
pontuacao = font.render('pontos:', True, (255, 0, 127))

peixes=peixe(0,0,WIDTH,HEIGHT)
while game:
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    peixes.pulo()
    window.fill((173, 216, 230))
    window.blit(image, (10, 10))
    window.blit(pontuacao, (600, 10))
    window.blit(peixes.image,(peixes.coord_x,peixes.coord_y))
    
    pygame.display.update() 

pygame.quit()  
