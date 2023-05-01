import time
from w1thermsensor import W1ThermSensor
import logging  # biblioteca per gestionar el traspàs de dades

# creacio del loger per les dades: 
logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/dbs.log')    # ruta relativa de larxiu on es desaran les dades
fh.setLevel(logging.INFO)
# format de les dades a l’arxiu: dades temporals (data i hora) + dades definides al while True
formatter = logging.Formatter('%(asctime)s|%(message)s|', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

sensor = W1ThermSensor() 

try:
  while True:
	temperatura = round(sensor.get_temperature(),2)  # canviem el format de la  variable: arrodonim amb 2 decimals 
	logger.info(str(temperatura))   # dades a desar en larxiu definit ('logs/dbs.log') en format string (text)
	print ("la temperatura es %s C" % temperatura)  
	time.sleep(1)	# interval actualitzacio de dades 1s
except:
  print ("execucio interrompuda")
