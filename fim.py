import pygame

from sala import HEIGHT, WIDTH

def tela_final(window):
    imagem_fundo=r"imagem/game-over.jpg"

    image_1 = pygame.image.load(imagem_fundo).convert()
    image_1 = pygame.transform.scale(image_1,(WIDTH,HEIGHT))

    pygame.display.set_caption('flappy fish')
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = False
                if event.key == pygame.K_ESCAPE:
                    game = False
                    pygame.quit()

        window.blit(image_1, (0,0))

        pygame.display.update()  

