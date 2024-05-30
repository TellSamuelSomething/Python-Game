import pygame
import sys
from bullet import Bullet
from obstacle import Obstacle
from grenate import Grenate

class Actions:
    def __init__(self):
        self.spacebar_pressed = False
        self.g_pressed = False
        self.Keys = pygame.key.get_pressed()
        self.event = pygame.event.get()
        self.bullet_list = []
        self.grenate_list = []

        self.grenate_ammo = 2
        self.bullet_ammo = 3
        
    def call_key(self):
        self.Keys = pygame.key.get_pressed()

    def shoot(self, map, square, obstacle):
        if self.bullet_ammo > 0: # Control that the player cant use more than the given amount of ammo
            if(self.Keys[pygame.K_SPACE] and self.spacebar_pressed == False):
                self.bullet_ammo = self.bullet_ammo - 1 # Decrease ammo
                self.spacebar_pressed = True
                bullet = Bullet(square.facing_direction, square.yposition, square.xposition, square.size, map.SCREEN_WIDTH)
                self.bullet_list.append(bullet)
            
            if(not self.Keys[pygame.K_SPACE] and self.spacebar_pressed == True):
                self.spacebar_pressed = False
        
        #Animate all the bullets and delete them if they touch the wall
        for index, bullet in enumerate(self.bullet_list):
            #Draw bullet and animate its movement
            bullet.fly(map.SCREEN)
            #Delete the bullet if it touches the end of the screen (wall)
            if(bullet.xposition <= 0 or bullet.xposition >= (map.SCREEN_WIDTH - bullet.width)):
                del self.bullet_list[index]
            for i, block in enumerate(obstacle.iceblock_list):
                if block.hit(bullet) != None:
                    del self.bullet_list[index]
            for j, block in enumerate(obstacle.dirtblock_list):
                if block.hit(bullet) != None:
                    del self.bullet_list[index]
            for k, block in enumerate(obstacle.lavablock_list):
                if block.hit(bullet) != None:
                    del self.bullet_list[index]
            
    
    def throw_grenate(self, square, map, obstacle):
        if self.grenate_ammo > 0: # Control that the player cant use more than the given amount of ammo
            if self.Keys[pygame.K_g] and self.g_pressed == False:
                self.grenate_ammo = self.grenate_ammo - 1 # Decrease ammo
                self.g_pressed = True
                grenate = Grenate()
                self.grenate_list.append(grenate)
            
            if not self.Keys[pygame.K_g] and self.g_pressed == True:
                self.g_pressed = False

        for index, grenate in enumerate(self.grenate_list):
            grenate.timer()
            if self.grenate_list[index].time_out == False:
                grenate.throw(map, square, obstacle)
            #Set timer and explode and delete after 3 seconds
            if self.grenate_list[index].time_out == True:
                if grenate.explode(map.SCREEN) == True:
                    del self.grenate_list[index]
        
