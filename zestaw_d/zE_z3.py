from gpiozero import LED
import RPi.GPIO as GPIO
import time

odczyt_pin = 18
GPIO.setmode(GPIO.BCM)
led_zielony = LED(17)
led_zielony.off()

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
        if poziom_oswietlenia < 0.000025:
            led_zielony.on()
        else:
            led_zielony.off()
        time.sleep(2)
except KeyboardInterrupt:
    print("koniec pomiarow")
    GPIO.cleanup()
    
    
#Poziom oswietlenia 1.9073486328125e-05
#Poziom oswietlenia 2.4080276489257812e-05
#Poziom oswietlenia 8.860978364944458
#Poziom oswietlenia 2.47955322265625e-05
#Poziom oswietlenia 2.4557113647460938e-05
#Poziom oswietlenia 2.5987625122070312e-05
#Poziom oswietlenia 2.3365020751953125e-05
#Poziom oswietlenia 2.005791187286377
#Poziom oswietlenia 2.3126602172851562e-05
#Poziom oswietlenia 2.5510787963867188e-05
#Poziom oswietlenia 2.7894973754882812e-05
#Poziom oswietlenia 2.4318695068359375e-05
#Poziom oswietlenia 2.6702880859375e-05
#Poziom oswietlenia 2.5510787963867188e-05
#Poziom oswietlenia 2.5510787963867188e-05