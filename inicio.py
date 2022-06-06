import pygame

from sala import HEIGHT, WIDTH

def tela_inicial(window):
    imagem_fundo=r"imagem/fundo do mar - Copia.webp"
    #imagem_peixe_triste=r"imagem/peixe-triste.webp"

    image_1 = pygame.image.load(imagem_fundo).convert()
    #image_2 = pygame.image.load(imagem_peixe_triste).convert_alpha()
    #image_2 = pygame.transform.scale(image_2,(300,250))

    font = pygame.font.SysFont('Times', 48)
    text = font.render('VAMOS JOGAR FLAPPY FISH', True, (0, 0, 255))
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
        #window.blit(image_2, (WIDTH/2, HEIGHT/2))

        window.blit(text, (230, 200))

        pygame.display.update()  
