from machine import Pin, PWM, ADC

# creating PWM and ADC objects
pwm = PWM(Pin(15))
adc = ADC(Pin(28))

# setting frequency of PWM output
pwm.freq(1000)

# continuously control the brightness of the LED using the potentiometer
while True:
    # reading analog values from the potentiometer
    duty = adc.read_u16()
    # writing analog values to the LED
    pwm.duty_u16(duty)
    print(duty)