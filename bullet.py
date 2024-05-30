import pygame

class Bullet:
    def __init__(self, recent_direction, square_ypos, square_xpos, square_size, SCREEN_WIDTH):
        self.DIRECTION = recent_direction # 1 for right -1 for left
        self.speed_x = 0.4
        self.vertical_start_speed = -0.1
        self.yposition = square_ypos + square_size/2
        self.xposition = square_xpos
        self.width = 14
        self.height = 8
        self.size = 14 #Lazy added variable for other classes hit functions which uses size as a overall variable name.
        self.color = (255, 0, 0) # Color
        self.flying = False # might not be needed
        self.square_size = square_size
        self.SCREEN_WIDTH = SCREEN_WIDTH

        self.test = 0

    def bullet_draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.xposition, self.yposition, self.width, self.height))

    def fly(self, screen):
        #Draw bullet
        self.bullet_draw(screen)
        #Then if square faces right. Go right with the amount of bullet speed. Else go left.
        if(self.DIRECTION == 1): # for left
            self.xposition += self.speed_x
        elif(self.DIRECTION == -1): # for right
            self.xposition -= self.speed_x
                
    def hit_removal(self):
        pass
    

            
