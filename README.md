# Project Ihy
Project Ihy is a repository for hardware control with a Raspberry Pi Pico.

# Set-up
To set up the raspberry pi the latest uf2 firmware needs to be loaded using the BOOTSEL button method on the Pico. This can be found here:

https://micropython.org/download/RPI_PICO_W/

A method to load the files onto the pico will also be needed, this can be Thonny, Visual studio code or any other suitable program, with VS Code an extension called MicroPico is usefull to install.

# Bluetooth
Blutooth requires two files:
- ble_advertising
- ble_test.py

ble_test.py is the file which can be edited as the Demo() function is just the one which runs when called, this function can be set to do anything but the code outside of that is necessary (*this will be changed to a specified file for this*)
calling the Demo() function from main will start the bluetooth advertising on boot of the Pico and Demo will run once a blutooth connection is made. An app called nRF connect on a mobile device is usefull for this as it will allow you to connected and view incomming messages form the Pico.

# i2c
To test if the i2c devices connected are being seen by the pico:
 - i2c_scan.py

This file when run will output the address of whatever i2c devices are seen on the set scl and sda pins. This is good to use to check the address is correct and the devices are being seen.

# ADC
to set up an external ADC (Analogue to Digital Converter) the files that are required are:
 - ADS1x15.py

ADS1x15.py contains the drivers needed for an external ADC device, **adc.py** is a good file to use to test the device as it will output the adc readings to the terminal. Use the code from adc.py to add adc capabilites to any other code.

## Wiring the adc
for this project an ADS1115 was used for testing. To wire this device up connect the VDD to 3v3out and the GND to ground. The SCL and SDA pins to the SCL and SDA pins that are to be used on the Pico. the A0 to A3 pins are to go to the analogue devices that are to be used, in this testing this was the center pin of a potentiometer with the outer pins connected to 3v3 and ground (one pin to each). The ADDR pin can be connected to change the address of that adc:

| ADDR to * | Address |
| ----------- | ----------- |
| GND | 0x48 |
| VDD | 0x49 |
| SDA | 0x4A |
| SCL | 0x4B | 

This means that 4 ADS1115 devices can be connected to the same SDA and SCL pins on the Pico as long as the address is different for each. if left unconnected the address will default to 0x48, same as ground. The ALRT pin can be left unconnected. 

