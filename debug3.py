import pygame
import ephem
import datetime


class Observatorio:
	def __init__(self):
		self.observador = ephem.Observer()

	def getFechaActual(self):
		# Obtener la fecha y hora actual
		fecha_hora_actual = datetime.datetime.now()

		# Formatear la fecha y hora actual
		fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")

		return fecha_hora_formateada

	def getFechaActualDate(self):
		# Obtener la fecha y hora actual
		fecha_hora_actual = datetime.datetime.now()

		return fecha_hora_actual

	def getFechaActualUTC(self):
		# Obtener la fecha y hora actual en formato UTC
		fecha_hora_actual_utc = datetime.datetime.utcnow()

		# Formatear la fecha y hora actual en formato UTC
		fecha_hora_formateada_utc = fecha_hora_actual_utc.strftime("%Y-%m-%d %H:%M:%S")

		return fecha_hora_formateada_utc

	def getFechaActualUTCDate(self):
		# Obtener la fecha y hora actual en formato UTC
		fecha_hora_actual_utc = datetime.datetime.utcnow()

		return fecha_hora_actual_utc

	def setGeoLatLong(self,lat,lon):
		self.observador.lat = lat
		self.observador.lon = lon

	def setGeoDate(self,fecha_ingresada):
		self.observador.date = ephem.Date(fecha_ingresada)

	def computeMoonCoords(self):
		self.astro = ephem.Moon()
		self.astro.compute(self.observador)

	def getActualAzimut(self):
		azimut = self.astro.az
		azimut_degrees = ephem.degrees(azimut) # Conversion de Radianes a Grados
		return azimut_degrees

	def getActualAltitud(self):
		altitud = self.astro.alt
		altitud_degrees = ephem.degrees(altitud) # Conversion de Radianes a Grados
		return altitud_degrees

	def getActualAzimutRad(self):
		azimut = self.astro.az
		return azimut.real

	def getActualAltitudRad(self):
		altitud = self.astro.alt
		return altitud.real





Obs1 = Observatorio()
Obs1.setGeoLatLong(lat='-34.36',lon='-58.26')

fecha = Obs1.getFechaActualDate()
HoraIni = datetime.time(0, 0, 0)
fechaN = datetime.datetime.combine(fecha, HoraIni)

azimutArr = []
altitudArr = []
altRadArr = []
azRadArr = []
fechas = []

#Estadistica de la posicion de la luna en el transcurso del dia actual
for i in range(0,24):
	print("Horas Transcurridos : "+str(i))
	print(str(fechaN) + " UTC")
	fechaAuxLocal = fechaN - datetime.timedelta(hours=3)
	print(str(fechaAuxLocal) + " LocalTime")
	Obs1.setGeoDate(fecha_ingresada=fechaN)

	Obs1.computeMoonCoords()

	azimutCad = str(Obs1.getActualAzimut())
	
	altitudCad = str(Obs1.getActualAltitud())
	

	fechas.append(fechaAuxLocal)
	azimutArr.append(azimutCad.split(':'))
	altitudArr.append(altitudCad.split(':'))
	
	print("Altitud = " + altitudCad)
	print("Azimut = " + azimutCad)
	altR = str(Obs1.getActualAltitudRad())
	azR = str(Obs1.getActualAzimutRad())
	print("Altitud R = " + altR)
	print("Azimut R = " + azR)
	
	auxAlt = altitudCad.split(':')
	if int(auxAlt[0]) > 0 :
		altRadArr.append(altR)
		azRadArr.append(azR)

	print("")

	fechaN = fechaN + datetime.timedelta(hours=1)



#Prueba de Grafica


import numpy as np
import matplotlib.pyplot as plt

def grados_minutos_segundos_a_decimal(grados, minutos, segundos):
    return grados + minutos / 60 + segundos / 3600

