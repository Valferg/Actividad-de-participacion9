from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        # Diccionario para mapear direcciones de viento a grados
        direccion_a_grados = {
            "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
            "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
            "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
            "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
        }

        # Variables para almacenar sumas parciales
        total_temp = 0
        total_hum = 0
        total_pres = 0
        total_vel_viento = 0
        dir_viento_grados = []

        # Contador para el número de registros
        count = 0

        with open(self.nombre_archivo, 'r') as file:
            for line in file:
                if line.startswith("Temperatura:"):
                    total_temp += float(line.split(":")[1])
                elif line.startswith("Humedad:"):
                    total_hum += float(line.split(":")[1])
                elif line.startswith("Presión:"):
                    total_pres += float(line.split(":")[1])
                elif line.startswith("Viento:"):
                    vel_dir = line.split(":")[1].strip().split(",")
                    total_vel_viento += float(vel_dir[0])
                    dir_viento_grados.append(direccion_a_grados[vel_dir[1]])
                count += 1

        # Calcular promedios
        prom_temp = total_temp / count
        prom_hum = total_hum / count
        prom_pres = total_pres / count
        prom_vel_viento = total_vel_viento / count

        # Calcular dirección predominante del viento
        prom_dir_viento_grados = sum(dir_viento_grados) / len(dir_viento_grados)
        # Buscar la dirección más cercana en grados
        dir_viento_predominante = min(direccion_a_grados, key=lambda x: abs(direccion_a_grados[x] - prom_dir_viento_grados))

        return prom_temp, prom_hum, prom_pres, prom_vel_viento, dir_viento_predominante

# Ejemplo de uso
archivo_ejemplo = "datos_meteorologicos.txt"
datos = DatosMeteorologicos(archivo_ejemplo)
resultado = datos.procesar_datos()
print("Temperatura promedio:", resultado[0])
print("Humedad promedio:", resultado[1])
print("Presión promedio:", resultado[2])
print("Velocidad promedio del viento:", resultado[3])
print("Dirección predominante del viento:", resultado[4])
