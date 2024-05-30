import pygame
from ammo import Ammo

class Accessories:
    def __init__(self):
        self.bullet_color = (255, 255, 0)
        self.bullet_size = 10

        self.grenate_color = (0, 0, 0)
        self.grenate_size = 14

        self.ammo_list = []


    def draw_bullet_score(self, map, actions):
        if actions.bullet_ammo >= 3:
            pygame.draw.circle(map.SCREEN, (0, 0, 0), (750, 50), self.bullet_size + 4)
            pygame.draw.circle(map.SCREEN, self.bullet_color, (750, 50), self.bullet_size)
        if actions.bullet_ammo >= 2:
            pygame.draw.circle(map.SCREEN, (0, 0, 0), (720, 50), self.bullet_size + 4)
            pygame.draw.circle(map.SCREEN, self.bullet_color, (720, 50), self.bullet_size)
        if actions.bullet_ammo >= 1:
            pygame.draw.circle(map.SCREEN, (0, 0, 0), (690, 50), self.bullet_size + 4)
            pygame.draw.circle(map.SCREEN, self.bullet_color, (690, 50), self.bullet_size)

    def draw_grenate_score(self, map, actions):
        if actions.grenate_ammo >= 2:
            pygame.draw.circle(map.SCREEN, self.grenate_color, (50, 50), self.grenate_size)
        if actions.grenate_ammo >= 1:
            pygame.draw.circle(map.SCREEN, self.grenate_color, (90, 50), self.grenate_size)
    
    def place_bullet_ammo(self, xposition, yposition):
        ammo = Ammo(self.bullet_color, xposition, yposition, "bullet") #Yellow
        self.ammo_list.append(ammo)
    
    def place_grenate_ammo(self, xposition, yposition):
        ammo = Ammo(self.grenate_color, xposition, yposition, "grenate") #Black
        self.ammo_list.append(ammo)
    
    def ammo_interact(self, screen, actions, square):
        for index, ammo in enumerate(self.ammo_list):
            ammo.draw(screen)
            if ammo.hit(square) == True and ammo.name == "grenate":
                actions.grenate_ammo = 2
                del self.ammo_list[index]
            if ammo.hit(square) == True and ammo.name == "bullet":
                actions.bullet_ammo = 3
                del self.ammo_list[index]
