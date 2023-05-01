# importa biblioteques:
import time
import lib.BMP280 as bmp280  # arxiu BMP280 que hem creat dins la carpeta lib
import logging  # biblioteca per gestionar el traspàs de dades

# creacio del loger per les dades dins el directori logs: 
logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/bmp.log')    # ruta relativa de larxiu on es desaran les dades
fh.setLevel(logging.INFO)
# format de les dades a l’arxiu: dades temporals (data i hora) + dades definides al while True
formatter = logging.Formatter('%(asctime)s|%(message)s|', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

# configuracio:
sensor = bmp280.BMP280()  # definicio de l'objecte BMP280 amb el nom sensor

try:
  while True:
    temperatura=sensor.get_temperature() # retorna la temperatura en C
    pressio=sensor.get_pressure() # retorna la pressio en hPa
    logger.info(str(temperatura) + "|" + str(pressio)) #traspas de dades en format string
    print ("temperatura: %s C \t \t pressio: %s hPa \t \t altitud: %s m" % (temperatura, pressio, altitud))
    time.sleep(1)

except:
  print("execucio interrompuda")
