import pygame
from game import jogo
from fim import tela_final

pygame.init()
pygame.mixer.init()
WIDTH = 800
HEIGHT = 400

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

state = "INIT"
while state != "QUIT":
    if state == "INIT":
        state = jogo(window)
    elif state == "GAME":
        state = jogo(window)

if state == "QUIT":
    state = tela_final(window)

pygame.quit()