#! /usr/bin/env python
import pygame , sys
import pygame.locals as pg
import time

import globals
from timer import Timer
from frog import Frog
from road import Road
from vehicle import Vehicle
from bang import Bang

pygame.init()

ZONE = pygame.display.set_mode([globals.WIDTH , globals.HEIGHT])
pygame.display.set_caption('Bermy Frog!')


def main():
    
    ZONE.fill(globals.BLACK)
    road1.display()
    road2.display()
    road3.display()
    
    frog.display()  
    frog2.display()
    car.display()
    car2.display()

    #flash screen during collisions
    if frog.collision == 1:
        bang.display()
    if frog2.collision == 1:
        bang2.display()
    #frog.pos = [50, 50]
    pygame.display.update()
    
    mod_x = 0
    mod_y = 0   
    left_mod_x = 0
    left_mod_y = 0  

    #monitor arrow keys to move frog1
    keys = pygame.key.get_pressed()
    if keys[ pygame.K_RIGHT ] : mod_x = 10
    elif keys[ pygame.K_LEFT ] : mod_x = -10
    elif keys[ pygame.K_UP ] : mod_y = -10
    elif keys[ pygame.K_DOWN ] : mod_y = 10
    else : mod_x = mod_y = 0

    frog.pos = [frog.pos[0]+mod_x, frog.pos[1]+mod_y]
    #frog2.pos = [frog2.pos[0]+mod_x, frog2.pos[1]+mod_y]

    #monitor WASD keys to move frog2
    keysleft = pygame.key.get_pressed()
    if keysleft[ pygame.K_d ] : left_mod_x = 10
    elif keysleft[ pygame.K_a ] : left_mod_x = -10
    elif keysleft[ pygame.K_w ] : left_mod_y = -10
    elif keysleft[ pygame.K_s ] : left_mod_y = 10
    else : left_mod_x = left_mod_y = 0
    
    #frog.pos = [frog.pos[0]+left_mod_x*-1, frog.pos[1]+left_mod_y*-1]
    frog2.pos = [frog2.pos[0]+left_mod_x, frog2.pos[1]+left_mod_y]

    #if cars drive off screen, wrap around
    if car.pos[0] > globals.WIDTH : car.pos[0] = 0
    if car2.pos[0]+car2.size[0] < 0 : car2.pos[0] = globals.WIDTH

    #move cars across screen
    car.pos = [car.pos[0]+3, car.pos[1]]
    car2.pos = [car2.pos[0]-3, car2.pos[1]]

    #wrap frog1 around the screen
    #alternative, make a barrier
    if frog.pos[0] > globals.WIDTH : frog.pos[0] = 0
    if frog.pos[0] < 0 : frog.pos[0] = globals.WIDTH
    if frog.pos[1] > globals.HEIGHT : frog.pos[1] = 0
    if frog.pos[1] < 0 : frog.pos[1] = globals.HEIGHT
    
    #basic collision detection
    #frog1 position is within scope of vehicle positions
    if ( ( (car.pos[0] < frog.pos[0] < car.pos[0]+car.size[0]) & (car.pos[1] < frog.pos[1] < car.pos[1]+car.size[1]) ) | 
    ( (car.pos[0] < frog.pos[0]+frog.size[0] < car.pos[0]+car.size[0]) & (car.pos[1] < frog.pos[1]+frog.size[1] < car.pos[1]+car.size[1]) ) ) :
        frog.collision = 1
    elif ( ( (car2.pos[0] < frog.pos[0] < car2.pos[0]+car2.size[0]) & (car2.pos[1] < frog.pos[1] < car2.pos[1]+car2.size[1]) ) | 
    ( (car2.pos[0] < frog.pos[0]+frog.size[0] < car2.pos[0]+car2.size[0]) & (car2.pos[1] < frog.pos[1]+frog.size[1] < car2.pos[1]+car2.size[1]) ) ) :
        frog.collision = 1
    else:
        frog.collision = 0

    #frog2 position is within scope of vehicle positions
    if ( ( (car.pos[0] < frog2.pos[0] < car.pos[0]+car.size[0]) & (car.pos[1] < frog2.pos[1] < car.pos[1]+car.size[1]) ) | 
    ( (car.pos[0] < frog2.pos[0]+frog2.size[0] < car.pos[0]+car.size[0]) & (car.pos[1] < frog2.pos[1]+frog2.size[1] < car.pos[1]+car.size[1]) ) ) :
        frog2.collision = 1
    elif ( ( (car2.pos[0] < frog2.pos[0] < car2.pos[0]+car2.size[0]) & (car2.pos[1] < frog2.pos[1] < car2.pos[1]+car2.size[1]) ) | 
    ( (car2.pos[0] < frog2.pos[0]+frog2.size[0] < car2.pos[0]+car2.size[0]) & (car2.pos[1] < frog2.pos[1]+frog2.size[1] < car2.pos[1]+car2.size[1]) ) ) :
        frog2.collision = 1
    else:
        frog2.collision = 0


    for event in pygame.event.get() :
        if event.type == pg.QUIT :
            pygame.quit()
            sys.exit()




####### create objects
frog = Frog(color = globals.GREEN, pos = [globals.WIDTH/2-10, globals.HEIGHT-25])
frog2 = Frog(color = globals.WHITE, pos = [globals.WIDTH/2+50, globals.HEIGHT-25])
car = Vehicle(color = globals.RED, pos = [0, globals.HEIGHT-95])
car2 = Vehicle(color = globals.BLUE, pos = [0, globals.HEIGHT-300])
bang = Bang(color = globals.GREEN)
bang2 = Bang(color = globals.WHITE)
road1 = Road(pos = [0, globals.HEIGHT-150])
road2 = Road(pos = [0, globals.HEIGHT-300])
road3 = Road(pos = [0, globals.HEIGHT-500])


###### start program

# Setup the main loop timer.
main_timer = Timer()

while True :

    # If the time since the last tick is more than 10 milliseconds.
    if main_timer.get_ticktime() > 10:
        main()

        # Tick the timer to reset it.
        main_timer.tick()

