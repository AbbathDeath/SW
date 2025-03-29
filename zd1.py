from gpiozero import LED, Button
import time
pieszy = LED(5)
przycisk = Button(18)

pieszy.off()

while True:
    #pieszy.on()
    #time.sleep(1)
    #pieszy.off()
    
    if przycisk.is_pressed:
        print("przycisk klikniety")
        pieszy.on()
        time.sleep(5)
        pieszy.off()
        
        pieszy.on()
        time.sleep(1)
        pieszy.off()
        
        pieszy.on()
        time.sleep(1)
        pieszy.off()
        
        pieszy.on()
        time.sleep(1)
        pieszy.off()
        
        pieszy.on()
        time.sleep(1)
        pieszy.off()
    #print("czekam")
    time.sleep(0.1)