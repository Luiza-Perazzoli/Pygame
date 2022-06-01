import pygame

from sala import HEIGHT, WIDTH

def tela_final(window):
    imagem_fundo=r"imagem/fundo do mar - Copia.webp"
    image = pygame.image.load(imagem_fundo).convert()
    font = pygame.font.SysFont(None, 48)
    text = font.render('VOCÊ PERDEU', True, (0, 0, 255))
    pygame.display.set_caption('flappy fish')
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        window.blit(image, (0,0))
        window.blit(text, (WIDTH/2, HEIGHT/2))

        pygame.display.update()  

