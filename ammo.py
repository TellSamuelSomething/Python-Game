import pygame

class Ammo:
    def __init__(self, color, xposition, yposition, name):
        self.name = name
        self.color = color
        self.xposition = xposition
        self.yposition = yposition
        self.width = 12
        self.height = 18
        self.size = 12
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), (self.xposition, self.yposition, self.width + 1, self.height + 1))
        pygame.draw.rect(screen, self.color, (self.xposition, self.yposition, self.width, self.height))
    
    def hit(self, player):
        #For horizontal boundraries
        #Right side boundarie
        if(player.xposition >= self.xposition + self.size - 3*player.speed_x and player.xposition <= self.xposition + self.size + 3*player.speed_x and player.yposition >= self.yposition - player.size - 3*player.vertical_start_speed and player.yposition <= self.yposition + self.size + 3*player.vertical_start_speed):
            return True
        #Left side
        elif(player.xposition <= self.xposition - player.size + 3*player.speed_x and player.xposition >= self.xposition - player.size - 3*player.speed_x and player.yposition >= self.yposition - player.size - 3*player.vertical_start_speed and player.yposition <= self.yposition + self.size + 3*player.vertical_start_speed):
            return True
        #For vertical boundaries
        #Up side
        elif(player.yposition <= self.yposition - player.size - 3*player.vertical_start_speed and player.yposition >= self.yposition - player.size + 3*player.vertical_start_speed and player.xposition >= self.xposition - player.size - 3*player.speed_x and player.xposition <= self.xposition + self.size + 3*player.speed_x):
            return True
        #Down side
        elif(player.yposition >= self.yposition + self.size - 3*player.vertical_start_speed and player.yposition <= self.yposition + self.size + 3*player.vertical_start_speed and player.xposition >= self.xposition - player.size - 3*player.speed_x and player.xposition <= self.xposition + self.size + 3*player.speed_x):
            return True
        else:
            False