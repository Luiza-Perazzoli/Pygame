import pygame

pygame.init()
WIDTH = 700
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('flappy fish')

game = True

image = pygame.image.load(r"C:\Users\luiza\OneDrive\Imagens\fundo do mar.webp").convert()
image = pygame.transform.scale(image, (700, 400)) 

font = pygame.font.SysFont("Times", 20)
text = font.render('pontos:', True, (255, 0, 127))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((173, 216, 230))
    window.blit(image, (10, 10))
    window.blit(text, (600, 10))

    pygame.display.update() 

pygame.quit()  