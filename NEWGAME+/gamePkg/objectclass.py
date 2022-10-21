import pygame

class Object(pygame.sprite.Sprite):

    def __init__(self, image, x_pos, y_pos, width, height):
        super().__init__()

        self.image = image

        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect(midbottom = (x_pos, y_pos))

        #self.image.fill((255,255,255))

        #self.hitbox = self.rect.inflate(0,0)    

        #self.hitbox.update(self.hitbox.left,self.hitbox.top, width,height)
        
    def update(self):

        bg.image.blit(self.image, self.rect)

        if debug_mode:
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox)

    def collide(self, entity):

        if entity.hitboxRect.colliderect(self.hitbox):

            entity.moveDown = False

            entity.moveLeft = False

            entity.moveRight = False

            entity.moveUp = False

            print("hitBox collision")
