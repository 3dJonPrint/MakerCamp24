import gpiozero as gpio

#motor pins
for_left_pin = 5
rev_left_pin = 6
speed_left_pin = 13

for_right_pin = 14
rev_right_pin = 15
speed_right_pin = 18

#motor pins initalisirung
for_right = gpio.DigitalOutputDevice(for_right_pin)
rev_right = gpio.DigitalOutputDevice(rev_right_pin)
speed_right = gpio.PWMOutputDevice(speed_right_pin)

for_left = gpio.DigitalOutputDevice(for_left_pin)
rev_left = gpio.DigitalOutputDevice(rev_left_pin)
speed_left = gpio.PWMOutputDevice(speed_left_pin)