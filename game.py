import pygame
from random import*
from sala import peixe, fundo, fundo2, alga, alga_invertida
def jogo(window):
    imagem_fundo=r"imagem/fundo do mar - Copia.webp"
    imagem_fundo2= r"imagem/fundo do mar2.webp"
    imagem_peixe=r"imagem/peixe_amarelo.png"
    imagem_alga=r"imagem\alga-png-real.png"
    imagem_alga_invertida= r"imagem/alga-png-real-invertida.png"

    WIDTH = 800
    HEIGHT = 600
    
    clock = pygame.time.Clock()
    FPS = 30

    all_algas = pygame.sprite.Group()

    pygame.display.set_caption('flappy fish')

    game = True

    vidas=3
    pontos=0
    gap = 0

    font = pygame.font.SysFont("Times", 20)


    peixes=peixe(0,0,WIDTH,HEIGHT)
    classe_fundo= fundo(WIDTH, HEIGHT)
    classe_fundo2= fundo2(WIDTH, HEIGHT)
    alga1= alga(WIDTH, HEIGHT, 0)
    all_algas.add(alga1)
    alga2= alga(WIDTH, HEIGHT, 1)
    all_algas.add(alga2)
    alga3= alga(WIDTH, HEIGHT, 2)
    all_algas.add(alga3)
    alga4= alga(WIDTH, HEIGHT, 3)
    all_algas.add(alga4)
    algas_invertidas1= alga_invertida(WIDTH, HEIGHT, alga1)
    all_algas.add(algas_invertidas1)
    algas_invertidas2= alga_invertida(WIDTH, HEIGHT, alga2)
    all_algas.add(algas_invertidas2)
    algas_invertidas3= alga_invertida(WIDTH, HEIGHT, alga3)
    all_algas.add(algas_invertidas3)
    algas_invertidas4= alga_invertida(WIDTH, HEIGHT, alga4)
    all_algas.add(algas_invertidas4)
    colisao_anterior = 0

    while game:
        pontuacao = font.render('pontos:{}'.format(pontos), True, (255, 0, 127))
        vidas_texto = font.render('vidas:{}'.format(vidas), True, (255, 0, 127))
        clock.tick(FPS)
        classe_fundo.update()   
        classe_fundo2.update()
        peixes.update()
        all_algas.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    peixes.pulo()
            if event.type == pygame.QUIT:
                game = False
                return "QUIT"

        window.fill((173, 216, 230))
        window.blit(classe_fundo.image, (classe_fundo.rect.x, classe_fundo.rect.y))
        window.blit(classe_fundo2.image, (classe_fundo2.rect.x, classe_fundo2.rect.y))
        all_algas.draw(window)
        window.blit(pontuacao, (700, 10))
        window.blit(vidas_texto, (700, 30))
        window.blit(peixes.image,(peixes.rect.x,peixes.rect.y))
        hits = pygame.sprite.spritecollide(peixes, all_algas, False, pygame.sprite.collide_mask)
        if hits != [] and pygame.time.get_ticks() > colisao_anterior + 500:
            colisao_anterior = pygame.time.get_ticks()
            vidas -= 1
            pontos-= 1
            hits = []
            if vidas == 0:
                game = False
                return "QUIT"
        if peixes.rect.left == alga1.rect.x + 60:
            pontos+= 1

        if peixes.rect.left == alga2.rect.x + 60:
            pontos+= 1

        if peixes.rect.left == alga3.rect.x + 60:
            pontos+= 1
        
        if peixes.rect.left == alga4.rect.x + 60:
            pontos+= 1

        pygame.display.update() 

