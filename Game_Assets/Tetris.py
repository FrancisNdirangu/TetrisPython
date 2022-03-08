import pygame


screen = pygame.display.set_mode((590,960))

pygame.display.flip() #this is for updating the display

#initializing pygame
pygame.init()

background_image = pygame.image.load('background.jpg')
#background_image = pygame.transform.scale(background_image,screen)

running = True
while running:
    screen.blit(background_image,(0,0))
    


    for event in pygame.event.get():
        if event.type ==   pygame.QUIT:
            running=False

    pygame.display.update()
pygame.quit()
