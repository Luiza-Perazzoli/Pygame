import pygame

from sala import HEIGHT, WIDTH

def tela_final(window):
    imagem_fundo=r"imagem/fundo do mar - Copia.webp"
    imagem_peixe_triste=r"imagem/peixe-triste.webp"

    image_1 = pygame.image.load(imagem_fundo).convert()
    image_2 = pygame.image.load(imagem_peixe_triste).convert_alpha()
    image_2 = pygame.transform.scale(image_2,(100,150))

    font = pygame.font.SysFont(None, 48)
    text = font.render('VOCÊ PERDEU', True, (0, 0, 255))
    pygame.display.set_caption('flappy fish')
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        window.blit(image_1, (0,0))
        window.blit(image_2, (WIDTH/2, HEIGHT/2))

        window.blit(text, (WIDTH/2, HEIGHT/2))

        pygame.display.update()  

