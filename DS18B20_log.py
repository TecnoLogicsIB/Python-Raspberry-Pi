import time
from w1thermsensor import W1ThermSensor
import logging

#Creacio del loger per les dades
logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/dallasdata.log')    # ruta de larxiu on es desaran les dades
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s|%(message)s|', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

sensor  =  W1ThermSensor()

try:
  while True:
    temperatura = round(sensor.get_temperature(),2)  # temperatura arrodonida amb 2 decimals
    print ("la temperatura es %s C" % temperatura)  #imprimeix al terminal
    logger.info(temperatura)   # dades a desar en larxiu definit ('logs/dallasdata.log')
    time.sleep(1)
except:
  print ("execucio interrompuda")
