from machine import Pin, I2C
import time

# Initialize I2C on GPIO 0 (SDA) and GPIO 1 (SCL)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=100000)  # I2C bus 0, 100 kHz speed

# Perform an I2C scan
def scan_i2c():
    devices = i2c.scan()  # List of I2C addresses found on the bus
    if devices:
        print("I2C devices found at addresses:")
        for device in devices:
            print(hex(device))  # Print the I2C addresses in hexadecimal format
    else:
        print("No I2C devices found")

# Main loop to scan I2C bus and print results
while True:
    scan_i2c()
    time.sleep(2)  # Wait 2 seconds before scanning again
