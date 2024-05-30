import pygame
import time
from block import Block

class Grenate():
    def __init__(self):
        self.speed_x = 0.4
        self.horizontal_vector = 0.3
        self.vertical_start_speed = -0.4 # Make sure that this value stays negative to not ruin the boundarie functions
        self.vertical_vector = self.vertical_start_speed
        self.gravity = 0.001
        self.size = 6 # Radius = 6 pixels. Diameter = 12 px
        self.start_size = self.size
        self.color = (0,0,0) # Bullet color = Black

        self.xposition = 0
        self.yposition = 0

        self.start = False
        self.bounce_block_boolean = False
        self.touched_block_id = None
        self.bounce_wall_boolean = False
        
        self.fly_left = False
        self.fly_right = False

        self.duration = 2.5
        self.start_time = time.time() # Set time for when this class is created
        self.explotion_color = (150, 20, 0)
        self.time_out = False

        self.repelent_force = 0.7
        self.friction_force = 0.6

    def throw(self, map, square, obstacle):
        self.starting_position(square.facing_direction, square.xposition, square.yposition, square.size)
        #Draw the grenate at its current position
        self.draw(map.SCREEN)
        #Make the grenate fly
        self.fly()
        #Control bounce physics
        self.bounce(obstacle, map)

    def fly(self):
        #Flying horizontally
        if self.fly_left == True and self.start == True and self.horizontal_vector != 0:
            self.xposition = self.xposition - self.horizontal_vector
        elif self.fly_right == True and self.start == True and self.horizontal_vector != 0:
            self.xposition = self.xposition + self.horizontal_vector
        #Flying vertically
        if self.start == True and self.vertical_vector != 0:
            self.yposition = self.yposition + self.vertical_vector
            self.vertical_vector = self.vertical_vector + self.gravity
    
    def starting_position(self, facing_direction, xposition, yposition, size):
        #Choosing starting position. Right or left side of square.
        if facing_direction == 1 and self.start == False: # Throw to the right
            self.xposition = xposition + size
            self.yposition = yposition + size/2
            self.fly_right = True
            self.start = True
            
        elif facing_direction == -1 and self.start == False: # Throw to the left
            self.xposition = xposition
            self.yposition = yposition + size/2
            self.fly_left = True
            self.start = True

    def block_bounce(self, block_list: list[Block]):
        # Go through all the dirtblocks boundaries and checks if the grenate hits it on any of it sides through the dirtblocks hit function.
        for block in block_list:
            #For Right side
            if block.hit(self) == 0 and self.bounce_block_boolean == False:
                self.touched_block_id = block.id
                self.horizontal_vector = self.horizontal_vector * (-1) * self.repelent_force
                self.bounce_block_boolean = True
            #For left side
            elif block.hit(self) == 1 and self.bounce_block_boolean == False:
                self.touched_block_id = block.id
                self.horizontal_vector = self.horizontal_vector * (-1) * self.repelent_force
                self.bounce_block_boolean = True
            #For upside
            elif block.hit(self) == 2 and self.bounce_block_boolean == False:
                self.touched_block_id = block.id
                self.vertical_vector = self.vertical_vector * (-1) * self.repelent_force
                self.horizontal_vector = self.horizontal_vector * self.friction_force
                self.bounce_block_boolean = True
            #For downside
            elif block.hit(self) == 3 and self.bounce_block_boolean == False:
                self.touched_block_id = block.id
                self.vertical_vector = self.vertical_vector * (-1)
                self.bounce_block_boolean = True

            if block.hit(self) == None and block.id == self.touched_block_id: #Control that the loop is on the hitted block's id and set bounce boolean back to False once its no longer hitting the current block its on.
                self.bounce_block_boolean = False
                self.touched_block_id = None

            if block.hit == 0 or 1 or 2 or 3: # Control grenate boundaries towards the block
                self.block_boundaries(block)

    def screen_bounce(self, map):
        #Control maps borders and bouncing effect on it.
        if map.hit_borders(self) == 0 and self.bounce_wall_boolean == False: # For left or right
            self.horizontal_vector = self.horizontal_vector * (-1) * self.repelent_force
            self.bounce_wall_boolean = True
            self.touched_wall_id = 1

        elif map.hit_borders(self) == 1 and self.bounce_wall_boolean == False: # For bottom hit
            self.vertical_vector = self.vertical_vector * (-1) * self.repelent_force
            self.horizontal_vector = self.horizontal_vector * self.friction_force
            self.bounce_wall_boolean = True
            self.touched_wall_id = 2

        elif map.hit_borders(self) == 2 and self.bounce_wall_boolean == False: # For upper hit
            self.vertical_vector = self.vertical_vector * (-1)
            self.bounce_wall_boolean = True
            self.touched_wall_id = 3

        else:
            self.bounce_wall_boolean = False
        
        if map.hit_borders(self) == 0 or 1 or 2:
            self.screen_boundaries(map)

        
    def bounce(self, obstacle, map):
        # Bounce the dirt_blocks
        self.block_bounce(obstacle.dirtblock_list)
        # Bounce the ice_blocks
        self.block_bounce(obstacle.iceblock_list)
        # Bounce on screen
        self.screen_bounce(map)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.xposition, self.yposition), self.size, width=0)
    
    def timer(self):
        if time.time() - self.start_time > self.duration:
            self.time_out = True
    
    def explode(self, screen):
        if self.time_out == True:    
            self.color = self.explotion_color
            self.size = self.size + 0.4
            self.draw(screen)
            if self.size >= 80: #After hitting a certain size. Return true for deletion in obstacle class
                return True
            else:
                return False

    def block_boundaries(self, block):
        #For horizontal boundaries
        #Right side
        if(block.hit(self) == 0):
            self.xposition = max((block.xposition + block.size), self.xposition)
        #Left side
        elif(block.hit(self) == 1):
            self.xposition = max(0, min(block.xposition - self.size, self.xposition))
        #For vertical boundaries
        #Up side
        elif(block.hit(self) == 2):
            self.yposition = max(0, min(self.yposition, block.yposition - self.size))
        #Down side
        elif(block.hit(self) == 3):
            self.yposition = max(block.yposition + block.size, self.yposition)
    
    def screen_boundaries(self, map):
        self.xposition = max(0, min(map.SCREEN_WIDTH - self.size, self.xposition))
        self.yposition = max(0, min(map.SCREEN_HEIGHT - self.size, self.yposition))