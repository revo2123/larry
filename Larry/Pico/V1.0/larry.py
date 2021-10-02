from machine import Pin, PWM
import utime

count = 10

servo = PWM(Pin(0))

servo.freq(50)

# .duty_16(#) takes values of 0 to 65535 for duty cycle of 0 to 100
# SG90 has 2 per cent duty cycle for 0 degrees, 12 per cent for 180.
# So a .duty_u16 value of c.1350 is zero degrees; 8200 is 180 degrees.

while count != 10:
    count = count + 1
    # Move servo to zero degrees (2 per cent duty cycle)
    servo.duty_u16(1350)
    utime.sleep(2)
    # Move servo to 180 degrees (12 per cent duty cycle)
    servo.duty_u16(8200)
    utime.sleep(2)
    print('turning')