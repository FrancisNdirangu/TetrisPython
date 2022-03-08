#Making Tetris

import pygame
pygame.init()

screen = pygame.display.set_mode((590,960))



background_img = pygame.image.load('C:\Users\franc\Downloads\Tetris-game-assets\Game_Assets\Mockup\background.jpg')
running = True

while running:
    pygame.display.flip()
    screen.blit(background_img,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

pygame.quit()



