import RPi.GPIO as GPIO
from gpiozero import Buzzer
import time

while True:
    try:
        print("nowy pomiar")
        time.sleep(1)
        GPIO.setmode(GPIO.BOARD)
        
        PIN_TRIGGER = 16
        PIN_ECHO = 12
        
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        
        print("czekam sensor")
        time.sleep(2)
        print("obliczam")
        
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        
        while GPIO.input(PIN_ECHO) == 0:
            # print("x")
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            # print("y")
            pulse_end_time = time.time()
            
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print(f"Dystans: {distance} cm")
    finally:
        GPIO.cleanup()
        
'''
abbath@raspberrypi:~/Desktop $ python3 C_zd1.py
nowy pomiar
czekam sensor
obliczam
Dystans: 29.61 cm
nowy pomiar
czekam sensor
obliczam
Dystans: 29.64 cm
nowy pomiar
czekam sensor
obliczam
Dystans: 3.95 cm
nowy pomiar
czekam sensor
obliczam
Dystans: 4.07 cm
nowy pomiar
czekam sensor
obliczam
Dystans: 36.11 cm
nowy pomiar
czekam sensor
obliczam
Dystans: 3.56 cm
nowy pomiar
czekam sensor
^Z
[3]+  Zatrzymano              python3 C_zd1.py
abbath@raspberrypi:~/Desktop $ ^C
abbath@raspberrypi:~/Desktop $ 

'''