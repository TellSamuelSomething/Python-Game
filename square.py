import pygame
from actions import Actions

class Square:

    # Function __init__: Here all the square's default varibles are set.
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.facing_direction = 1 # -1 for square facing left and 1 for facing right. Which side it faces is determined by which way it recently walked in a horizontal direction
        self.speed_x = 0.15
        self.size = 50
        self.player_color = (0, 0, 255)
        self.xposition = (SCREEN_WIDTH - self.size)/2
        self.yposition = (SCREEN_HEIGHT - self.size)

        self.walking = False
        self.on_ice = False # important boolean value to control if the player is on a ice_block or not.
        self.sliding = False
        self.horizontal_vector = self.speed_x #For sliding effect

        self.vertical_start_speed = -0.7 # Reglate this variable to change the vectors starting value. NOTE: make sure this value stays negative to not screw up the boundaries functions.
        self.jump_vector = self.vertical_start_speed
        self.jump_gravity = 0.001

        #self.jump_up = False
        self.jump_process = False 
        self.jump_hitroof = False #Control if the square hits the underside of a block
        self.hitground = False #Control if the square has hit the maps ground parameter
        self.on_iceblock = False #Control if the square hits a block on its topside or not
        self.on_dirtblock = False
        #self.on_lavablock = False
        self.UPkey_pressed = False
        self.falling = False
        
    def jump_function(self, keys):
        # Press upkey and start jump sequence
        if keys[pygame.K_UP] and self.jump_process == False and self.UPkey_pressed == False and self.falling == False:
            self.UPkey_pressed = True
            self.jump_process = True
            self.hitground = False
            self.on_iceblock = False
            self.on_dirtblock = False
        # This part is so that the player needs to release the up button before it can jump again
        if (not keys[pygame.K_UP]):
            self.UPkey_pressed = False
        #Start jump process. Until cancel properties are met.
        if(self.jump_process == True):
            self.yposition = self.yposition + self.jump_vector
            self.jump_vector = self.jump_vector + self.jump_gravity
            #When roof hit. Change vector direction. The other and statment for vector <= 0 is so that it can only be done once during a jumping process.
            if self.jump_hitroof == True and self.jump_vector <= 0:
                self.jump_vector = self.jump_vector * (-1)
            #Restart
            if self.jump_vector > 0: # This extra if statement is for not making the square teleport to the block surface when it touches its side during its jump process.
                if self.hitground == True or self.on_iceblock == True or self.on_dirtblock == True:
                    self.jump_process = False
                    self.jump_hitroof = False
                    self.jump_vector = self.vertical_start_speed

        #print("j pr: ", self.jump_process, "hitground: ", self.hitground, "on_block", self.on_block)
        #Gravity. Fall when it has nothing to stand on and isn't jumping.
        if(self.jump_process == False and self.hitground == False and self.on_iceblock == False and self.on_dirtblock == False):
            self.falling = True
            self.yposition = self.yposition - self.vertical_start_speed
        else:
            self.falling = False

    # Function move_left: Make the square move to the left if the LEFT-key is pressed
    # Description: When K_LEFT command is activated through pygame library then square x_position is subtrakted with minus x_speed for every frame the key is held. 
    # The facing direction variable for the square is also changed to (-1) for other applications.
    # The maps horizontal size is set through the left to right.
    def move_horizontally(self, keys):
        #Right key pressed to move right
        if keys[pygame.K_RIGHT]:
            self.facing_direction = 1 # 1 for right
            self.xposition += self.speed_x
            self.walking = True #Boolean to control if the square is moving horizontally or not for other classes in the game
        #Left key pressed to move left
        elif keys[pygame.K_LEFT]:
            self.facing_direction = -1 # -1 for left
            self.xposition -= self.speed_x 
            self.walking = True #Boolean to control if the square is moving horizontally or not for other classes in the game
        # To reset the walking boolean for the other two move sections
        elif self.walking == True:
            self.walking = False

    # Function draw_rectangel: Draws the square on the screen with its given settings
    # Description: The square is drawned on the playing screen with help of the screen variable from the map class.
    def draw_player(self, map):
        pygame.draw.rect(map.SCREEN, self.player_color, (self.xposition, self.yposition, self.size, self.size))
    
    def screen_boundaries(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.xposition = max(0, min(SCREEN_WIDTH - self.size, self.xposition))
        self.yposition = max(0, min(SCREEN_HEIGHT - self.size, self.yposition))
        # If player hits the maps roof. Set the hit_roof boolean to true to cancel jump up process.
        if self.yposition <= 0:
            self.jump_hitroof = True
        # Trigger hit ground boolean for jumping function process. Which ends the jumping process.
        if self.yposition == SCREEN_HEIGHT - self.size and self.hitground == False:
            self.hitground = True