import pygame


class Levels:
    def __init__(self) -> None:
        self.enemies = 0 #Set amount of enemies that needs to be killed during the level
        self.place = True
        self.enemies_dead = False
        self.next_map = False
        self.current_level = 1
        self.zero_index = 0

        
    def level_1(self, obstacle, accessories, enemies, square):
        #Determine position and amount of blocks
        if self.place == True and self.current_level == 1:
            #First large middle floor
            obstacle.build_dirtblocks(200, 400, 1, 0)
            obstacle.build_dirtblocks(600, 400, 1, 0)
            obstacle.build_dirtblocks(250, 350, 7, 0)
            enemies.create_square_enemy(250, 300, 300)

            #Left floor section
            obstacle.build_dirtblocks(0, 200, 3, 0)
            obstacle.build_dirtblocks(100, 150, 3, 1)
            #obstacle.build_dirtblocks(100, 180, 1, 1)
            enemies.create_square_enemy(20, 150, 0)

            #Right floor section
            obstacle.build_dirtblocks(650, 200, 3, 0)
            accessories.place_grenate_ammo(740, 180)

            #Quit placement section for non iterable blocks or stuff on same position
            self.place = False

        if len(enemies.square_enemy_list) == 0 and self.current_level == 1:
            self.reset(obstacle, accessories, enemies, square, 2)
                
    def level_2(self, obstacle, accessories, enemies, square):
        #Determine position and amount of blocks
        if self.place == True and self.current_level == 2:
            #lowest left dirt section
            obstacle.build_dirtblocks(100, 550, 3, 0)
            obstacle.build_dirtblocks(150, 500, 2, 0)
            obstacle.build_dirtblocks(150, 450, 3, 0)
            obstacle.build_dirtblocks(200, 400, 2, 0)
            
            #lowest right dirt section
            obstacle.build_dirtblocks(600, 550, 3, 0)
            obstacle.build_dirtblocks(550, 500, 2, 0)
            enemies.create_square_enemy(300, 550, 250)
            enemies.create_square_enemy(250, 550, 300)
            
            #Right up side of dirtblocks. With ammo on it.
            obstacle.build_dirtblocks(650, 150, 3, 0)
            accessories.place_bullet_ammo(730, 125)

            #Left up side with iceblocks
            obstacle.build_iceblocks(0, 200, 4, 0)
            enemies.create_square_enemy(100, 150, 0)

            #over ice section
            obstacle.build_iceblocks(300, 300, 3, 0)
            obstacle.build_iceblocks(550, 300, 2, 0)

            #Quit placement section for non iterable blocks or stuff on same position
            self.place = False
        
        if len(enemies.square_enemy_list) == 0  and self.current_level == 2:
            self.reset(obstacle, accessories, enemies, square, 3)

    def level_3(self, obstacle, accessories, enemies, square):
        #Determine position and amount of blocks
        if self.place == True and self.current_level == 3:
            #lowest left dirt section
            obstacle.build_dirtblocks(100, 550, 3, 0)
            obstacle.build_dirtblocks(150, 500, 2, 0)
            obstacle.build_dirtblocks(200, 450, 1, 0)
            
            #lowest right dirt section
            obstacle.build_dirtblocks(600, 550, 3, 0)
            obstacle.build_dirtblocks(600, 500, 2, 0)
            obstacle.build_dirtblocks(600, 450, 1, 0)
            
            #Middle ice 
            obstacle.build_iceblocks(250, 350, 2, 0)
            obstacle.build_iceblocks(450, 350, 3, 0)

            #Lowest lava part
            obstacle.build_lavablocks(250, 550, 7, 0)
            
            #Flying enemy over middle ice field
            enemies.create_circle_enemy(250, 250, 300, 120)

            #Up right dirt part
            obstacle.build_dirtblocks(600, 200, 4, 0)
            obstacle.build_dirtblocks(650, 250, 3, 0)
            enemies.create_square_enemy(600, 150, 160)

            #Upper left dirt section
            obstacle.build_dirtblocks(0, 150, 3, 0)
            accessories.place_bullet_ammo(100, 120)

            #Quit placement section for non iterable blocks or stuff on same position
            self.place = False
        
        if len(enemies.square_enemy_list) == 0 and self.current_level == 2:
            self.reset(obstacle, accessories, enemies, square, 4)
        
    def level_4(self, obstacle, accessories, enemies, square):
        #Determine position and amount of blocks
        if self.place == True and self.current_level == 3:
            

            #Quit placement section for non iterable blocks or stuff on same position
            self.place = False
        
        if len(enemies.square_enemy_list) == 0 and self.current_level == 2:
            self.reset(obstacle, accessories, enemies, square, 5)

    def reset(self, obstacle, accessories, enemies, square, next_level):
        if square.xposition >= 750: #Map size on x parameter - 50 (player width size).
            while self.zero_index < len(obstacle.dirtblock_list): # regular for-loop doesnt seem to delete all blocks.
                del obstacle.dirtblock_list[self.zero_index]

            while self.zero_index < len(obstacle.iceblock_list): # regular for-loop doesnt seem to delete all blocks.
                del obstacle.iceblock_list[self.zero_index]

            for index, enemy in enumerate(enemies.square_enemy_list):
                del enemies.square_enemy_list[index]
            for index, ammo in enumerate(accessories.ammo_list):
                del accessories.ammo_list[index]
            
            #Reset start values
            self.place = True
            square.xposition = 0
            square.yposition = 550
            self.current_level = next_level
    