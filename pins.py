import gpiozero as gpio

#motor pins
rev_left_pin = 7
for_left_pin = 1
speed_left_pin = 12

for_right_pin = 14
rev_right_pin = 15
speed_right_pin = 18

#motor pins initalisirung
for_left = gpio.DigitalOutputDevice(for_left_pin)
rev_left = gpio.DigitalOutputDevice(rev_left_pin)
speed_left = gpio.PWMOutputDevice(speed_left_pin)

for_right = gpio.DigitalOutputDevice(for_left_pin)
rev_right = gpio.DigitalInputDevice(rev_left_pin)
speed_right = gpio.PWMOutputDevice(speed_left_pin)