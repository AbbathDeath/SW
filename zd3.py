from gpiozero import LED, Button
import time

button = Button(23)

g_pieszy = LED(5)
r_pieszy = LED(6)

g_auto = LED(13)
y_auto = LED(19)
r_auto = LED(26)

def przejscie():
    r_pieszy.off()
    g_auto.off()
    y_auto.on()
    time.sleep(1)
    
    y_auto.off()
    r_auto.on()
    g_pieszy.on()
    time.sleep(3)
    
    r_auto.off()
    y_auto.on()
    g_pieszy.off()
    r_pieszy.on()
    time.sleep(1)
    
    y_auto.off()
    g_auto.on()
    time.sleep(1)
    
r_pieszy.on()
g_auto.on()
while True:
    if button.is_pressed:
        print("wchodzi na przejscie")
        przejscie()
        
