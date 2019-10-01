# -*- coding:UTF-8 -*-

import RPi.GPIO as GPIO
import time

#Definition of RGB module pin
LED_R = 22
LED_G = 27
LED_B = 24

#Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#RGB pins are initialized into output mode
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
global pwm_red
global pwm_green
global pwm_blue
pwm_red = GPIO.PWM(LED_R, 1000)
pwm_green = GPIO.PWM(LED_G, 1000)
pwm_blue = GPIO.PWM(LED_B, 1000)
pwm_red.start(0)
pwm_green.start(0)
pwm_blue.start(0)

"""
Checks to make sure the input power is a valid value
@param power should be a number 0<=power<=100
@return the boolean of whether or not it is valid
"""
def check_power(power):
    if((power < 0) or (power > 100)):
        print("Invalid power!")
        print("Please use a number within 0-100")
        return False
    else:
        return True

"""
turns on the red LED with either 0 or 1 arguement
no arguements sets the power to 100, but the optional arguement will set power
@param args[0] (optional) will specify the power of the LED
"""
def turn_on_red(*args):
    if len(args) > 1:
        print("Too many arguements!")
    if len(args) == 1:
        if check_power(args[0]):
            pwm_red.ChangeDutyCycle(args[0])
    else:
        pwm_red.ChangeDutyCycle(100)

"""
turns on the green LED with either 0 or 1 arguement
no arguements sets the power to 100, but the optional arguement will set power
@param args[0] (optional) will specify the power of the LED
"""
def turn_on_green(*args):
    if len(args) > 1:
        print("Too many arguements!")
    if len(args) == 1:
        if check_power(args[0]):
            pwm_green.ChangeDutyCycle(args[0])
    else:
        pwm_green.ChangeDutyCycle(100)

"""
turns on the blue LED with either 0 or 1 arguement
no arguements sets the power to 100, but the optional arguement will set power
@param args[0] (optional) will specify the power of the LED
"""
def turn_on_blue(*args):
    if len(args) > 1:
        print("Too many arguements!")
    if len(args) == 1:
        if check_power(args[0]):
            pwm_blue.ChangeDutyCycle(args[0])
    else:
        pwm_blue.ChangeDutyCycle(100)

"""
turns on the specified LED (color) with a specified power
@param color the color of the LED to be turned on
@param power the power of the LED
"""
def turn_on_LED(color, power):
    if color == "red":
        turn_on_red(power)
    elif color == "green":
        turn_on_green(power)
    elif color == "blue":
        turn_on_blue(power)
    else:
        print("Invalid color!")

"""
turns on a single or a set of LEDS (same as "turn_on_LED" except it can take
multiple LEDS at once as arguements)
number of pairs is optional, and no arguements will turn all LEDs off
@param args should be pairs of arguements as (color1,power1, color2,power2,...)
"""
def turn_on_LEDs(*args):
    turn_on_red(0)
    turn_on_green(0)
    turn_on_blue(0)
    for i in range(0,len(args),2):
        try:
            turn_on_LED(args[i], args[i+1])
        except IndexError:
            print("should be an even number of arguements")
            print("(color1, power1, color2, power2, etc..)")


"""
#Display 7 color LED
try:
    while True:
        for i in range(0,101):
            pwm_red.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_red.ChangeDutyCycle(100-i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_blue.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_blue.ChangeDutyCycle(100-i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_green.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_green.ChangeDutyCycle(100-i)
            time.sleep(0.01)
        pwm_red.ChangeDutyCycle(100)
        for i in range(0,101):
            pwm_blue.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_blue.ChangeDutyCycle(100-i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_green.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_green.ChangeDutyCycle(100-i)
            time.sleep(0.01)
        pwm_red.ChangeDutyCycle(0)
        pwm_blue.ChangeDutyCycle(100)
        for i in range(0,101):
            pwm_red.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_red.ChangeDutyCycle(100-i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_green.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_green.ChangeDutyCycle(100-i)
            time.sleep(0.01)
        pwm_blue.ChangeDutyCycle(0)
        pwm_green.ChangeDutyCycle(100)
        for i in range(0,101):
            pwm_red.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_red.ChangeDutyCycle(100-i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_blue.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(0,101):
            pwm_blue.ChangeDutyCycle(100-i)
            time.sleep(0.01)
        pwm_green.ChangeDutyCycle(0)
        for i in range(0,101):
            pwm_red.ChangeDutyCycle(i)
            pwm_blue.ChangeDutyCycle(i)
            pwm_green.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100,-1,-1):
            pwm_red.ChangeDutyCycle(i)
            pwm_blue.ChangeDutyCycle(i)
            pwm_green.ChangeDutyCycle(i)
            time.sleep(0.02)



        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(1)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(1)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(1)
        GPIO.output(LED_R, GPIO.HIGH)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.HIGH)
        GPIO.output(LED_B, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_R, GPIO.LOW)
        GPIO.output(LED_G, GPIO.LOW)
        GPIO.output(LED_B, GPIO.LOW)
        time.sleep(1)
except:
    print "except"
GPIO.cleanup()
"""
