
### Necessary imports
import pygame, json
from random import randint, choice
from sys import exit
from time import time

### Initialization and base variable constants
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

CLOCK = pygame.time.Clock()

WIDTH = 1024
HEIGHT = 768

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('This is a template'.upper())

### Main game func/loop
def MAIN():

    RUN = True

    while RUN:

        #WINDOW.fill((50,50,255))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('LEFT')
                    Prompt(16,64,(300,300))

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print('RIGHT')

            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_ESCAPE:

                    pygame.quit()
                    exit()

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('LEFT RELEASED')

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print('RIGHT RELEASED')


        #SIRIUS.update()
        pygame.display.flip()

### Call to MAIN game func to run game
MAIN() if __name__ == '__main__' else print('Not Main')
