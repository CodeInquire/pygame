import pygame

def Write(destSurface, text, color, xPos, yPos, fontSize):

    basicFont = pygame.font.SysFont(None, fontSize)

    msg = basicFont.render(text, True, color) # variable containing the 'text'

    msgRect = msg.get_rect(center = (xPos, yPos)) # creating a rectangle for 'msg' variable

    msgBox = pygame.Rect(((msgRect.x - 3), (msgRect.y - 3), (msgRect.width + 3), (msgRect.height + 3)))

    msgBoxFill = pygame.Rect(((msgRect.x - 3), (msgRect.y - 3), (msgRect.width + 3), (msgRect.height + 3)))

    #pygame.draw.rect(destSurface, (123,23,123), msgBox, 5) # FOR PUTTING A BORDER AROUND THE TEXT
    #pygame.draw.rect(destSurface, (234,234,234), msgBoxFill)

    destSurface.blit(msg,msgRect)
