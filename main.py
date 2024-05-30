import pygame
import sys
from map import Map
from square import Square
from actions import Actions
from bullet import Bullet
from enemies import Enemies
from obstacle import Obstacle
from accessories import Accessories
from levels import Levels

# Initialize Pygame
pygame.init()

# Create class instances
map = Map()
square = Square(map.SCREEN_WIDTH, map.SCREEN_HEIGHT)
actions = Actions() # Has the keys actions inbuilt
bullet = Bullet(square.facing_direction, square.yposition, square.xposition, square.size, map.SCREEN_WIDTH)
obstacle = Obstacle()
accessories = Accessories()
enemies = Enemies()
levels = Levels()

#Notes: It seems like the combination of left + space + up keys are not possible on my computer. After trying to debugging this problem through checking all combinations through if-statments it just doesnt seem to work for some reason.
#
#
#
#

# Loop variables
place = True
running = True
# Main game loop
while running:
   
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Call for action key variable and update it for each iteration
    actions.call_key()

    # Fill the screen with white. IMPORTANT INFO!: This function where the screen gets filled in needs to be infront of the other drawned object calls
    map.SCREEN.fill((255, 255, 255))

    # Control ammo boundaries for the player and animate them
    accessories.ammo_interact(map.SCREEN, actions, square)

    #Animate enemies
    enemies.use_square_enemy(map.SCREEN, actions, square)
    enemies.use_circle_enemy(map.SCREEN, actions, square)

    # Animate the obstacles and control all their boundaries
    obstacle.place_obstacles(map.SCREEN, square)

    # Make the square move left or right horizontally if the left or right key is pressed. Utimetally changeing its x_position
    square.move_horizontally(actions.Keys)
    
    # Make the square jump if up key is pressed
    square.jump_function(actions.Keys)

    # Make the square shoot a small projectile when the space-bar is pressed
    actions.shoot(map, square, obstacle)

    #Throw grenate
    actions.throw_grenate(square, map, obstacle)
    
    # Keep the square within the screen boundaries
    square.screen_boundaries(map.SCREEN_WIDTH, map.SCREEN_HEIGHT)
    
    # PUT LEVELS HERE
    levels.level_1(obstacle, accessories, enemies, square)
    levels.level_2(obstacle, accessories, enemies, square)
    levels.level_3(obstacle, accessories, enemies, square)
    levels.level_4(obstacle, accessories, enemies, square)
    # Draw the square
    square.draw_player(map)

    #Animate the accessories
    accessories.draw_bullet_score(map, actions)
    accessories.draw_grenate_score(map, actions)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

#Function:
#Description: