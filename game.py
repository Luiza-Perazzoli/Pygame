import pygame
from random import*

imagem_fundo=r"C:\Users\luiza\OneDrive\Imagens\fundo do mar.webp"
imagem_peixe=r"C:\Users\luiza\OneDrive\Imagens\peixe2.jpg"
imagem_alga=r"C:\Users\luiza\OneDrive\Imagens\alga.png"
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

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((173, 216, 230))
    window.blit(image, (10, 10))
    window.blit(pontuacao, (600, 10))

    pygame.display.update() 

pygame.quit()  