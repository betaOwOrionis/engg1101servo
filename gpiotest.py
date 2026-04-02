from gpiozero import Servo
import time
servo = Servo(12)

while True:
    servo.min()
    time.sleep(2)
    servo.mid()
    time.sleep(2)
    servo.max()
    time.sleep(2)
