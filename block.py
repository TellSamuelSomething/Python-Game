import pygame

class Block:
    def __init__(self, xposition, yposition, color, name, id):
        self.id = id
        self.size = 50
        self.xposition = xposition
        self.yposition = yposition
        self.color = color
        self.name = name

    #Function name: Create dirt block
    #Description: This function draws the dirt block at the specified place and keeps track of the user square's position and keeps
    # it out of its own boundaries. This creates the illusion that the user square can't pass the dirt block. 
    # COMMENT: all the object speed addition are to keep the objects float-value to not make the object bug through the dirtblock.
    #Returns: Nothing. Just the draws and controlles the blocks boundaries for the player and other obstacles.
    def create(self, screen, object):
        #Draw block
        pygame.draw.rect(screen, self.color, (self.xposition, self.yposition, self.size, self.size))
        #Check its boundaries
        self.boundaries(object)
    
    #Function name: boundaries
    #Description: This function controles that nothing can pass the blocks borders. Creating the illusion that it is a 2D square object.
    #Returns: Nothing. Just controles the objects position that interacts with the blocks. So that it can't pass it.
    def boundaries(self, object):
        #For horizontal boundaries
        #Right side
        if(self.hit(object) == 0):
            object.xposition = max((self.xposition + self.size), object.xposition)
        #Left side
        elif(self.hit(object) == 1):
            object.xposition = max(0, min(self.xposition - object.size, object.xposition))
        #For vertical boundaries
        #Up side
        elif(self.hit(object) == 2):
            object.yposition = max(0, min(object.yposition, self.yposition - object.size))
        #Down side
        elif(self.hit(object) == 3):
            object.yposition = max(self.yposition + self.size, object.yposition)
            #If the square hits the roof then instantly reverse the jumping process.
            if object.jump_hitroof == False:
                object.jump_hitroof = True
    
    #Function name: top_parameters
    #Description: This class is primerily for controling if the player is stadning on any of the current created blocks in the game.
    #Returns: True if player (square class) is on top of the block. False if it isn't.
    def top_parameters(self, object):
        if object.yposition == self.yposition - object.size and object.xposition >= self.xposition - object.size  and object.xposition <= self.xposition + object.size:
            return True
        else:
            return False

    #Function name: hit
    #Description: This function controles all the parameters of the block class. This is usefull for all other classes that may need to interact with -
    #the block during the games progress. For exampel if you want something to repel on it or not to be able to walk through it.
    #the parameters set for the if-statments are within the blocks side borders and a small window inside of its wall and outside of its wall. I had to do this because of the float values that aren't completely on point in python.
    #what this means is that when you want to compare two different float values with eachother they may not always be the same even if they're suppose to mathmatically. Python seems to not be exactly on point with calculating d decimal numbers.
    #Returns: A number between 0 and 3. These four different numbers determines which side of the block the object has hit. If it isn't touching any side, return None.
    def hit(self, object):
        #For horizontal boundraries
        #Right side boundarie
        if(object.xposition >= self.xposition + self.size - 3*object.speed_x and object.xposition <= self.xposition + self.size + 3*object.speed_x and object.yposition >= self.yposition - object.size - 3*object.vertical_start_speed and object.yposition <= self.yposition + self.size + 3*object.vertical_start_speed):
            #print("hit right side")
            return 0
        #Left side
        elif(object.xposition <= self.xposition - object.size + 3*object.speed_x and object.xposition >= self.xposition - object.size - 3*object.speed_x and object.yposition >= self.yposition - object.size - 3*object.vertical_start_speed and object.yposition <= self.yposition + self.size + 3*object.vertical_start_speed):
            #print("hit left side")
            return 1
        #For vertical boundaries
        #Up side
        elif(object.yposition <= self.yposition - object.size - 3*object.vertical_start_speed and object.yposition >= self.yposition - object.size + 3*object.vertical_start_speed and object.xposition >= self.xposition - object.size + 2*object.speed_x and object.xposition <= self.xposition + self.size - 2*object.speed_x):
            #print("hit up side")
            return 2
        #Down side
        elif(object.yposition >= self.yposition + self.size + 3*object.vertical_start_speed and object.yposition <= self.yposition + self.size - 3*object.vertical_start_speed and object.xposition >= self.xposition - object.size + 2*object.speed_x and object.xposition <= self.xposition + self.size - 2*object.speed_x):
            #print("hit down side")
            return 3
        
        return None