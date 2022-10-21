
### Necessary imports
import pygame, json, turtle
from random import randint, choice
from sys import exit
from time import time
from debug import debug
from gamePkg.images import images
from gamePkg.dice import diceRoll
from gamePkg.entityclass import Entity
from gamePkg.loadingfunc import Loading
from gamePkg.messagefunc import Write
from gamePkg.weaponclass import Weapon, WEAPONS
from gamePkg.button import Button

### Initialization and base variable constants
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

CLOCK = pygame.time.Clock()

WIDTH = 1024
HEIGHT = 768

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Canis Major V2'.upper())

### Player Instance
SIRIUS = Entity(700,100,images['knight'][0])
ENEMY = Entity(50,100,images['jester'][0])

###
BGI = pygame.transform.scale(images['village'][2], (1024, 768))
BGIrect = BGI.get_rect()

### Main game func/loop
def MAIN():

    optionBox = pygame.Surface((200,300))
    optionBox.fill((255,255,255))
    opRect = optionBox.get_rect(center=(pygame.mouse.get_pos()))
    showBox = False

    ### Converts integer id tag to corresponding class instance
    for item in list(SIRIUS.stats['items']):
        if item == 0:
            SIRIUS.stats['items'].remove(item)
            SIRIUS.stats['items'].append(WEAPONS[0])
        if item == 1:
            SIRIUS.stats['items'].remove(item)
            SIRIUS.stats['items'].append(WEAPONS[1])

    print(SIRIUS.stats['items']) # simple test output
    print(images['forest'][0])

    RUN = True

    while RUN:

        WINDOW.blit(BGI, BGIrect)

        SIRIUS.update() ### Renders sprites onto screen
        ENEMY.update()

        Write(WINDOW, f"{SIRIUS.stats['name']}",(200,203,200), 800, 90, 36)
        Write(WINDOW, 'Enemy', (231,123,213), 100, 90, 36)

        Write(WINDOW, 'The following is the first of many dialogue trees..', (123,0,231),  500, 300, 48)
        Write(WINDOW, 'Which path will you choose?', (0, 213, 123), 500, 330, 48)
        answerA = Button('A)',100,50, (300, 350), (123,123,123), (123,213,0))
        answerA.draw()

        answerB = Button('B)',100,50, (300, 450), (123,123,123), (0,213,213))
        answerB.draw()

        Write(optionBox, 'OPTIONS', (50,255,50), 50, 10, 26)
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                data = {
                    'lvl': SIRIUS.stats['level'],
                    'xp': SIRIUS.stats['exp'],
                    '$': SIRIUS.stats['$$$'],
                    'hp': SIRIUS.stats['health'],
                    'mgc': [spell.tag for spell in SIRIUS.stats['magic']],
                    'inv': [item.tag for item in SIRIUS.stats['items']],
                    'eqp': {},
                    }

                with open('gameSave.txt', 'w') as gameSave:
                    json.dump(data, gameSave)

                print('FILE SAVED')

                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('LEFT')

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print('RIGHT')

                elif event.key == pygame.K_g:
                    SIRIUS.stats['items'].append(WEAPONS[0])
                    print(SIRIUS.stats['items'])

                elif event.key == pygame.K_SPACE:
                    #SIRIUS.stats['items'].pop() if len(SIRIUS.stats['items']) > 0 else print('no items in inventory')
                    #print(SIRIUS.stats['items'])
                    #Loading()
                    diceRoll(20)

                elif event.key == pygame.K_t:
                    showBox = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('LEFT RELEASED')

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print('RIGHT RELEASED')

                elif event.key == pygame.K_t:
                    showBox = False

            ### Mouse Input
            mx, my = pygame.mouse.get_pos()

            left, middle, right = pygame.mouse.get_pressed()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if left:
                    print('left button clicked')
                if middle:
                    print('middle button clicked')
                    print(f'Mouse coords are {(mx, my)}')
                if right:
                    print('right button clicked')

            if event.type == pygame.MOUSEBUTTONUP:
                 
                if left:
                    print('left button released')
                    
                if middle:
                    print('middle button released')

                if right:
                    print('right button released')

        #WINDOW.blit(optionBox, opRect) if showBox == True else print('option box NOT displaying')
        
        pygame.display.update()

        '''for sprite in sorted(allSprites, key = lambda sprite: sprite.rect.bottom):
        pygame.display.get_surface().blit(sprite.image, sprite.rect)'''

### Call to MAIN func to run game
MAIN() if __name__ == '__main__' else print('Not Main')
