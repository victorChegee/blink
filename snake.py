from machine import Pin
from utime import sleep
led=Pin(1,Pin.OUT)
led2=Pin(3,Pin.OUT)
led3=Pin(4,Pin.OUT)
led4=Pin(5,Pin.OUT)
led5=Pin(7,Pin.OUT)
led6=Pin(9,Pin.OUT)
while True :
    led.value(1)
    sleep(0.1)
    led.value(0)
    led2.value(1)
    sleep(0.1)
    led2.value(0)
    led3.value(1)
    sleep(0.1)
    led3.value(0)
    led4.value(1)
    sleep(0.1)
    led4.value(0)
    led5.value(1)
    sleep(0.1)
    led5.value(0)
    sleep(0.1)
    led6.value(1)
    sleep(0.1)
    led6.value(0)
    sleep(0.1)