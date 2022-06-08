#from curses import window
from random import*
import pygame

#link das imagens
imagem_fundo=r"imagem/fundo do mar - Copia.webp"
imagem_fundo2= r"imagem/fundo do mar2.webp"
imagem_peixe=r"imagem/peixe_amarelo.png"
imagem_alga=r"imagem/alga-png-real.png"
imagem_alga_invertida= r"imagem/alga-png-real-invertida.png"
#nomeia altura e largura da tela
WIDTH = 800
HEIGHT = 600
#classe das algas
class alga(pygame.sprite.Sprite):
    #consições iniciais da alga
    def __init__(self,WIDTH,HEIGHT,numero):
        pygame.sprite.Sprite.__init__(self)
        #soretia tamanho da alga em escala y, para ter vários tamanhos diferentes
        self.alturas_alga = [150,100,250,200]
        self.random = randint(0,3)
        self.escala_y = self.alturas_alga[self.random]
        #faz load da imagem do png e define seu tamanho
        self.image = pygame.image.load(imagem_alga).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, self.escala_y))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #multiplica pelo número que é a posição da alga, para que tenha mais de uma por tela
        self.rect.x = WIDTH + 200*numero
        #para a alga ficar no chão
        self.rect.y = HEIGHT-self.escala_y+30
        self.speedx = -10
        self.speedy = 0

    def update(self):
        #movimenta a alga pra trás e quando chega no final da tela volta pro começo
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.x = WIDTH
            self.escala_y = self.alturas_alga[self.random]
            self.random = randint(0,3)
            self.rect.y = HEIGHT-self.escala_y+30
            self.image = pygame.transform.scale(self.image, (60, self.escala_y))
            self.speedx = -10
            self.speedy = 0
#classe da laga de cima 
class alga_invertida(pygame.sprite.Sprite):
    #consições iniciais
    def __init__(self,WIDTH,HEIGHT, algas):
        pygame.sprite.Sprite.__init__(self)
        #distância da alga de cima pra de baixo
        self.distancia= 100
        #tamanho da alga em relação ao tamanho random escolhido na de cima
        self.escala_y_invertida= HEIGHT - algas.escala_y - self.distancia
        #faz load da imagem do png e define seu tamanho
        self.image = pygame.image.load(imagem_alga_invertida).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, self.escala_y_invertida))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = algas.rect.x
        self.rect.y = -30
        self.speedx = -10
        self.speedy = 0
        self.outra_alga=algas

    def update(self):
        #movimenta a alga pra trás e quando chega no final da tela volta pro começo
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.x = self.outra_alga.rect.x
            self.escala_y_invertida= HEIGHT - self.outra_alga.escala_y - self.distancia
            self.image = pygame.transform.scale(self.image, (60, self.escala_y_invertida))
            self.speedx = -10
            self.speedy = 0
#classe do peixe
class peixe(pygame.sprite.Sprite):
    def __init__(self,vel_x,vel_y,WIDTH,HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        #faz load da imagem do png e define seu tamanho
        self.image = pygame.image.load(imagem_peixe).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 30))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        #coloca o peixe no meio da tela
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT/2
        self.speedx = 0
        self.speedy = 0
        #aceleração do peixe
        self.count = 1

    def update(self):
        #faz o peixe cair com aceleração
        self.speedy += self.count
        self.rect.y += self.speedy
        #faz o peixe não sair da tela
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.y < 40:
            self.rect.y = 40
    
    def pulo(self):
        #quanto ele sobe no pulo
        self.speedy = -10
       
#classe do fundo
class fundo(pygame.sprite.Sprite):
    def __init__(self,WIDTH,HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        #faz load da imagem e define seu tamanho
        self.image = pygame.image.load(imagem_fundo).convert()
        #bota escala pra tampar o fundo inteiro
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        #move o fundo pra trás
        self.speedx = -10
        self.speedy = 0
        self.largura= WIDTH

    def update(self):
        #faz o fundo voltar quando chega a zero
        self.rect.x += self.speedx
        if self.rect.x + self.largura == 0:
            self.rect.x= self.largura
#classe do segundo fundo para que se mexa a imagem do fundo sem ficar sem fundo
class fundo2(pygame.sprite.Sprite):
    #condições iniciais
    def __init__(self,WIDTH,HEIGHT):
            pygame.sprite.Sprite.__init__(self)
            #faz load da imagem (fundo invertida) e define seu tamanho
            self.image = pygame.image.load(imagem_fundo2).convert()
            self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
            self.rect = self.image.get_rect()
            self.rect.x = WIDTH
            self.rect.y = 0
            self.speedx = -10
            self.speedy = 0
    #faz o fundo voltar quando chega a zero
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x + WIDTH == 0:
            self.rect.x = WIDTH

