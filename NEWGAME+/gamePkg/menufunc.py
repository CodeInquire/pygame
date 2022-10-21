def MenuScreen():
    
    global dagger

    sound.pause()
    music.pause()
    menuVibe.play(menuMusic, -1)

    print('menu entered')

    menuBGI = pygame.transform.scale(pygame.image.load('graphics/siriusDrawn.jpg'), (540, 810))

    basicFont = pygame.font.Font('font/PixeloidSans-nR3g1.ttf', 33)#pygame.font.SysFont(None, 36, italic = True)

    menuPlyr = pygame.transform.scale(pygame.image.load('graphics/Player_UI.png'), (200,240))
    menuPlayerRect = menuPlyr.get_rect(center = (130, 200))

    itemBorder = pygame.Rect(30, 630, 444, 150)
    itemText = basicFont.render('INVENTORY', True, (213,123,213))
    itemTextRect = itemText.get_rect(bottomleft = itemBorder.topleft)

    coinImg = pygame.transform.scale(pygame.image.load('graphics/coins.png'), (45,45))
    coinRect = coinImg.get_rect(topleft = (33,470))
    coinImg.set_colorkey((255,255,255))

    heartImg = pygame.transform.scale(pygame.image.load('graphics/hearts.png'), (39,39))
    heartRect = coinImg.get_rect(topleft = (42,433))

    messageTimer = 100

    showText = False
    menu = True
    while menu:

        screen.fill((245,245,245))

        screen.blit(menuBGI, (360, 0, 420, 720))

        menuBGI.set_alpha(81)

        pygame.draw.line(screen, (0,0,0), (530,81), (369,81), 2)
        pygame.draw.line(screen, (0,0,0), (500,175), (369,175), 2)
        pygame.draw.line(screen, (0,0,0), (480,300), (369,300), 2)
        pygame.draw.line(screen, (0,0,0), (540,600), (369,600), 2)
        pygame.draw.rect(screen, (0,0,0), (270, 15, 72, 72), 2)
        pygame.draw.rect(screen, (0,0,0), (270, 144, 72, 72), 2)
        pygame.draw.rect(screen, (0,0,0), (270, 291, 72, 72), 2)
        pygame.draw.rect(screen, (0,0,0), (270, 531, 72, 72), 2)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                        menu = False
                        print('menu exited')
                        menuVibe.pause()
                        sound.unpause()
                        music.unpause()
                    
                    
            # MOUSE EVENT DETECTION

            #pygame.mouse.set_cursor(system)
            mx, my = pygame.mouse.get_pos()

            left, middle, right = pygame.mouse.get_pressed()

            rightClicking = False
            leftCLicking = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if left:
                    leftClicking = True

                    if mapScrn.clicked:
                        showText = True
                        print('Navigate to Map Screen')

                    elif SET.clicked:
                        SETTINGS()

                    else:
                        print('nothing to interact with')

                if middle:
                    print('middle button clicked')

                if right:
                    print('right button clicked')
                    rightClicking = True
                
            if event.type == pygame.MOUSEBUTTONUP:

                if left:
                    leftClicking = False

                if right:
                    rightClicking = False
                        

        if showText == True:######## PUT INTO SINGLE MULTI-USE FUNCTION
            
            if messageTimer >= 0:
                messageToScreen(f'Feature Currently Unavailable', 420, 400, 18)

                messageTimer -= 1
                #debug(messageTimer)
                
            if messageTimer <= 0:
                messageTimer = 100
                showText = False

        if dagger.rect.collidepoint(pygame.mouse.get_pos()):
            messageToScreen(dagger.dscr, dagger.rect.x+150, dagger.rect.y-21, 15)
            messageToScreen(dagger.name+'s', dagger.rect.x+150, dagger.rect.y+30, 15)


        screen.blit(menuPlyr, menuPlayerRect)
        screen.blit(itemText, itemTextRect)
        screen.blit(heartImg, heartRect)
        screen.blit(coinImg, coinRect)
        

        pygame.draw.rect(screen, (0,0,0), itemBorder, 2)
        

        dagger.draw()
        

        displayStats()


        mapScrn.draw()
        mapScrn.checkClick()


        SET.draw()
        SET.checkClick()


        pygame.display.update()

        clock.tick(60)
