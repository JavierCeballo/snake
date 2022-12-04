# Import libraries and modules
import pygame
from pygame.locals import *
import constants


class Snake():
    def __init__(self, window):
        self.parent_window = window
        # Load the snake body image
        self.snake_body = pygame.image.load("images/snake_section_body.png")
        # Initial position
        self.x = constants.WIDTH/2
        self.y = constants.HEIGHT/2
        
    def move_left(self):
        # for decrease the position in x
        self.x -= 10
        self.draw()
        
    def move_right(self):
        # for increment the position in x
        self.x += 10
        self.draw()
        
    def move_up(self):
        # for decrease the position in y
        self.y -= 10
        self.draw()
        
    def move_down(self):
        # for increment the position in y
        self.y += 10
        self.draw()
        
    def draw(self):
        self.parent_window.blit(self.snake_body, (self.x, self.y))
        pygame.display.flip()
    
 
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
        
        # Creating a snake object
        self.snake = Snake(self.window)
        self.snake.draw()
        
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
                    
                    # Movement to left
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    
                    # Movement to right
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    
                    # Movement to up 
                    if event.key == K_UP:
                        self.snake.move_up()
                    
                    # Movement to down
                    if event.key == K_DOWN:
                        self.snake.move_down()  
                    
                        
                elif event.type == QUIT:
                    running = False

# Creating a game object  
game = Game()
game.run()
