import ephem
import datetime
import numpy as np

def degress_minutes_seconds_to_decimal(degress, minutes, seconds):
    return degress + minutes / 60 + seconds / 3600

def polar_to_cartesian(azimut_degress, altitud_degress, azimut_mins, azimut_segs, altitud_mins, altitud_segs):
    # Convertir azimut y altitud a grados decimales
    azimut_decimal = degress_minutes_seconds_to_decimal(azimut_degress, azimut_mins, azimut_segs)
    altitud_decimal = degress_minutes_seconds_to_decimal(altitud_degress, altitud_mins, altitud_segs)

    # Convertir de grados a radianes
    azimut_radians = np.radians(azimut_decimal)
    altitud_radians = np.radians(90 - altitud_decimal)  # Convertir altitud a ángulo cenital

    # Calcular coordenadas cartesianas
    x = altitud_radians * np.cos(azimut_radians)
    y = altitud_radians * np.sin(azimut_radians)
    return x, y