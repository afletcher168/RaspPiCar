#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import ColorLED

#Definition of  motor pin 
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pin initialization operation
def motor_init():
    global pwm_ENA
    global pwm_ENB
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

#advance
def run(delaytime, power):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    ColorLED.turn_on_LEDs("red", power, "green", power, "blue", power)
    time.sleep(delaytime)

#back
def back(delaytime, power):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    ColorLED.turn_on_LEDs("red", (50 + power/2))
    time.sleep(delaytime)

#turn left
def left(delaytime, power):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(0)
    pwm_ENB.ChangeDutyCycle(power)
    ColorLED.turn_on_LEDs("green", power, "blue", power)
    time.sleep(delaytime)

#turn right
def right(delaytime, power):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(0)
    ColorLED.turn_on_LEDs("green", power, "blue", power)
    time.sleep(delaytime)

#turn left in place
def spin_left(delaytime, power):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    ColorLED.turn_on_LEDs("red", power, "blue", power)
    time.sleep(delaytime)

#turn right in place
def spin_right(delaytime, power):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(power)
    pwm_ENB.ChangeDutyCycle(power)
    ColorLED.turn_on_LEDs("red", power, "blue", power)
    time.sleep(delaytime)

#brake
def brake(delaytime):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(0)
    pwm_ENB.ChangeDutyCycle(0)
    ColorLED.turn_on_LEDs("red", 20)
    time.sleep(delaytime)

"""
#Delay 2s	
time.sleep(2)
"""
#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
#The robot car advance 1s，back 1s，turn left 2s，turn right 2s，turn left  in place 3s
#turn right  in place 3s，stop 1s。

motor_init()
"""
try:
    motor_init()
    while True:
        for i in range(0,101):
            run(0.01,i)
        for i in range(100,-1,-1):
            run(0.01,i)
        brake(0.5)
        for i in range(0,101):
            back(0.01,i)
        for i in range(100,-1,-1):
            back(0.01,i)
        brake(0.5)
        left(0.6,45)
        right(0.6,45)
        brake(0.5)
        for i in range(0,101):
            spin_left(0.0055,i)
        for i in range(100,-1,-1):
            spin_left(0.0055,i)
        for i in range(0,101):
            spin_right(0.0055,i)
        for i in range(100,-1,-1):
            spin_right(0.0055,i)
        brake(1)
        
        run(1, 50)
        back(1, 50)
        left(1, 50)
        right(1, 50)
        spin_left(.28, 35)
        spin_right(.28, 35)
        brake(1)
except KeyboardInterrupt:
    pass
pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup() 
"""


