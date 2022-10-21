class Armor(pygame.sprite.Sprite):
    def __init__(self, name, description, image, type, defensePower, special):
        super().__init__()

        self.name = name
        self.dscr = description
        self.image = image
        self.rect = self.image.get_rect()

        self.stats = {
            'type': type,
            'dfn': defensePower,
            'special': special,
            }

    def __repr__(self):
        return self.name


    def equip(self):
        if sirius.stats['items'].__contains__(self):
            sirius.stats['equip']['wpn1'] = self
        else:
            print('You dont own that item!')

    def draw(self, xPos, yPos):
        screen.blit(self.image, self.rect)
