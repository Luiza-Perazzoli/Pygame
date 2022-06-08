import pygame

from sala import HEIGHT, WIDTH
#função do fim 
def tela_final(window):
    #imagem do peixe triste 
    imagem_fundo=r"imagem/game-over.jpg"
    #define fonte
    font = pygame.font.SysFont("Times", 20)
    #imagem do fundo
    image_1 = pygame.image.load(imagem_fundo).convert()
    image_1 = pygame.transform.scale(image_1,(WIDTH,HEIGHT))
    #texto
    texto = font.render('clique RETURNE para voltar pra tela inicial', True, (0, 0, 125))
    
    pygame.display.set_caption('flappy fish')
    game = True
    #quando aperta returne pra ir pra tela de jogar de novo
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = False
                if event.key == pygame.K_ESCAPE:
                    game = False
                    pygame.quit()
        #coloca as imagens e texto
        window.blit(image_1, (0,0))
        window.blit(texto, (60, 400))

        pygame.display.update()  

