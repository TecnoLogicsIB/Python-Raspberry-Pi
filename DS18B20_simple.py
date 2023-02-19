# importa biblioteques
import time
from w1thermsensor import W1ThermSensor

# configuracio
sensor = W1ThermSensor()  # definicio de l'objecte W1ThermSensor

# execucio en condicions normals
try:
  while True:
    temperatura = sensor.get_temperature()  # obtencio directa de la temperatura en C
    print ("la temperatura es %s C" % temperatura)  # imprimeix el text i el valor
    time.sleep(1)    # interval actualitzacio de dades 1s

# quan es produeixi una excepcio, com Ctrl+C ...
except:
  print ("execucio interrompuda")
