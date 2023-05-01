# importa biblioteques:
import time
import lib.BMP280 as bmp280  # arxiu BMP280 que hem creat dins la carpeta lib

# configuracio:
sensor = bmp280.BMP280()  # definicio de l'objecte BMP280 amb el nom sensor

try:
  while True:
    temperatura=sensor.get_temperature()
    pressio=sensor.get_pressure()
    print("temperatura: %s C, pressio: %s hPa" % (temperatura, pressio))
    time.sleep(1)

except:
  print("execucio interrompuda")
