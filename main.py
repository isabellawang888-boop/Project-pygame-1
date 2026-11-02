import pygame
from sys import exit

# Set up
pygame.init() #Initialize pygame(very important), this is the first step in any pygame program
screen = pygame.display.set_mode((800, 400)) #Set the size of the window: pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner") #Set the title of the window

#Game loop
while True:
    for event in pygame.event.get(): #Process all events in the event queue(the event are usually user inputs))
        if event.type == pygame.QUIT: #Check if the user has clicked the close button(the pygame.QUIT is build-in)
            pygame.quit() #Quit pygame
            exit() #Exit the program

    # Draw all elements
    # Update everything
    pygame.display.update()#Display the updated screen(update of a frame is another loop), this is the last step 
