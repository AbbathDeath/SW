import Adafuit_DHT
import time

czujnik = Adafruit_DHT_DHT11
sygnal = 4

while True:
    wilg, temp = Adafruit_DHT.read_retry(czujnik, sygnal)
    if wilg is not None and temp is not None:
        print(f"Temperatura {temp}")
        print(f"Wilgotnosc {wilg}")
    else:
        print("Brak odczytu")
    time.sleep(2)
    