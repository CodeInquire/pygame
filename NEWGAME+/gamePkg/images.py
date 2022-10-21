import pygame

### A dictionary holding various images sorted by scene-type
images = {
    'forest': [pygame.image.load('gamePkg/graphics/forest1.png'),
                  pygame.image.load('gamePkg/graphics/forest2.png')],

    'village': [pygame.image.load('gamePkg/graphics/village1.png'),
                   pygame.image.load('gamePkg/graphics/village2.png'),
                    pygame.image.load('gamePkg/graphics/village3.png')],

    'knight': [pygame.image.load('gamePkg/graphics/knight.png'),],

    'jester': [pygame.image.load('gamePkg/graphics/jester.png'),],
    }
