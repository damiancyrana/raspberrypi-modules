import os
import time
from RPLCD.i2c import CharLCD
from datetime import datetime

def get_cpu_temperature():
    temp_file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(temp_file.read()) / 1000
    temp_file.close()
    return temp

# Adres I2C wyświetlacza LCD
LCD_ADDR = 0x27

# Inicjalizacja wyświetlacza LCD
lcd = CharLCD(i2c_expander='PCF8574', address=LCD_ADDR, port=1, cols=16, rows=2, dotsize=8)

while True:
    # Pobieranie aktualnego czasu
    current_time = datetime.now().strftime("%H:%M:%S")

    # Pobieranie temperatury procesora
    cpu_temp = get_cpu_temperature()

    # Formatowanie wyświetlanego tekstu
    display_line_1 = f"Time: {current_time}"
    display_line_2 = f"CPU Temp: {cpu_temp:.1f}C"

    # Wysyłanie tekstu do wyświetlacza LCD
    lcd.cursor_pos = (0, 0)
    lcd.write_string(display_line_1)
    lcd.cursor_pos = (1, 0)
    lcd.write_string(display_line_2)

    # Aktualizacja co sekundę
    time.sleep(1)
    lcd.clear()
