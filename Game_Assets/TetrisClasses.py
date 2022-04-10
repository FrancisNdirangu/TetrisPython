#TetrisClasses


import pygame
import random
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((590,960))

#background image
background_img = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/Mockup/background.jpg')

#there will be two groups
#the group for the object we are controlling and another for the stationary pieces that aren't moving

#what i can do is control the shape until there is a collision. then after that I would move the shape into the stationary class, empty the controlled class and spawn a new shape


class MovingObjects(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #the different shapes
        T_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/T/T_2.png')
        Z_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/S/S.png')
        O_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/R/R.png')
        L_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/L/L.png')
        I_shape = pygame.image.load('C:/Users/franc/Downloads/Tetris-game-assets/Game_Assets/I/1.png')

        #array full of the shapes
        self.shapes = [T_shape,Z_shape,O_shape,L_shape,I_shape]
        #this will be the shape that we are controlling
        self.shape_chosen = self.shapes[random.randint(0,len(self.shapes))]
    
    def movement(self):
        self.shape_chosenrect.y += 2

        key = pygame.key.get_pressed()
        if event.type == key[K_RIGHT]:
            self.shape_chosenrect.x += 10
        if event.type == key[K_LEFT]:
            self.shape_chosenrect.x -= 10


