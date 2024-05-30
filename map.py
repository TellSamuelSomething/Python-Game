import pygame
import sys

class Map:
    # Function __init__: Sets the default settings for the screen
    # Description: 
    def __init__(self):
        # Square properties
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def hit_borders(self, object):
        #Go through all the maps borders
        #return 0 for horizontal touch. return 1 for bottom hit. return 2 for up hit.
        #Horizontal borders
        if object.xposition >= self.SCREEN_WIDTH - object.size or object.xposition <= object.size:
            return 0
        #Vertical borders
        #Bottom map border
        elif object.yposition >= self.SCREEN_HEIGHT - object.size:
            return 1
        #Up map border
        elif object.yposition <= object.size:
            return 2
        
        return None
    
    