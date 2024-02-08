import ephem

# Coordenadas geográficas de Buenos Aires: latitud y longitud en grados decimales
latitud_buenos_aires = '-34.6037'  # Latitud de Buenos Aires
longitud_buenos_aires = '-58.3816'  # Longitud de Buenos Aires

# Crear un observador para Buenos Aires
observador_buenos_aires = ephem.Observer()
observador_buenos_aires.lat = ephem.degrees(latitud_buenos_aires)  # Latitud en grados decimales
observador_buenos_aires.lon = ephem.degrees(longitud_buenos_aires)  # Longitud en grados decimales

# Fecha y hora específicas (en formato UTC)
fecha_hora = '2024/02/08 18:30:00'
observador_buenos_aires.date = ephem.Date(fecha_hora)

# Crear un objeto celestial (en este caso, el planeta Marte)
marte = ephem.Mars()

# Calcular la posición de Marte con respecto al observador de Buenos Aires
marte.compute(observador_buenos_aires)

# Obtener azimut y altura de Marte (en radianes)
azimut = marte.az
altura = marte.alt

# Convertir azimut y altura de radianes a grados
azimut_grados = ephem.degrees(azimut)
altura_grados = ephem.degrees(altura)

print("Azimut de Marte desde Buenos Aires:", azimut_grados)
print("Altura de Marte desde Buenos Aires:", altura_grados)
