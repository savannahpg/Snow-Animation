"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from random import *


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTSTEELBLUE = (176,196,222)
PLUM = (221, 160, 221)
PINK =	(255, 192, 203)



#lists & variables
colorlist = [WHITE, LIGHTSTEELBLUE, PLUM, PINK]
colorlen=len(colorlist)
actualcolor = randint(0,colorlen-1)











pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


# Your SnowFlake class
class Snowflake ():
	def __init__(self, positionx, positiony, xspeed, yspeed, size, color):  
		self.x_location = positionx
		self.y_location = positiony 
		self.x_speed = xspeed
		self.y_speed = yspeed 
		self.size = size
		self.color = color
		
	def movement (self, screen, speed, direction):
		
		self.x_location += self.x_speed 
		self.y_location += self.y_speed 
		
		

		
	def draw(self):
		pygame.draw.circle(screen, colorlist[actualcolor], [self.x_location, self.y_location], self.size)
		
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 3

# Snow List
snow_list = []




# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(BLACK)


    # --- Drawing code should go here
    # Begin Snow
	
	positionx = randint(0, 700)
	positiony = randint(0, 0)
	randspeedx = randint (0, 0)
	randspeedy = randint (0, 5)
	flake = Snowflake(positionx, positiony, randspeedx, randspeedy, 2, colorlist[actualcolor])
	snow_list.append(flake)
	
	for flake in (snow_list):
		flake.draw()
		flake.movement(screen, randspeedx, 180)
    
 

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
