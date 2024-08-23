import gpiozero as gpio

#motor pins
for_left_pin = 5
rev_left_pin = 6
speed_left_pin = 13

for_right_pin = 14
rev_right_pin = 15
speed_right_pin = 18

#motor pins initalisirung:
for_right = gpio.DigitalOutputDevice(for_right_pin, initial_value=False)
rev_right = gpio.DigitalOutputDevice(rev_right_pin, initial_value=False)
speed_right = gpio.PWMOutputDevice(speed_right_pin, initial_value=1)

for_left = gpio.DigitalOutputDevice(for_left_pin, initial_value=False)
rev_left = gpio.DigitalOutputDevice(rev_left_pin, initial_value=False)
speed_left = gpio.PWMOutputDevice(speed_left_pin, initial_value=1)