import pygame
from game import jogo
from fim import tela_final
from inicio import tela_inicial

pygame.init()
pygame.mixer.init()
#tamanho do fundo
WIDTH = 800
HEIGHT = 600
#tela do jogo
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('peixinho')
#começa com a texa inicial, começa o jogo
state = "INIT"
while state != "QUIT":
    tela_inicial(window)
    jogo(window)
    tela_final(window)
#se perder vai pra tela de fim
if state == "QUIT":
    tela_final(window)

pygame.quit()