import pygame
from random import*
from sala import peixe, fundo, fundo2, alga, alga_invertida
def jogo(window):
    #define as imagens
    imagem_fundo=r"imagem/fundo do mar - Copia.webp"
    imagem_fundo2= r"imagem/fundo do mar2.webp"
    imagem_peixe=r"imagem/peixe_amarelo.png"
    imagem_alga=r"imagem\alga-png-real.png"
    imagem_alga_invertida= r"imagem/alga-png-real-invertida.png"
    #define o tamanho do fundo
    WIDTH = 800
    HEIGHT = 600
    #conta tempo do jogo
    clock = pygame.time.Clock()
    #vai atualizando a tela
    FPS = 30
    #grupo das algas
    all_algas = pygame.sprite.Group()
    #título do jogo
    pygame.display.set_caption('flappy fish')
    #inicia o jogo
    game = True
    #define variáveis iniciais
    vidas=3
    pontos=0
    #fonte do texto
    font = pygame.font.SysFont("Times", 20)

    #nomeia as classes com as devidas entradas da função
    peixes=peixe(0,0,WIDTH,HEIGHT)
    classe_fundo= fundo(WIDTH, HEIGHT)
    classe_fundo2= fundo2(WIDTH, HEIGHT)
    #faz as 4 algas da tela e as invertidas respectivas
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
    #define colisão
    colisao_anterior = 0
    #loop do jogo
    while game:
        #pontos e vidas na tela
        pontuacao = font.render('pontos:{}'.format(pontos), True, (255, 0, 127))
        vidas_texto = font.render('vidas:{}'.format(vidas), True, (255, 0, 127))
        #atualização da tela
        clock.tick(FPS)
        #faz update das classes pra que as posições atualizem
        classe_fundo.update()   
        classe_fundo2.update()
        peixes.update()
        all_algas.update()
        for event in pygame.event.get():
            #quando aperta space o peixe pula
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    peixes.pulo()
            #quando fecha a tela acaba o jogo
            if event.type == pygame.QUIT:
                game = False
                return "QUIT"
        #coloca as imagens na tela com as devidas posições
        window.fill((173, 216, 230))
        #quando tem rect é que atualiza a posição então ela varia
        window.blit(classe_fundo.image, (classe_fundo.rect.x, classe_fundo.rect.y))
        window.blit(classe_fundo2.image, (classe_fundo2.rect.x, classe_fundo2.rect.y))
        #coloca o grupo das algas na tela
        all_algas.draw(window)
        window.blit(pontuacao, (700, 10))
        window.blit(vidas_texto, (700, 30))
        window.blit(peixes.image,(peixes.rect.x,peixes.rect.y))
        #resposta quando a alga bate no peixe
        hits = pygame.sprite.spritecollide(peixes, all_algas, False, pygame.sprite.collide_mask)
        #tem esse +500 para que só considere um hit por alga e não pra cada pixel
        if hits != [] and pygame.time.get_ticks() > colisao_anterior + 500:
            #quando bate perde vidas e perde pontos
            colisao_anterior = pygame.time.get_ticks()
            vidas -= 1
            pontos-= 1
            hits = []
            # se vidas=0 acaba o jogo
            if vidas == 0:
                game = False
                return "QUIT"
        #se o peixe passa a alga (60 é o x da alga) ganha ponto
        if peixes.rect.left == alga1.rect.x + 60:
            pontos+= 1

        if peixes.rect.left == alga2.rect.x + 60:
            pontos+= 1

        if peixes.rect.left == alga3.rect.x + 60:
            pontos+= 1
        
        if peixes.rect.left == alga4.rect.x + 60:
            pontos+= 1
        #update do jogo funcionando
        pygame.display.update() 

