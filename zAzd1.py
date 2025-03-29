from gpiozero import LED
from time import sleep

led_zolty = LED(4)
led_czerwony = LED(27)
led_zielony = LED(22)
while True:
	led_zolty.on()
	print("on")
	sleep(1)
	led_zolty.off()
	print("off")
	sleep(1)

	led_czerwony.on()
	print("on")
	sleep(1)
	led_czerwony.off()
	print("off")
	sleep(1)

	led_zielony.on()
	print("on")
	sleep(1)
	led_zielony.off()
	print("off")
	sleep(1)
