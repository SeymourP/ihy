from machine import Pin, I2C
import time
from pcf8575 import PCF8575

# Set up I2C on the Raspberry Pi Pico (GPIO 0 = SDA, GPIO 1 = SCL)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=10000)

# The address of the PCF8575 (usually 0x20 by default, but can vary depending on the address pins)
pcf = PCF8575(i2c, 0x20)

# Function to read the state of the buttons
pcf.port = 0xFFFF

while True:
#     pcf.toggle(0)
#     time.sleep(0.1)
#     pcf.toggle(1)
#     time.sleep(0.1)
#     pcf.toggle(2)
#     time.sleep(0.1)
#     pcf.toggle(3)
#     time.sleep(0.1)
#     pcf.toggle(4)
#     # print(pcf.pin(0))
#     # Delay before checking again
#     time.sleep(0.1)
#    print(pcf.pin(0))

    if(not pcf.pin(0)):
        print("button 0 pressed")
    if(not pcf.pin(1)):
        print("button 1 pressed")
    if(not pcf.pin(2)):
        print("button 2 pressed")
    if(not pcf.pin(3)):
        print("button 3 pressed")
    if(not pcf.pin(4)):
        print("button 4 pressed")
       
    time.sleep(0.1)