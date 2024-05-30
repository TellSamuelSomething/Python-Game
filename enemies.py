import pygame
import sys
from square_enemy import Square_enemy
from circle_enemy import Circle_enemy

class Enemies:
    def __init__(self):
        self.square_enemy_list = []
        self.circle_enemy_list = []

    def create_square_enemy(self, xposition, yposition, walk_distance):
        enemy = Square_enemy(xposition, yposition, walk_distance)
        self.square_enemy_list.append(enemy)

    def use_square_enemy(self, screen, actions, square):
        for i, enemy in enumerate(self.square_enemy_list):
            enemy.draw(screen)
            enemy.walk()
            
            if enemy.hit(square) == True:
                pygame.quit()

            for j, grenate in enumerate(actions.grenate_list):
                if enemy.grenate_hit(actions.grenate_list[j]) == True and actions.grenate_list[j].time_out == True:
                    del self.square_enemy_list[i]

            for u, bullet in enumerate(actions.bullet_list):
                if enemy.hit(actions.bullet_list[u]) == True:
                    del self.square_enemy_list[i]
                    del actions.bullet_list[u]
    
    def create_circle_enemy(self, xposition, yposition, fly_distance, dive_distance):
        enemy = Circle_enemy(xposition, yposition, fly_distance, dive_distance)
        self.circle_enemy_list.append(enemy)

    def use_circle_enemy(self, screen, actions, square):
        for i, enemy in enumerate(self.circle_enemy_list):
            enemy.draw(screen)
            enemy.fly(square)
            
            if enemy.hit(square) == True:
                pygame.quit()

            for j, grenate in enumerate(actions.grenate_list):
                if enemy.grenate_hit(actions.grenate_list[j]) == True and actions.grenate_list[j].time_out == True:
                    del self.circle_enemy_list[i]

            for u, bullet in enumerate(actions.bullet_list):
                if enemy.hit(actions.bullet_list[u]) == True:
                    del self.circle_enemy_list[i]
                    del actions.bullet_list[u]