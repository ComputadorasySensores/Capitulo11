import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

boton1_pin= board.GP15

teclado = Keyboard(usb_hid.devices)

boton1 = digitalio.DigitalInOut(boton1_pin)
boton1.direction = digitalio.Direction.INPUT
boton1.pull = digitalio.Pull.DOWN

while True:
    if boton1.value:
        print("Botón 1 Seleccionar Todo")
        teclado.press(Keycode.CONTROL, Keycode.A)
        time.sleep(0.1)
        teclado.release(Keycode.CONTROL, Keycode.A)
    time.sleep(0.1)
