#Making Tetris

import pygame
import numpy as np
pygame.init()

screen = pygame.display.set_mode((590,960))


#background image
background_img = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/Mockup/background.jpg')

#now I will place the different shapes we need for Tetris
I_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/I/1.png')
I_shape = pygame.transform.scale(I_shape,(150,150))
locationx = 250
locationy = 150
L_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/L/L.png')
L_shape = pygame.transform.scale(L_shape,(150,150))
O_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/R/R.png')
O_shape = pygame.transform.scale(O_shape,(150,150))
Z_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/S/S.png')
Z_shape = pygame.transform.scale(Z_shape,(150,150))
T_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/T/T_2.png')
T_shape = pygame.transform.scale(T_shape,(150,150))

shape_chosen = [I_shape,L_shape,O_shape,Z_shape,T_shape]
index_shape = np.random.randint(0,(len(shape_chosen)+1))

print(index_shape)

running = True

while running:
    pygame.display.flip()
    screen.blit(background_img,(0,0))
    locationy += 0.3
    if locationy > 810:
        locationy = 810
    screen.blit(shape_chosen[index_shape],(locationx,locationy))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    

pygame.quit()



