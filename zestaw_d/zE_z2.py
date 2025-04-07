import RPi.GPIO as GPIO
import time

odczyt_pin = 18
GPIO.setmode(GPIO.BCM)

def natezenie(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    
    start=time.time()
    while GPIO.input(pin) == GPIO.LOW:
        pass
    return time.time() - start

try:
    while True:
        poziom_oswietlenia = natezenie(odczyt_pin)
        print("Poziom oswietlenia", poziom_oswietlenia)
        time.sleep(2)
except KeyboardInterrupt:
    print("koniec pomiarow")
    GPIO.cleanup()
    
#Poziom oswietlenia 2.002716064453125e-05
#Poziom oswietlenia 2.3603439331054688e-05
#Poziom oswietlenia 2.384185791015625e-05
#Poziom oswietlenia 2.2172927856445312e-05
#Poziom oswietlenia 2.8848648071289062e-05
#Poziom oswietlenia 2.288818359375e-05
#Poziom oswietlenia 2.5033950805664062e-05
#Poziom oswietlenia 2.2411346435546875e-05
#Poziom oswietlenia 2.4318695068359375e-05
#Poziom oswietlenia 3.528594970703125e-05
#Poziom oswietlenia 2.193450927734375e-05