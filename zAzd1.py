from gpiozero import LED
from time import sleep

led_zolty = LED(4)
led_czerwony = LED(27)
led_zielony = LED(22)
while True:
	led_czerwony.on()
	led_zolty.off()
	led_zielony.off()
	sleep(5)

	led_czerwony.on()
	led_zolty.on()
	led_zielony.off()
	sleep(1)
	
	led_czerwony.off()
	led_zolty.off()
	led_zielony.on()
	sleep(5)

	led_czerwony.off()
	led_zolty.on()
	led_zielony.off()
	sleep(1)