def polar_to_cartesian(azimut_grados, altitud_grados, azimut_minutos, azimut_segundos, altitud_minutos, altitud_segundos):
    # Convertir azimut y altitud a grados decimales
    azimut_decimal = grados_minutos_segundos_a_decimal(azimut_grados, azimut_minutos, azimut_segundos)
    altitud_decimal = grados_minutos_segundos_a_decimal(altitud_grados, altitud_minutos, altitud_segundos)

    # Convertir de grados a radianes
    azimut_radianes = np.radians(azimut_decimal)
    altitud_radianes = np.radians(90 - altitud_decimal)  # Convertir altitud a ángulo cenital

    # Calcular coordenadas cartesianas
    x = altitud_radianes * np.cos(azimut_radianes)
    y = altitud_radianes * np.sin(azimut_radianes)
    return x, y

# Puntos de ejemplo relacionados con la posición lunar

azimut_grados = []  # Azimut en grados
azimut_minutos = []  # Azimut en minutos
azimut_segundos = []  # Azimut en segundos
altitud_grados = []   # Altitud en grados
altitud_minutos = []   # Altitud en minutos
altitud_segundos = []   # Altitud en segundos

"""
for i in range(len(azimutArr)):
	azimut_grados.append(int(azimutArr[i][0]))  # Azimut en grados
	azimut_minutos.append(float(azimutArr[i][1]))  # Azimut en minutos
	azimut_segundos.append(float(azimutArr[i][2]))  # Azimut en segundos

for i in range(len(altitudArr)):
	altitud_grados.append(int(altitudArr[i][0]))   # Altitud en grados
	altitud_minutos.append(float(altitudArr[i][1]))   # Altitud en minutos
	altitud_segundos.append(float(altitudArr[i][2]))   # Altitud en segundos
"""
for i in range(24):
	if (int(altitudArr[i][0]))>=0:
		azimut_grados.append(int(azimutArr[i][0]))  # Azimut en grados
		azimut_minutos.append(float(azimutArr[i][1]))  # Azimut en minutos
		azimut_segundos.append(float(azimutArr[i][2]))  # Azimut en segundos

		altitud_grados.append(int(altitudArr[i][0]))   # Altitud en grados
		altitud_minutos.append(float(altitudArr[i][1]))   # Altitud en minutos
		altitud_segundos.append(float(altitudArr[i][2]))   # Altitud en segundos



# Convertir coordenadas polares a cartesianas
coordenadas = []
for azimut_g, altitud_g, azimut_m, altitud_m, azimut_s, altitud_s in zip(azimut_grados, altitud_grados, azimut_minutos, altitud_minutos, azimut_segundos, altitud_segundos):
    x, y = polar_to_cartesian(azimut_g, altitud_g, azimut_m, azimut_s, altitud_m, altitud_s)
    coordenadas.append((x, y))

"""
j = 0
for i in coordenadas:
	print(str(i[1])+" = "+str(altRadArr[j]))
	print(str(i[0])+" = "+str(azRadArr[j]))
	print()
	j += 1
"""

# Configuración de Pygame
pygame.init()

ANCHO = 600
ALTO = 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
FUENTE = pygame.font.SysFont("Arial", 24)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Posición Lunar")

reloj = pygame.time.Clock()

terminado = False
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True

    pantalla.fill(BLANCO)
    
    # Dibujar la circunferencia
    pygame.draw.circle(pantalla, NEGRO, (ANCHO // 2, ALTO // 2), 160, 1)
    
    # Dibujar los puntos
    i=0
    for punto in coordenadas:
        x = int(punto[0] * 100 + ANCHO // 2)
        y = int(punto[1] * 100 + ALTO // 2)
        #x = int(float(altRadArr[i]) * 100 + ANCHO // 2)
        #y = int(float(azRadArr[i]) * 100 + (ALTO // 2)-400)
        pygame.draw.circle(pantalla, NEGRO, (x, y), 5)

    # Mostrar etiquetas de tiempo
        etiqueta = FUENTE.render(fechas[i].strftime("%H:%M"), True, NEGRO)
        pantalla.blit(etiqueta, (x + 10, y - 10))
        i += 1

    
    

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
