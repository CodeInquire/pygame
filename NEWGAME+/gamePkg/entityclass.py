import pygame, json

try:
    with open('gameSave.txt') as gameSave:

        data= json.load(gameSave)

        for entry in data.items():
            print(entry)

except:
    print('No Save File Created Yet')


class Entity(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos, image=None):
        super().__init__()

        # SPRITE FRAMES
        #idle1, idle2 = pygame.transform.scale(pygame.image.load('graphics/idle1.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/idle2.png').convert_alpha(), (96,96))
        #left1, left2, left3, left4, left5, left6 = pygame.transform.scale(pygame.transform.flip(pygame.image.load('graphics/right1.png').convert_alpha(), True, False), (96,96)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('graphics/right2.png').convert_alpha(), True, False), (96,96)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('graphics/right3.png').convert_alpha(), True, False), (96,96)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('graphics/right4.png').convert_alpha(), True, False), (96,96)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('graphics/right5.png').convert_alpha(), True, False), (96,96)), pygame.transform.scale(pygame.transform.flip(pygame.image.load('graphics/right6.png').convert_alpha(), True, False), (96,96))
        #right1, right2, right3, right4, right5, right6 = pygame.transform.scale(pygame.image.load('graphics/right1.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/right2.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/right3.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/right4.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/right5.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/right6.png').convert_alpha(), (96,96))
        #up1, up2, up3, up4, up5 = pygame.transform.scale(pygame.image.load('graphics/up1.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/up2.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/up3.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/up4.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/up5.png').convert_alpha(), (96,96))
        #down1, down2, down3, down4, down5, down6 = pygame.transform.scale(pygame.image.load('graphics/down1.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/down2.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/down3.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/down4.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/down5.png').convert_alpha(), (96,96)), pygame.transform.scale(pygame.image.load('graphics/down6.png').convert_alpha(), (96,96))

        self.velocity = 1 # MOVEMENT SPEED
        self.shift = False # FOR SPRINTING: HOLD LSHFT
        self.moveLeft = False  # ----
        self.moveRight = False # SETS PLAYER MOVEMENT-TOGGLE-VARIABLES
        self.moveUp = False    # ----
        self.moveDown = False  # ----

        #self.idle = [idle1, idle2]
        self.idleIndex = 0
        self.idling = False

        #self.runRight = [right1, right2, right3, right4, right5, right6]
        self.rightIndex = 0
        self.runningRight = False

        #self.runLeft = [left1, left2, left3, left4, left5, left6]
        self.leftIndex = 0
        self.runningLeft = False

        #self.runUp = [up1, up2, up3]
        self.upIndex = 0
        self.runningUp = False

        #self.runDown = [down1, down2, down3]
        self.downIndex = 0
        self.runningDown = False

        self.moveFrame = 0
        self.moveFrameDown = 0

        #self.idle[self.idleIndex] # PLAYER SURFACE / SPRITE
        self.image = pygame.transform.scale(image, ((300,400)))

        if self.image == None:
            self.image = pygame.Surface((50,100)) 
        else:
            self.rect = self.image.get_rect() # GETS RECT FROM LOADED IMAGE
            self.rect.topleft = [x_pos, y_pos] # SETS RECT COORDS
            self.mask = pygame.mask.from_surface(self.image)

            self.hitboxRect = self.rect.inflate(-60,-80)
            self.hitboxRect.topleft = [x_pos, y_pos]
            self.hitboxRect.midbottom = self.rect.midbottom
            
            self.hitboxRect = self.hitboxRect.move(0,-20)

        try:
            self.stats = {
                'name': 'Sirius',
                'level': data['lvl'],
                'exp': data['xp'],
                'health': data['hp'],
                'items': data['inv'],
                'equip': data['eqp'],
                'magic': data['mgc'],
                '$$$': data['$']
                }
        except:
            self.stats = {
                'name': 'Sirius',
                'level': 1,
                'exp': 0,
                'health': 100,
                'items': [],
                'equip': {
                    'head': None,
                    'body': None,
                    'legs': None,
                    'cowl': None,
                    'wpn1': None,
                    'wpn2': None,
                    },
                'magic': [],
                '$$$': 30
                }
        
        self.walkingPace = 1000 // 7 #Higher == faster. inter-frame delay in milliseconds
        self.runningPace = 1000 // 10
        self.idlingPace = 1000 // 4
        self.millisec_rate = self.walkingPace
        self.last_frame_at = 0
        self.shouldAnimate = True
        self.lengthBeforeIdling = 1000
        self.isIdling = True

    def movement(self):

        if self.shift:
            self.velocity = 3
            self.millisec_rate = self.runningPace
        else:
            self.velocity = 1
            self.millisec_rate = self.walkingPace
                    

        # Idling check
        if not self.moveLeft and not self.moveRight and not self.moveUp and not self.moveDown:
            self.isIdling = True
            self.millisec_rate = self.idlingPace
        else:
            self.isIdling = False


        time_now = pygame.time.get_ticks()
        if (time_now > self.last_frame_at + self.millisec_rate):
            self.moveFrame += 1
            self.shouldAnimate = True
            self.last_frame_at = time_now
        else:
            self.shouldAnimate = False

        if self.moveDown and self.rect.bottom < pygame.display.get_surface().get_height():
            if (self.moveFrame >= len(self.runDown)):
                self.moveFrame = 0
            if self.shouldAnimate:
                self.image = self.runDown[self.moveFrame]
            self.rect.bottom += self.velocity


        if self.moveUp and self.rect.top > 0:
            if (self.moveFrame >= len(self.runUp)):
                self.moveFrame = 0
            if self.shouldAnimate:
                self.image = self.runUp[self.moveFrame]
            self.rect.top -= self.velocity


        if self.moveLeft and self.rect.left > 0:
            if (self.moveFrame >= len(self.runLeft)):
                self.moveFrame = 0
            if self.shouldAnimate:
                self.image = self.runLeft[self.moveFrame]
            self.rect.left -= self.velocity


        if self.moveRight and self.rect.right < pygame.display.get_surface().get_width():
            if (self.moveFrame >= len(self.runRight)):
                self.moveFrame = 0
            if self.shouldAnimate:
                self.image = self.runRight[self.moveFrame]
            self.rect.right += self.velocity

        # Idling
        #if self.isIdling and self.shouldAnimate:
            #if self.moveFrame >= len(self.idle):
                #self.moveFrame = 0
            #self.image = self.idle[self.moveFrame]

    def update(self):
        self.movement()
        try:
            pygame.display.get_surface().blit(self.image, self.rect)
        except:
            pass
        #if debug_mode:
            #pygame.draw.rect(screen, (255,0,0), sirius.hitboxRect)
        #self.hitboxRect.center = self.rect.midbottom
        #self.hitboxRect = self.hitboxRect.move(0,-20)
