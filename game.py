import pygame
from random import*
from sala import peixe

imagem_fundo=r"imagem/fundo do mar - Copia.webp"
imagem_peixe=r"imagem/peixe_amarelo.png"
imagem_alga=r"imagem/alga.png"
WIDTH = 700
HEIGHT = 400

pygame.init()


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
    window.blit(image, (0, 0))
    window.blit(pontuacao, (600, 10))
    window.blit(peixes.image,(peixes.coord_x-110/2,peixes.coord_y-70/2))
    
    pygame.display.update() 

pygame.quit()  
