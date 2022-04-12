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

        spawning_x_position = 212
        spawning_y_position = 150
        self.shape_chosenrect = self.shape_chosen.get_rect(midbottom = (spawning_x_position,spawning_y_position))

    def pieces_movement_boundaries(self):
        self.shape_chosenrect.y += 2
        if self.shape_chosenrect.y > 990:
            self.shape_chosenrect.y =990
        
        #the y_boundaries for each shape, find out if the shapes need a self infront of them since they are constants
        if self.I_shape.bottom > 970:
            self.I_shape.bottom = 970
        if self.L_shape.bottom > 985:
            self.L_shape.bottom = 985
        if self.Z_shape.bottom > 1000:
            self.Z_shape.bottom = 1000
        if self.T_shape.bottom > 1000:
            self.T_shape.bottom = 1000
        if self.O_shape.bottom > 1000:
            self.O_shaperect.bottom = 1000

        #boundaries to the right
        if self.I_shape.right > 495:
            self.I_shape.right = 495
        if self.L_shape.right > 500:
            self.L_shape.right = 500
        if self.Z_shape.right > 465:
            self.Z_shape.right = 465
        if self.T_shape.right > 500:
            self.T_shape.right = 500
        if self.O_shape.right > 480:
            self.O_shape.right = 480

        #boundaries to the right
        if self.I_shape.left < -55:
            self.I_shape.left = -55
        if self.L_shape.left < -40:
            self.L_shape.left = -40
        if self.Z_shape.left < -20:
            self.Z_shape.left = -20
        if self.T_shape.left < 0:
            self.T_shape.left = 0
        if self.O_shape.left < -35:
            self.O_shape.left = -35
    
    def controlled_movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.shape_chosenrect.x += 10  #moving the shape by refering to the rectangle of the shape
        if key[pygame.K_LEFT]:
            self.shape_chosenrect.x -= 10
        if key[pygame.K_SPACE]:
            self.shape_chosenrect = pygame.transform.rotate(self.shape_chosenrect,90)


