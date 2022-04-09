#Making Tetris

import pygame
import numpy as np
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((590,960))


#background image
background_img = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/Mockup/background.jpg')

#now I will place the different shapes we need for Tetris

locationx = 212
locationy = 150


I_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/I/1.png')
I_shape = pygame.transform.rotozoom(I_shape,0,0.3)
I_shaperect = I_shape.get_rect(midbottom = (locationx,locationy))

L_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/L/L.png')
L_shape = pygame.transform.rotozoom(L_shape,0,0.3)
L_shaperect = L_shape.get_rect(midbottom = (locationx,locationy))

O_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/R/R.png')
O_shape = pygame.transform.rotozoom(O_shape,0,0.3)
O_shaperect = O_shape.get_rect(midbottom = (locationx,locationy))

Z_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/S/S.png')
Z_shape = pygame.transform.rotozoom(Z_shape,0,0.3)
Z_shaperect = Z_shape.get_rect(midbottom = (locationx,locationy))

T_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/T/T_2.png')
T_shape = pygame.transform.rotozoom(T_shape,0,0.3)
T_shaperect = T_shape.get_rect(midbottom = (locationx,locationy))

shape_chosen = [I_shape,L_shape,O_shape,Z_shape,T_shape]
shape_chosenrect = [I_shaperect,L_shaperect,O_shaperect,Z_shaperect,T_shaperect]
index_shape = np.random.randint(0,(len(shape_chosen)))


#print(index_shape)

running = True

location_tracker_horizontal = 212 #tracking the horizontal position of the shape
while running:
    pygame.display.flip()
    clock.tick(60)
    screen.blit(background_img,(0,0))

    for i in range(len(shape_chosenrect)):
        shape_chosenrect[i].bottom +=10
        if I_shaperect.bottom > 970:
            I_shaperect.bottom = 970
        if L_shaperect.bottom > 985:
            L_shaperect.bottom = 985
        if Z_shaperect.bottom > 1000:
            Z_shaperect.bottom = 1000
        if T_shaperect.bottom > 1000:
            T_shaperect.bottom = 1000
        if O_shaperect.bottom > 1000:
            O_shaperect.bottom = 1000
            #print("the final location is ",location_tracker_horizontal)
            #i should also find a way of ensuring that the shapes cannot move once they are in their final position and in order to do that I need to save their coordinates
            #i should store the location and shape in a dictionary in a list
            #i should then generate a new shape


    #location tracker

    screen.blit(shape_chosen[index_shape],shape_chosenrect[index_shape])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                shape_chosenrect[index_shape].right += 10
                location_tracker_horizontal = shape_chosenrect[index_shape].right
                if I_shaperect.right > 495:
                    I_shaperect.right = 495
                if L_shaperect.right > 500:
                    L_shaperect.right = 500
                if Z_shaperect.right > 465:
                    Z_shaperect.right = 465
                if T_shaperect.right > 500:
                    T_shaperect.right = 500
                if O_shaperect.right > 480:
                    O_shaperect.right = 480
                
                # if location_tracker_horizontal >400:
                #     location_tracker_horizontal = 400 #setting a limit on the location tracker to know boundary has been reached
                #if shape_chosenrect[index_shape].right > 465:
                 #   shape_chosenrect[index_shape].right = 465
            if event.key == pygame.K_LEFT:
                shape_chosenrect[index_shape].left -= 10
                location_tracker_horizontal -= 10
                # if location_tracker_horizontal < -50:
                #     location_tracker_horizontal = -50 #setting a limit on the location tracker to know boundary has been reached
                if I_shaperect.left < -55:
                    I_shaperect.left = -55
                if L_shaperect.left < -40:
                    L_shaperect.left = -40
                if Z_shaperect.left < -20:
                    Z_shaperect.left = -20
                if T_shaperect.left < 0:
                    T_shaperect.left = 0
                if O_shaperect.left < -35:
                    O_shaperect.left = -35
                # if shape_chosenrect[index_shape].left < -50:
                #     shape_chosenrect[index_shape].left = -50
            if event.key == pygame.K_UP: 
                shape_chosen[index_shape] = pygame.transform.rotate(shape_chosen[index_shape],90) #the code works when i only rotate the image
                 
        #to make new shapes appear i can check if the velocity of the shape is zero. if that is the case then a new shape should be called
        #we can also make new shapes appear when we sense a collision between the falling shape and anything else
        #i can then also make another if statement to produce new shapes when the "floor" is reached since I dont know how to make 
    

#some of the shapes dont reach the left or right boundary because they have different thicknesses
#find a way of using collisions to make all the shapes able to reach the edge
    

pygame.quit()



