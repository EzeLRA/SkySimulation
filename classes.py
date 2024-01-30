from config import *
import pygame as pg
import sys

# Principal Object
class Object:
	def __init__(self,ScreenDisplay,coords,typeObject):
		self.typeClass = typeObject
		self.screen = ScreenDisplay
		self.posX = coords[0]
		self.posY = coords[1]
		if self.typeClass == PLANET:
			self.scale = 5
			self.color = "BROWN"
		elif self.typeClass == STAR:
			self.scale = 2
			self.color = "YELLOW"
		elif self.typeClass == UNKNOW:
			self.scale = 3
			self.color = "GREY"

	def run(self):
		pg.draw.circle(self.screen,self.color,[self.posX,self.posY],self.scale)




# Circle Border
class CircleBorder:
	def __init__(self,ScreenDisplay):
		self.centerCoords = [(WIN_SIZE_PREDEFINED[0] / 2)-150,WIN_SIZE_PREDEFINED[1] / 2]
		self.screen = ScreenDisplay
		self.borderSize = 1
		self.radius = self.centerCoords[0] - 50

	def cuadrantsDraw(self):
		circlesRadius = self.radius
		for i in range(0,5):
			pg.draw.circle(self.screen,"WHITE",self.centerCoords,circlesRadius,self.borderSize)
			circlesRadius -= 50


	def axisDraw(self):
		coordsX1 = [self.centerCoords[0] - self.radius,self.centerCoords[1]]
		coordsX2 = [self.centerCoords[0] + self.radius,self.centerCoords[1]]
		pg.draw.line(self.screen,"WHITE",coordsX1,coordsX2,1)
		coordsY1 = [self.centerCoords[0],self.centerCoords[1] - self.radius]
		coordsY2 = [self.centerCoords[0],self.centerCoords[1] + self.radius]
		pg.draw.line(self.screen,"WHITE",coordsY1,coordsY2,1)

	def run(self):
		CircleBorder.cuadrantsDraw(self)
		CircleBorder.axisDraw(self)
		pg.draw.circle(self.screen,"WHITE",self.centerCoords,self.radius,self.borderSize)


# Principal Structure
class EscenaryInit:
	def __init__(self,win_size):
		# init pygame modules
		pg.init()
		# window size
		self.screen = pg.display.set_mode(win_size)
		
		# Objets init
		self.border = CircleBorder(self.screen) 
		self.object1 = Object(self.screen,self.border.centerCoords,PLANET)
		# clock
		self.clock = pg.time.Clock()
		

	def check_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
				pg.quit()
				sys.exit()

	def render(self):
		self.screen.fill("BLACK")
		
		#Objects Running
		self.border.run()
		self.object1.run()

		# swap buffers
		pg.display.flip()


	def get_time(self):
		self.time = pg.time.get_ticks() * 0.001

	def run(self):
		while True:
			self.get_time()
			self.check_events()
			self.render()
			self.delta_time = self.clock.tick(60)