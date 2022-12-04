# Import libraries and modules
import pygame
from pygame.locals import *
import constants

class Game():
    
    def __init__(self):
        # Initialize pygame
        pygame.init()
        # Displaying a window
        self.window = pygame.display.set_mode(constants.SIZE)
        # Setting a window title
        self.title = pygame.display.set_caption(constants.TITLE)
        # Setting a window icon
        self.icon = pygame.image.load("images/icon.png")
        pygame.display.set_icon(self.icon)
        # Setting a background color
        self.window.fill(constants.BG_COLOR)
        pygame.display.update()
        
    def run(self):
        # Creating a bool value which checks
        # if game is running
        running = True
        
        # Keep game running till running is true
        while running:
            
            # Check for event if user has pushed
            # any event in queue
            for event in pygame.event.get():
                
                # If event is of type keydown or quit then 
                # set running bool to false
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        
                elif event.type == QUIT:
                    running = False

# Creating a game object  
game = Game()
game.run()
