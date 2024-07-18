import RPi.GPIO as GPIO
import time

pin_servo = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_servo,GPIO.OUT)

pwn = GPIO.pwn(pin_servo, 50 ) 

def mover_servo(grados):
    duty_cycle = grados / 18.0 + 2.5
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1) 

try:
    pwm.star(0)
    print("Abriendo...")
    mover_servo(0)

    print("cerrando...")
    mover_servo(180)
    time.sleep(2)

finally:
    pwm.stop()
    GPIO.cleanup()


