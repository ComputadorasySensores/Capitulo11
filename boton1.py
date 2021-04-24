import time
import digitalio
import board

boton1_pin= board.GP15

boton1 = digitalio.DigitalInOut(boton1_pin)
boton1.direction = digitalio.Direction.INPUT
boton1.pull = digitalio.Pull.DOWN

while True:
    if boton1.value:
        print("Botón 1 presionado")
        time.sleep(0.2)
        
