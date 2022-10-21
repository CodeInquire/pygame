import pygame

pygame.init()

font = pygame.font.Font(None, 33)

def debug(info, x = 333, y = 333):

    displaySurf = pygame.display.get_surface()

    debugSurf = font.render(str(info), True, 'Black')

    debugRect = debugSurf.get_rect(topleft = (x, y))

    displaySurf.blit(debugSurf, debugRect)
