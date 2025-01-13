from machine import Pin, PWM
from time import sleep

class Servo:
    __servo_pwm_freq = 50  # Standard frequency for servos (50 Hz)
    __min_u16_duty = 1000  # Min pulse width (in microseconds)
    __max_u16_duty = 2000  # Max pulse width (in microseconds)
    min_angle = 0
    max_angle = 180
    current_angle = 0.001

    def __init__(self, pin, reverse=False):
        self.__reverse = reverse  # Reverse direction flag
        self.__initialise(pin)

    def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u16_duty = min_u16_duty
        self.__max_u16_duty = max_u16_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)

    def move(self, angle):
        angle = round(angle, 2)
        if angle == self.current_angle:
            return
        self.current_angle = angle

        # Debug: Print the angle being moved to
        print(f"Moving servo to angle: {angle}")
        duty_u16 = self.__angle_to_u16_duty(angle)
        print(f"Calculated duty cycle: {duty_u16}")

        self.__motor.duty_u16(duty_u16)

    def __angle_to_u16_duty(self, angle):
        # Reverse the angle if needed
        if self.__reverse:
            angle = 180 - angle  # Reverse logic for servo
        
        # Map angle to duty cycle between min_u16_duty and max_u16_duty
        duty = int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty
        print(f"Angle: {angle}, Duty Cycle: {duty}")  # Debug output
        return duty

    def __initialise(self, pin):
        self.current_angle = -0.001
        # Calculate the angle-to-duty conversion factor
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)

# Initialize the servo on the correct pin
servo_pin = 15  # Change this to the pin your servo is connected to
servo = Servo(servo_pin)

# Move the servo to different angles
servo.move(0)     # Move to 0 degrees
sleep(1)           # Wait for 1 second
servo.move(90)    # Move to 90 degrees
sleep(1)           # Wait for 1 second
servo.move(180)   # Move to 180 degrees
sleep(1)           # Wait for 1 second

