# importa biblioteques:
import time
import lib.BMP280 as bmp280  # arxiu BMP280 que hem creat dins la carpeta lib

# configuració:
sensor = bmp280.BMP280()  # definició de l'objecte BMP280 amb el nom sensor

try:    # execució en condicions normals
  while True:
	  temperatura = sensor.get_temperature()  # retorna la temperatura en C
    pressio = sensor.get_pressure()     # retorna la pressio en hPa
    print ("temperatura: %s C, pressio: %s hPa" % (temperatura, pressio))  # imprimeix 
    time.sleep(1)	# interval actualitzacio de dades 1s

except:    # quan es produeixi una excepció, com Ctrl+C, l’execució sortirà del bucle anterior
  print ("execucio interrompuda")
