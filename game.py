import pygame
from random import*
from sala import peixe

imagem_fundo=r"imagem/fundo do mar - Copia.webp"
imagem_peixe=r"imagem/peixe_amarelo.png"
imagem_alga=r"imagem/alga.png"
WIDTH = 700
HEIGHT = 400

pygame.init()
clock = pygame.time.Clock()
FPS = 30

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('flappy fish')

game = True

image = pygame.image.load(imagem_fundo).convert()
image = pygame.transform.scale(image, (WIDTH, HEIGHT)) 

font = pygame.font.SysFont("Times", 20)
pontuacao = font.render('pontos:', True, (255, 0, 127))

peixes=peixe(0,0,WIDTH,HEIGHT)
while game:
    clock.tick(FPS)
    peixes.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                peixes.pulo()
        if event.type == pygame.QUIT:
            game = False

    window.fill((173, 216, 230))
    window.blit(image, (0, 0))
    window.blit(pontuacao, (600, 10))
    window.blit(peixes.image,(peixes.rect.x-110/2,peixes.rect.y-70/2))
    
    pygame.display.update() 

pygame.quit()  
