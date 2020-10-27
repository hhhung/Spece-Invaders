import pygame
import time
(width, height) = (1500, 800)
background_colour = (245,245,245)
Y = 750
X = 750
boolet = 0
pew = 785
BY = Y + 15
Koiyl = True #{'left': True, 'right': True, 'fire': True}
Koiyr = True
Koiyf = True
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Panunu')
evant = False
running = True
while running:    
    screen.fill(background_colour)
    pygame.draw.circle(screen, (255,90,0), (int(X), int(Y)), 15, 15)
    pygame.display.flip()
    events = pygame.event.get()
    if not Koiyl:#(f'left') == False:
        if X <= 15:
            X = 15
            pass
        else:
            X -= 1
    if not Koiyr:#(f'right') == False:
        if X >= 1485:
            X = 1485
            pass
        else:
            X += 1
    if not Koiyf:#(f'fire') == False:
        boolet = 1
        
    for event in events:
        #print(event) 
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.KEYDOWN:
            evant = True
            #pygame.key.set_repeat(10,10)
            if event.key == pygame.K_LEFT:                
                Koiyl = False#.update({'left':  False})
            elif event.key == pygame.K_RIGHT:                
                Koiyr = False#.update({'right':  False})                    
            elif event.key == pygame.K_z:
                Koiyf =False #(f"fire") = False
        elif event.type == pygame.KEYUP:
            if not Koiyl:#(f"left") != True:
                Koiyl = True#(f"left") = True
            if not Koiyr:#(f"right") != True:
                Koiyr = True#(f"right")= True
            if not Koiyf:
                Koiyf = True
            #    pass
    if boolet == 1:        
        print("egg")
        #for i in range (pew):
        pygame.draw.circle(screen, (90,255,0), (X, 100), 10, 10)
            #BY += 15
            #pew -= 15
        time.sleep(5)
        boolet = 0
        pew = 785
            
pygame.QUIT        