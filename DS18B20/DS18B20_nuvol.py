import time
from w1thermsensor import W1ThermSensor
import logging
import thingspeak

logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/dbs.log')    
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s|%(message)s|', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

sensor = W1ThermSensor() 
canal = thingspeak.Channel(‘IDcanal’, ‘WriteAPIkey’) # canal definit per la seva ID i Write API key

try:
  while True:
	temperatura = round(sensor.get_temperature(),2)  
	logger.info(str(temperatura))   
	print ("la temperatura es %s C" % temperatura)  
	dada_nubol = canal.update ({1:temperatura}); # puja el valor de la variables al camp 1 del canal definit
	time.sleep(1)	
except:
  print ("execucio interrompuda")
