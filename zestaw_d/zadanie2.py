import RPi.GPIO as GPIO
import time

PIR_PIN = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("Czekam na ruch...")
i = 0

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Wykrylem ruch")
            time.sleep(5)
            print("Czekam na ruch...")
        
        i += 1
        time.sleep(0.5)
        print(i)

except KeyboardInterrupt:
  print("Koniec odczytu")
  GPIO.cleanup() 
