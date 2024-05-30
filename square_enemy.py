import pygame

class Square_enemy:
    #This enemy will be a walking enemy. Meaning it will stick to the ground. It will either stand still or walk back and fourth horizontally.
    def __init__(self, xposition, yposition, walk_distance):
        self.size = 50
        self.color = (50, 255, 0)
        self.xposition = xposition
        self.yposition = yposition
        self.vertical_start_speed = -0.1
        self.distance = walk_distance
        self.current_distance = 0
        self.speed_x = 0.1
        self.goal = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.xposition, self.yposition, self.size, self.size))
    
    #Always first walks to the right side then to the left. And the repeat the process
    def walk(self):
        if self.distance != 0:
            if self.current_distance < self.distance and self.goal == False:
                self.xposition = self.xposition + self.speed_x
                self.current_distance = self.current_distance + self.speed_x
            else:
                self.goal = True
            
            if self.goal == True:
                self.xposition = self.xposition - self.speed_x
                self.current_distance = self.current_distance - self.speed_x
            if self.current_distance <= 0 and self.goal == True:
                self.goal = False

    def hit(self, object):
        if(object.xposition >= self.xposition - object.size and object.xposition <= self.xposition + self.size and object.yposition >= self.yposition - object.size and object.yposition <= self.yposition + self.size):
            return True

    def grenate_hit(self, object):
        if (object.xposition + object.size) >= self.xposition - object.start_size and (object.xposition + object.start_size - object.size) <= self.xposition + self.size and (object.yposition + object.size) >= self.yposition - object.start_size and (object.yposition + object.start_size - object.size) <= self.yposition + self.size:
            return True
    
