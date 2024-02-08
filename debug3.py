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





Obs1 = Observatorio()
Obs1.setGeoLatLong(lat='-34.6037',lon='-58.3816')

fecha = Obs1.getFechaActualDate()
HoraIni = datetime.time(0, 0, 0)
fechaN = datetime.datetime.combine(fecha, HoraIni)



#Estadistica de la posicion de la luna en el transcurso del dia actual
for i in range(0,24):
	print("Horas Transcurridos : "+str(i))
	print(fechaN)
	Obs1.setGeoDate(fecha_ingresada=fechaN)

	Obs1.computeMoonCoords()
	
	print("Azimut = "+str(Obs1.getActualAzimut()))
	print("Altitud = "+str(Obs1.getActualAltitud()))
	print("")

	fechaN = fechaN + datetime.timedelta(hours=1)
