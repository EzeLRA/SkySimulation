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
azimut_grados = [45, 90, 180, 270]  # Azimut en grados
azimut_minutos = [0, 0, 0, 0]  # Azimut en minutos
azimut_segundos = [0, 0, 0, 0]  # Azimut en segundos
altitud_grados = [45, 60, 30, 50]   # Altitud en grados
altitud_minutos = [0, 0, 0, 0]   # Altitud en minutos
altitud_segundos = [0, 0, 0, 0]   # Altitud en segundos

# Convertir coordenadas polares a cartesianas
coordenadas_x = []
coordenadas_y = []
for azimut_g, altitud_g, azimut_m, altitud_m, azimut_s, altitud_s in zip(azimut_grados, altitud_grados, azimut_minutos, altitud_minutos, azimut_segundos, altitud_segundos):
    x, y = polar_to_cartesian(azimut_g, altitud_g, azimut_m, altitud_m, azimut_s, altitud_s)
    coordenadas_x.append(x)
    coordenadas_y.append(y)

# Dibujar la circunferencia
circunferencia = plt.Circle((0, 0), 1, color='b', fill=False)
plt.gca().add_patch(circunferencia)

# Dibujar los puntos
plt.scatter(coordenadas_x, coordenadas_y, color='red')

# Etiquetas y títulos
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Puntos relacionados con la posición lunar')

# Ajustes de visualización
plt.axis('equal')
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.grid(True)

# Mostrar el gráfico
plt.show()
