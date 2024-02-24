from config import *
import pygame as pg
import sys
import ephem
import datetime

#
# Objects (Astros) class
#

class Object:
	def __init__(self,ScreenDisplay,coords,typeObject):
		# Classifies Objects
		self.typeClass = typeObject
		# Actual Using Window
		self.screen = ScreenDisplay
		# Coords for the actual object
		self.posX = coords[0]
		self.posY = coords[1]

		# Sets Color type for the actual object
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





#
# Principal Observer Class:
#

class Observatory:
	def __init__(self):
		self.actualObserver = ephem.Observer()

	#
	# Computing Funtions
	#
	
	def computeMoonCoords(self):
		# Init moon coords with the actual parameters seted in the actual observatory
		self.astro = ephem.Moon()
		self.astro.compute(self.actualObserver)

	#
	# Seters Functions
	#

	def setGeoLatLong(self,lat,lon):
		# Set determinated location for the observatory
		self.actualObserver.lat = lat
		self.actualObserver.lon = lon

	def setGeoDate(self,ingresedDate):
		# Set a determinated Date Time for the observatory
		self.actualObserver.date = ephem.Date(ingresedDate)

	#
	# Geters Functions
	#

	def getActualAzimutDegrees(self):
		azimut = self.astro.az
		azimut_degrees = ephem.degrees(azimut) # Radians to Degrees
		return azimut_degrees

	def getActualAltitudDegrees(self):
		altitud = self.astro.alt
		altitud_degrees = ephem.degrees(altitud) # Radians to Degrees
		return altitud_degrees

	def getActualAzimutRadians(self):
		azimut = self.astro.az
		return azimut.real

	def getActualAltitudRadians(self):
		altitud = self.astro.alt
		return altitud.real

	def getActualDate(self):
		# Actual Local Date
		actualDate = datetime.datetime.now()
		return actualDate

	def getActualUTCDate(self):
		# Actual UTC Date format
		actualUTCDate = datetime.datetime.utcnow()
		return actualUTCDate




#
# Circle Border Class
#

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



#
# Escenary Estructure Class (Init)
#

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

		Obs1 = Observatory()
		Obs1.setGeoLatLong(lat='-34.36',lon='-58.26')
		Obs1.setGeoDate(Obs1.getActualUTCDate())
		Obs1.computeMoonCoords()
		print(Obs1.getActualDate())
		print(Obs1.getActualAltitudDegrees())
		print(Obs1.getActualAzimutDegrees())
		print(Obs1.getActualAltitudRadians())
		print(Obs1.getActualAzimutRadians())
		

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