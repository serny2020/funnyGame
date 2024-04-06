import pygame
import random
# global variable
SCREENSIZE=(600,600)
BLACK=(0,0,0,13)
# initialize pygame
pygame.init()
font = pygame.font.SysFont('Consolas', 20)
screen = pygame.display.set_mode(SCREENSIZE)
surface = pygame.Surface(SCREENSIZE, flags=pygame.SRCALPHA) # create surface for fading effect
pygame.Surface.convert(surface)
surface.fill(BLACK)
screen.fill(BLACK)
# content of digital rain
lib=[chr(i) for i in range(48,48+10)] + [chr(i) for i in range(97,97+26)]   # list of all chars in the rain
texts = [font.render(l, True, (0, 255, 0)) for l in lib]
cols = list(range(40)) 

# drawing
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(33)
    screen.blit(surface, (0, 0)) # transparent background
    for i in range(n:=len(cols)):
        text = random.choice(texts)
        # printing the digital rain
        screen.blit(text, (i * 15, cols[i] * 15)) # pick a letter and draw on screen
        cols[i] = 0 if cols[i] >80 or random.random() > 0.95 else cols[i]+1
    pygame.display.flip()