import pygame
from block import Block

class Obstacle:
    def __init__(self):
        #Lists for obstacles
        self.iceblock_list = []
        self.dirtblock_list = []
        self.lavablock_list = []
        self.block_id = 0
        #For sliding function for the iceblocks
        self.friction = 0.00015 #Friction variable to decrease the slide effect of the iceblock within the slide function.
        self.reset = False
        
    #Function: place_obstacles
    #Description:
    def place_obstacles(self, screen, square):
        #Create all iceblocks
        for iceblock in self.iceblock_list:
            iceblock.create(screen, square)
        #For controlling sliding parameters: NOTE: I made this part of the program to negate the not sliding on the left side of the square problem. I think this solution is very ugly tho.
        if square.on_dirtblock == False:
            for iceblock in self.iceblock_list:
                if iceblock.top_parameters(square) == False:
                    square.on_ice = False
                    square.on_iceblock = False
                elif iceblock.top_parameters(square) == True:
                    square.on_ice = True
                    square.on_iceblock = True
                    break
        
        #If player square is on ice then this follows.
        if square.on_ice == True:
            self.slide(square)
        
        #Create all dirtblocks
        for dirtblock in self.dirtblock_list:
            dirtblock.create(screen, square)
        #Control if player is on any of the dirtblocks
        if square.on_iceblock == False: # So that the false value reapears after its set to true for the iceblock on block control.
            for dirtblock in self.dirtblock_list:
                if dirtblock.top_parameters(square) == False:
                    square.on_dirtblock = False
                elif dirtblock.top_parameters(square) == True:
                    square.on_dirtblock = True
                    break
        
        #Create all lavablocks and control their melt (losing hit property).
        for lavablock in self.lavablock_list:
            lavablock.create(screen, square)
        for lavablock in self.lavablock_list:
            if lavablock.hit(square) != None:
                pygame.quit()
        
    #Function: build iceblokcs
    #Description: This function let the user place mutliple block in a straight line from start to the right or start to upwards.
    #0 for right and 1 for up.
    def build_iceblocks(self, xposition, yposition, amount, right_or_up):
        for index in range(amount):
            block = Block(xposition, yposition, (0, 191, 255), "ice_block", self.block_id) #Makes it the color light blue.
            self.iceblock_list.append(block)
            #0 for right
            if(right_or_up == 0):
                xposition += block.size
            #1 for up
            elif(right_or_up == 1):
                yposition += block.size
            #increase id number
            self.block_id = self.block_id + 1

    #Function: build dirtblocks
    #Description: This function let the user place mutliple block in a straight line from start to the right or start to upwards.
    #0 for right and 1 for up.
    def build_dirtblocks(self, xposition, yposition, amount, right_or_up):
        for index in range(amount):
            block = Block(xposition, yposition, (139, 69, 19), "dirt_block", self.block_id) #Makes it the color brown.
            self.dirtblock_list.append(block)
            #0 for right
            if(right_or_up == 0):
                xposition += block.size
            #1 for up
            elif(right_or_up == 1):
                yposition -= block.size
            #increase id number
            self.block_id = self.block_id + 1
    
    def build_lavablocks(self, xposition, yposition, amount, right_or_up):
        for index in range(amount):
            block = Block(xposition, yposition, (255, 80, 0), "lava_block", self.block_id) #Makes it the color dark orange.
            self.lavablock_list.append(block)
            #0 for right
            if(right_or_up == 0):
                xposition += block.size
            #1 for up
            elif(right_or_up == 1):
                yposition -= block.size
            #increase id number
            self.block_id = self.block_id + 1

    #Function:
    #Description:
    def delete_obstacles(self):
        for block in self.iceblock_list:
            del block
        for block in self.dirtblock_list:
            del block

    #Function slide: Makes the player square slide for a small amount when ontop of a icecube.
    def slide(self, object):
        # Controls if the square is walking or not through its own walking function.
        if object.walking == True and self.reset == False:
            self.reset = True
            object.sliding = False
        elif object.walking == False and self.reset == True:
            self.reset = False
            object.sliding = True 
        # Makes the square slide in its last faced direction
        if object.facing_direction == 1 and object.walking == False and object.sliding == True:
            object.xposition += object.horizontal_vector 
            object.horizontal_vector -= self.friction
        elif object.facing_direction == -1 and object.walking == False and object.sliding == True:
            object.xposition += -object.horizontal_vector
            object.horizontal_vector -= self.friction
        # Make the square stop sliding after its vector is below zero or it moves away from the ice surface.
        if object.horizontal_vector <= 0 or object.walking == True and self.reset == True: 
            object.horizontal_vector = object.speed_x
            object.sliding = False
            self.reset == False
    