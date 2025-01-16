from machine import Pin, PWM
import time

# Set the GPIO pin connected to the servo (change to your pin number)
servo_pin = Pin(15)  # GPIO 15, change this according to your wiring

# Set up PWM on the pin
pwm = PWM(servo_pin)
pwm.freq(50)  # Servo motors typically use a frequency of 50Hz

def set_servo_angle(angle):
    # Convert the angle (0-180) to a duty cycle (in microseconds)
    # For most servos, 0° is 1ms pulse, 180° is 2ms pulse
    # Duty cycle range for the servo: 40-115 (duty cycles may need adjustment)
    #duty = int(40 + (angle / 180) * (115 - 40))
    pwm.duty_u16(angle)

# Example: Move servo to 0° and 90° angle with a small delay
while True:
    global angle
#     angle = 180
#     set_servo_angle(angle)
#     print(angle)
#     time.sleep(1)
#     set_servo_angle(-90)
#     print('fif')
#     time.sleep(1)
    set_servo_angle(1802)
    print('fif')
    time.sleep(1)
    set_servo_angle(7664)
    time.sleep(1)

# Optionally, turn off PWM when done
pwm.deinit()

