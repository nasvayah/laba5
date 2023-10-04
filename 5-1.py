import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM) 
def binbin(x):
    return[int(element) for element in bin(x)[2:].zfill(8)]
def adc(x):
    return x*3.3/2**8


dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH) 
gpio.setup(comp, gpio.IN)
n = 0
try:
    while (n<20):
        n=n+1
        for i in range(256):
            binarr = binbin(i)
            gpio.output(dac,binarr)
            time.sleep(0.001)
            value = gpio.input(comp)
            if value == 1:
                print(binarr, " ", adc(i))
                break
finally:
    gpio.output(dac, 0)
    gpio.cleanup()

