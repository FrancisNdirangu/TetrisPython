#Making Tetris

import pygame
import numpy as np
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((590,960))


#background image
background_img = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/Mockup/background.jpg')

#now I will place the different shapes we need for Tetris

locationx = 250
locationy = 150


I_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/I/1.png')
I_shape = pygame.transform.scale(I_shape,(150,150))
I_shaperect = I_shape.get_rect(midbottom = (locationx,locationy))

L_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/L/L.png')
L_shape = pygame.transform.scale(L_shape,(150,150))
L_shaperect = L_shape.get_rect(midbottom = (locationx,locationy))

O_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/R/R.png')
O_shape = pygame.transform.scale(O_shape,(150,150))
O_shaperect = O_shape.get_rect(midbottom = (locationx,locationy))

Z_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/S/S.png')
Z_shape = pygame.transform.scale(Z_shape,(150,150))
Z_shaperect = Z_shape.get_rect(midbottom = (locationx,locationy))

T_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/T/T_2.png')
T_shape = pygame.transform.scale(T_shape,(150,150))
T_shaperect = T_shape.get_rect(midbottom = (locationx,locationy))

shape_chosen = [I_shape,L_shape,O_shape,Z_shape,T_shape]
shape_chosenrect = [I_shaperect,L_shaperect,O_shaperect,Z_shaperect,T_shaperect]
index_shape = np.random.randint(0,(len(shape_chosen)))


print(index_shape)

running = True

while running:
    pygame.display.flip()
    clock.tick(60)
    screen.blit(background_img,(0,0))
    # locationy += 2
    # if locationy > 810:
    #     locationy = 810
    # I_shaperect.bottom += 2
    # L_shaperect.bottom += 2
    # O_shaperect.bottom += 2
    # Z_shaperect.bottom += 2
    # T_shaperect.bottom += 2
    for i in range(len(shape_chosenrect)):
        shape_chosenrect[i].bottom +=2
        if shape_chosenrect[i].bottom > 990:
            shape_chosenrect[i].bottom = 990


    

    screen.blit(shape_chosen[index_shape],shape_chosenrect[index_shape])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                shape_chosenrect[index_shape].right += 10
                if shape_chosenrect[index_shape].right > 470:
                    shape_chosenrect[index_shape].right = 470
            if event.key == pygame.K_LEFT:
                shape_chosenrect[index_shape].left -= 10
                if shape_chosenrect[index_shape].left < -15:
                    shape_chosenrect[index_shape].left = -15
            if event.key == pygame.K_UP: #this code doesnt work. the reason is because we set shape_chosen[index_shape].bottom to a constant. the bottom must change as the shape rotates for this to work
                shape_chosenrect[index_shape] = pygame.transform.rotate(shape_chosenrect[index_shape],90)
                shape_chosen[index_shape] = pygame.transform.rotate(shape_chosen[index_shape],90)
        


    

pygame.quit()



