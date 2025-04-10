import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

lcd_rs = digitalio.DigitalInOut(board.D25)
lcd_en = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D23)
lcd_d5 = digitalio.DigitalInOut(board.D17)
lcd_d6 = digitalio.DigitalInOut(board.D18)
lcd_d7 = digitalio.DigitalInOut(board.D22)

lcd_columns = 16
lcd_rows = 2
lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

lcd.message = "Hello\nWorld"
time.sleep(5)
lcd.clear()

text = input("Type something:")
lcd.message = text

time.sleep(5)
lcd.clear()
lcd.message = "Goodbye\nWorld"

time.sleep(5)
lcd.clear()
