# importa biblioteques:
import time
from w1thermsensor import W1ThermSensor
import logging
import thingspeak

# creacio del logger per les dades:
logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/dsb2.log') # cal actualitzar el fitxer de recepcio de les dades   
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s|%(message)s|', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

# configuració:
sensor = W1ThermSensor()  # definició de l'objecte W1ThermSensor amb el nom sensor
temperatura = []  # llista buida en que desarem les temperatures dels 2 sensors
canal = thingspeak.Channel(‘IDcanal’, ‘WriteAPIkey’) # canal definit per la seva ID i Write API key

# execució en condicions normals
try:
  while True: 
      for sensor in W1ThermSensor.get_available_sensors():
         temperatura.append (round(sensor.get_temperature(),2))  

      print (temperatura)
      logger.info (str(temperatura[0]) + “|” str(temperatura[1]))
      # envia les dades als canals 1 i 2 de thingspeak
      dada_nubol = canal.update ({1:temperatura[0], 2:temperatura[1]});
      temperatura.clear()   
      time.sleep(1)

# quan es produeixi una excepció, com Ctrl+C, l’execució sortirà del bucle anterior i ...
except:
  print ("execucio interrompuda")
