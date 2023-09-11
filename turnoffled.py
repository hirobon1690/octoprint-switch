import pigpio

pi = pigpio.pi()
pi.set_mode(26, pigpio.OUTPUT)

pi.write(26,0)