import pygame
from sala import HEIGHT, WIDTH

def tela_inicial(window):
    imagem_fundo=r"imagem/WhatsApp Image 2022-06-08 at 19.50.32.jpeg"

    image_1 = pygame.image.load(imagem_fundo).convert()
    image_1 = pygame.transform.scale(image_1,(WIDTH,HEIGHT))
    pygame.display.set_caption('flappy fish')
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = False
                if event.key == pygame.K_ESCAPE:
                    game = False
                    pygame.quit()

        window.blit(image_1, (0,0))

        pygame.display.update()  
