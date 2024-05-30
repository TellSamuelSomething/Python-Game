import pygame

class Circle_enemy:
    def __init__(self, xposition, yposition, fly_distance, dive_distance):
        self.xposition = xposition
        self.yposition = yposition
        self.dive_distance = dive_distance
        self.fly_distance = fly_distance
        self.current_fly_distance = 0
        self.current_dive_distance = 0
        self.goal = False
        self.dive_margin = 10

        self.size = 30
        self.hit_box = 40
        self.color = (50, 255, 0)

        self.vertical_start_speed = 0.2
        self.speed_x = 0.06
        self.diving = False
        self.dive_up = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.xposition, self.yposition), self.size, width=0)
    
    #Always first walks to the right side then to the left. And the repeat the process
    def fly(self, square):

        self.dive(square)

        if self.fly_distance != 0 and self.diving == False:
            if self.current_fly_distance < self.fly_distance and self.goal == False:
                self.xposition = self.xposition + self.speed_x
                self.current_fly_distance = self.current_fly_distance + self.speed_x
            else:
                self.goal = True
            
            if self.goal == True:
                self.xposition = self.xposition - self.speed_x
                self.current_fly_distance = self.current_fly_distance - self.speed_x
            if self.current_fly_distance <= 0 and self.goal == True:
                self.goal = False
    
    def dive(self, square):
        if square.xposition >= self.xposition - self.size - self.dive_margin and square.xposition <= self.xposition + self.size + self.dive_margin and square.yposition > self.yposition + self.size:
            self.diving = True
        
        if self.diving == True:
            if self.current_dive_distance < self.dive_distance and self.dive_up == False:
                self.yposition = self.yposition + self.vertical_start_speed
                self.current_dive_distance = self.current_dive_distance + self.vertical_start_speed
            else:
                self.dive_up = True
            
            if self.dive_up == True:
                self.yposition = self.yposition - self.vertical_start_speed
                self.current_dive_distance = self.current_dive_distance - self.vertical_start_speed

                if self.current_dive_distance <= 0:
                    self.dive_up = False
                    self.diving = False
    
    def hit(self, object):
        if(object.xposition >= self.xposition - object.size - self.hit_box and object.xposition <= self.xposition + self.hit_box and object.yposition >= self.yposition - object.size - self.hit_box and object.yposition <= self.yposition + self.hit_box):
            return True

    def grenate_hit(self, object):
        if (object.xposition + object.size) >= self.xposition - object.start_size and (object.xposition + object.start_size - object.size) <= self.xposition + self.size and (object.yposition + object.size) >= self.yposition - object.start_size and (object.yposition + object.start_size - object.size) <= self.yposition + self.size:
            return True
            