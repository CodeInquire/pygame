import pygame

def Loading():

    CLOCK = pygame.time.Clock()

    screen = pygame.Rect(1,1,1,1)
    screen.fill((255,0,0))
    screen.set_alpha(50)
    
    blk = pygame.Rect(1,1,1,1)

    loadTimer = 300
    
    loading = True
    
    while loading:

        pygame.display.get_surface().fill((255,255,255))

        for event in pygame.event.get():

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    loading = False

        if loadTimer > 0 :
            blk = blk.inflate(24,18)
            blk.center = (512,384)
            loadTimer -= 1
            pygame.display.get_surface().blit(screen,blk)
            
        else:
            loading = False
        
        pygame.draw.rect(pygame.display.get_surface(), (0,0,0), blk)

        pygame.display.update()
        
        CLOCK.tick(60)
