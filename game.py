import pygame
from random import*
from sala import peixe, fundo, fundo2

imagem_fundo=r"imagem/fundo do mar - Copia.webp"
imagem_fundo2= r"imagem/fundo do mar2.webp"
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

font = pygame.font.SysFont("Times", 20)
pontuacao = font.render('pontos:', True, (255, 0, 127))

peixes=peixe(0,0,WIDTH,HEIGHT)
classe_fundo= fundo(WIDTH, HEIGHT)
classe_fundo2= fundo2(WIDTH, HEIGHT)

while game:
    clock.tick(FPS)
    classe_fundo.update()
    classe_fundo2.update()
    peixes.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                peixes.pulo()
        if event.type == pygame.QUIT:
            game = False

    window.fill((173, 216, 230))
    window.blit(classe_fundo.image, (classe_fundo.rect.x, classe_fundo.rect.y))
    window.blit(classe_fundo2.image, (classe_fundo2.rect.x, classe_fundo2.rect.y))
    window.blit(pontuacao, (600, 10))
    window.blit(peixes.image,(peixes.rect.x-110/2,peixes.rect.y-70/2))
    
    pygame.display.update() 

pygame.quit()  
