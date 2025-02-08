from machine import I2C, Pin
import time
from ADS1x15 import ADS1115
i2c=I2C(0, sda=Pin(16), scl=Pin(17))
adc = ADS1115(i2c, address=72, gain=0)

while True:
    pot1 = adc.read(4, 0)
    pot2 = adc.read(4, 1)
    pot3 = adc.read(4, 2)
    pot4 = adc.read(4, 3)
    print("Pot1:", pot1)
    print("Pot2:", pot2)
    print("Pot3:", pot3)
    print("Pot4:", pot4)
    #voltage = adc.raw_to_v(value)
    #print("Voltage", voltage)
    time.sleep(0.5)