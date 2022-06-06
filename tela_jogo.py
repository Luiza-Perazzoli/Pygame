import pygame
from game import jogo
from fim import tela_final
from inicio import tela_inicial

pygame.init()
pygame.mixer.init()
WIDTH = 800
HEIGHT = 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('peixinho')

state = "INIT"
while state != "QUIT":
    tela_inicial(window)
    jogo(window)
    tela_final(window)

if state == "QUIT":
    tela_final(window)

pygame.quit()