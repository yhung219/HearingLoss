from gpiozero import LED
from time import sleep

led = LED(16)

while True:
    led.on(1)
    sleep(1)
    led.off(1)
    sleep(1)