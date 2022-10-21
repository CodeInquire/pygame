class NPC(pygame.sprite.Sprite):

    def __init__(self, name, health, image, x_pos, y_pos):
        super().__init__()

        self.name = name
        self.image = image
        self.image.set_colorkey((255,255,255))
        #self.image.fill((222,54,147))
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
        self.interact = pygame.draw.circle(screen, (0,255,0), self.rect.center, 66, 3)
        #self.velocity = 1
        self.stats = {
            'name': name,
            'level': 1,
            'exp': 0,
            'health': health,
            'items': [],
            'equip': {
                'head': None,
                'body': None,
                'legs': None,
                'cowl': None,
                'wpn1': None,
                'wpn2': None,
                },
            'magic': []
            }

    def __repr__(self):
        return self.name

    def movement(self):
        pass

    def collide(self):
        if self.rect.colliderect(sirius.hitboxRect):
            messageToScreen('Testing message func...', self.rect.x, self.rect.y - 30)

    def update(self):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, (0,255,0), self.rect.center, 66, 3)
