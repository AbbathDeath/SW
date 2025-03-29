from gpiozero import LED
from time import sleep

led_zolty = LED(4)
led_czerwony = LED(27)
led_zielony = LED(22)
while True:
	led.on()
	print("on")
	sleep(1)
	led.off()
	print("off")
	sleep(1)

