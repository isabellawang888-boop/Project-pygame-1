Display surface: screen = pygame.display.set_mode((800, 400)) -> pygame.display.set_mode((width, height))
                 line 6 in main.py
Regular surface: test_surface = pygame.Surface((100, 200)) -> pygame.Surface((width, height))
                 line 10 in main.py


Set(define) the clock: clock = pygame.time.Clock()
                       - we actually didn't assign it to a value at this stage
                       line 8 in main.py
Assign and create the value of FPS for the game using the clock var we created outside the game loop: clock.tick(60)
                                                                                                      line 22 in main.py

.time is a module of pygame/.Clock() is a class of pygame.time module and we can use its method(ex: clock = pygame.time.Clock *next line* clock.tick())


Draw stuff(steps): 1. Create a surface(or reserve an area of the main screen):test_surface = pygame.Surface((100, 200))
                   2. Fill that entre space with red: test_surface.fill("red")
                   3. Copies that red area onto the main screen: screen.blit(test_surface, (0, 0))

                   
Important function: .fill() .blit() .Surface() .set_mode .Clock 
Important standard protocol: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Quit pygame
            exit()
