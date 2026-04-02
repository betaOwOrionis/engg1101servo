import RPi.GPIO as GPIO
import time
angle = 0
GPIO.setmode(GPIO.BOARD)
servo_pin = 12
GPIO.setup(servo_pin, GPIO.OUT)

# PWM Setup - 50Hz
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)

try:
    while True:
        x = input("Enter angle (0-180) or 'q' to quit: ")
        if x == 'q':
                print("Terminating program...")
                pwm.stop()
                GPIO.cleanup()
        try:
            angle = int(x)
            if 0 <= angle <= 180:
                set_angle(angle)
            else:
                print("Please enter an angle between 0 and 180.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

except KeyboardInterrupt:
    print("Terminating program...")
    pwm.stop()
    GPIO.cleanup()
