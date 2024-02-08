from geopy.geocoders import Nominatim

# Dirección del lugar del que deseas obtener las coordenadas
direccion_lugar = "Buenos Aires, Argentina"

# Crear un objeto geolocalizador
geolocalizador = Nominatim(user_agent="myGeocoder")

# Obtener la ubicación (coordenadas) del lugar
ubicacion_lugar = geolocalizador.geocode(direccion_lugar)

# Imprimir la latitud y longitud del lugar
print("Coordenadas de", direccion_lugar)
print("Latitud:", ubicacion_lugar.latitude)
print("Longitud:", ubicacion_lugar.longitude)
