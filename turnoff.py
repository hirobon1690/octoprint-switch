import pigpio
from time import sleep

pi = pigpio.pi()

pi.set_servo_pulsewidth(14,1500)
sleep(0.5)
pi.set_servo_pulsewidth(14,0)