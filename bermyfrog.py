#! /usr/bin/evn python
import pygame , sys
import pygame.locals as pg
import time

#slow motion replays

pygame.init()

####### GLOBAL VARIABLES
# x = row
# y = column
#SCREENSIZE = 
SCREENSIZE = (800, 800) #800 horizontal, 600 vertical
ROWS = 10
COLUMNS = 10

ZONE = pygame.display.set_mode( ( SCREENSIZE[0] , SCREENSIZE[1]) )
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (50, 50, 0)



######## define classes
class Frog():
	global ZONE
	def __init__(self, color = GREEN, pos = [10, 10]):
		self.pos = pos
#		self.cordinate = [
		self.size = [10, 10]
		self.color = color
	def display(self):
		pygame.draw.rect(ZONE, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1] ) )



class Road():
	def __init__(self):
		self.pos = [0, SCREENSIZE[1]-100]
		self.size = [800, 50]
		self.color = BROWN
	def display(self):
		pygame.draw.rect(ZONE, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1] ) )

class Vehicle():
	global ZONE
	def __init__(self, color = GREEN, pos = [10, 10]):
		self.pos = pos
#		self.cordinate = [
		self.size = [20, 10]
		self.color = color
	def display(self):
		pygame.draw.rect(ZONE, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1] ) )





####### define functions



def main():
	
	ZONE.fill(BLACK)
	road.display()	
	frog.display()	
	redfrog.display()
	car.display()
	
	#frog.pos = [50, 50]
	pygame.display.update()
	
	mod_x = 0
	mod_y = 0	
	left_mod_x = 0
	left_mod_y = 0	


	keys = pygame.key.get_pressed()
	if keys[ pygame.K_RIGHT ] : mod_x = 10
	elif keys[ pygame.K_LEFT ] : mod_x = -10
	elif keys[ pygame.K_UP ] : mod_y = -10
	elif keys[ pygame.K_DOWN ] : mod_y = 10
	else : mod_x = mod_y = 0

	frog.pos = [frog.pos[0]+mod_x, frog.pos[1]+mod_y]
	redfrog.pos = [redfrog.pos[0]+mod_x, redfrog.pos[1]+mod_y]


	keysleft = pygame.key.get_pressed()
	if keysleft[ pygame.K_d ] : left_mod_x = 10
	elif keysleft[ pygame.K_a ] : left_mod_x = -10
	elif keysleft[ pygame.K_w ] : left_mod_y = -10
	elif keysleft[ pygame.K_s ] : left_mod_y = 10
	else : left_mod_x = left_mod_y = 0
	
	frog.pos = [frog.pos[0]+left_mod_x*-1, frog.pos[1]+left_mod_y*-1]
	redfrog.pos = [redfrog.pos[0]+left_mod_x, redfrog.pos[1]+left_mod_y]

	if car.pos[0] > 800 : car.pos[0] = 0
	car.pos = [car.pos[0]+3, car.pos[1]]
	
	for event in pygame.event.get() :
		if event.type == pg.QUIT :
			pygame.quit()
			sys.exit()



####### create objects
frog = Frog(color = GREEN, pos = [500, 500])
redfrog = Frog(color = WHITE, pos = [400, 400])
car = Vehicle(color = RED, pos = [0, 700])

road = Road()
tick_time = 1000 * time.time()



###### start program

while True :
	now = 1000 * time.time()
	
	
	# comment
	if now - tick_time > 10:
		main()
		tick_time = 1000 * time.time()


