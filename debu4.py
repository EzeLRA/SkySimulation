import pygame
import numpy as np
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

# Crear una instancia de la clase Observatorio
Obs1 = Observatorio()
Obs1.setGeoLatLong(lat='-34.6037',lon='-58.3816')

# Calcular las coordenadas de la Luna para distintos momentos del día
azimutArr = []
altitudArr = []
fechas = []

fecha = Obs1.getFechaActualDate()
HoraIni = datetime.time(0, 0, 0)
fechaN = datetime.datetime.combine(fecha, HoraIni)

for i in range(24):
    Obs1.setGeoDate(fecha_ingresada=fechaN)
    Obs1.computeMoonCoords()

    azimutArr.append(Obs1.getActualAzimut())
    altitudArr.append(Obs1.getActualAltitud())
    fechas.append(fechaN)

    fechaN += datetime.timedelta(hours=1)

# Convertir las coordenadas polares a cartesianas
coordenadas_x = []
coordenadas_y = []

for azimutAct, altitudAct in zip(azimutArr, altitudArr):
    azimut_grados, azimut_minutos, azimut_segundos = azimutAct.split(':')
    altitud_grados, altitud_minutos, altitud_segundos = altitudAct.split(':')

    x, y = polar_to_cartesian(int(azimut_grados), int(altitud_grados), float(azimut_minutos), float(azimut_segundos), float(altitud_minutos), float(altitud_segundos))
    coordenadas_x.append(x)
    coordenadas_y.append(y)

# Configurar Pygame
ANCHO = 800
ALTO = 800
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
FUENTE = pygame.font.SysFont(None, 24)

pygame.init()
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
    pygame.draw.circle(pantalla, NEGRO, (ANCHO // 2, ALTO // 2), 200, 1)

    # Dibujar los puntos y sus etiquetas de tiempo
    for i in range(len(coordenadas_x)):
        x = int(coordenadas_x[i] * 200 + ANCHO // 2)
        y = int(coordenadas_y[i] * 200 + ALTO // 2)
        pygame.draw.circle(pantalla, NEGRO, (x, y), 5)

        # Mostrar etiquetas de tiempo
        etiqueta = FUENTE.render(fechas[i].strftime("%H:%M"), True, NEGRO)
        pantalla.blit(etiqueta, (x + 10, y - 10))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
