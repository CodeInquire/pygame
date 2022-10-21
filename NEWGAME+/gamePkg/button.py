import pygame

class Button:

    def __init__(self, text, w, h, pos, textColor, rectColor, image = None):
        button_color = rectColor

        basicFont = pygame.font.SysFont(None, 36, italic = True)
        
        # TOP RECT
        self.topRect = pygame.Rect(pos,(w,h))
        self.topColor = rectColor

        # TEXT
        self.textSurf = basicFont.render(text, False, textColor)
        self.textRect = self.textSurf.get_rect(center = self.topRect.center)

        self.image = image
        if self.image == None:
            pass
        else:
            self.imageRect = self.image.get_rect(midbottom = self.topRect.midbottom)

        self.clicked = False
    button_color =(255,255,255)
    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(), self.topColor, self.topRect, border_radius = 0)
        pygame.display.get_surface().blit(self.textSurf, self.textRect)
        if self.image == None:
            pass
        else:
            pygame.display.get_surface().blit(self.image, self.imageRect)
    def display_disabled(self):
        self.topColor = (10,10,10)
        
    def display_enabled(self):
        self.topColor = (255,0,0)

    def checkClick(self):
        mousePos = pygame.mouse.get_pos()
        if self.topRect.collidepoint(mousePos):
            self.clicked = True
            #self.topColor = (255,50,50)
            #pygame.draw.rect(screen, (0,0,0), self.topRect, 5, border_radius = 0)
            
        else:
            #self.topColor = (33,255,33)
            self.clicked = False
