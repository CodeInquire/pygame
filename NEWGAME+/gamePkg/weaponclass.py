import pygame

###
class Weapon(pygame.sprite.Sprite):
    def __init__(self, tag, name, description, image, type, attackPower, special=None):
        super().__init__()

        self.name = name
        self.dscr = description
        self.image = image
        #self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (309,330))
        self.stats = {
            'type': type,
            'atk': attackPower,
            'special': special
            }
        self.tag = tag

    def __repr__(self):
        return self.name


    def equip(self, player):
        if player.stats['items'].__contains__(self):
            player.stats['equip']['wpn1'] = self
            print('weapon equipped')
        else:
            print('You dont own that item!')

    def draw(self):
        screen.blit(self.image, self.rect)

###
dagger = Weapon(0, 'dagger', 'trusty dagger', pygame.Surface((50,100)), 'slash', 3)

###
sword = Weapon(1, 'longsword', 'a worn blade..', pygame.Surface((50,100)), 'slash', 6)

###
WEAPONS = [

    dagger,
    sword,

    ]
