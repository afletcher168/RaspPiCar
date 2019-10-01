"""
MyTravelling.py

@author Andrew Fletcher
    email: afletcher168@gmail.com
@since 08/09/2019
Sources of help:
    Huge source of help/much of the code taken from the company Yahboom
    Freenove tutorial for their Reaspberry Pi starter kit

This file is for having the car travel in the original direction. 
If it encounters an obstacle, it will try to go around the obstacle, then
return to it's original direction.
"""

#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import CarRun
import avoid_ultrasonic
import infrared_avoid

#Definition of  motor pins 
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#Definition of infrared obstacle avoidance module pin
AvoidSensorLeft = 12
AvoidSensorRight = 17

#Definition of servo pin
ServoPin = 23
SERVO_OFFSET = -0.9

car_angle = 0

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pins are initialized into output mode
#Key pin is initialized into input mode
#Ultrasonic pin,RGB pin,servo pin initialization
#infrared obstacle avoidance module pin
def init():
    global pwm_ENA
    global pwm_ENB
    global pwm_servo
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(AvoidSensorLeft,GPIO.IN)
    GPIO.setup(AvoidSensorRight,GPIO.IN)
    GPIO.setup(ServoPin, GPIO.OUT)
    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)
	

"""
The servo rotates to the specified angle
@param pos the desired position of the servo in degrees with 0 as facing right
"""
def servo_appointed_direction(pos):
    if pos > 180:
        pos = 180
    elif pos < 0:
        pos = 0

    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180 + SERVO_OFFSET)	
		
"""
checks the distance in front, to the left, and to the right by moving the servo
with the utlrasonic sensor on it.
This iteration of the method also spins the car to the side that has the most
distance (space), and points the servo/ultrasonic sensor in the originial
direction.
"""
def servo_distance_check():
    servo_appointed_direction(0)
    time.sleep(0.8)
    rightdistance = avoid_ultrasonic.Distance_test()
  
    servo_appointed_direction(180)
    time.sleep(0.8)
    leftdistance = avoid_ultrasonic.Distance_test()

    servo_appointed_direction(90)
    time.sleep(0.8)
    frontdistance = avoid_ultrasonic.Distance_test()

    global car_angle
    
    if leftdistance < 30 and rightdistance < 30 and frontdistance < 30:
        CarRun.spin_right(0.65, 35)
        CarRun.brake(0)
        car_angle -= 180
        servo_appointed_direction(180)
    elif leftdistance >= rightdistance:
        CarRun.spin_left(0.4, 50)
        CarRun.brake(0)
        car_angle += 90
        servo_appointed_direction(0)
    elif leftdistance <= rightdistance:
        CarRun.spin_right(0.4, 100)
        time.sleep(5)
        CarRun.brake(0)
        car_angle -= 90
        servo_appointed_direction(180)
    time.sleep(0.8)


"""
avoids obstacles using the infrared sensors on the front of the car.
If it gets stopped, it will turn all the way around in order to fulfill the
requirements of the travelling function.
@param power the speed at which the car moves during the method
"""
def travelling_infra_avoid(power):
    global car_angle
    LeftSensorValue  = GPIO.input(AvoidSensorLeft)
    RightSensorValue = GPIO.input(AvoidSensorRight)

    if LeftSensorValue == True and RightSensorValue == True :
        CarRun.run(0.002,power)     
    elif LeftSensorValue == True and RightSensorValue == False :
        CarRun.spin_left(0.05,35)   
    elif RightSensorValue == True and LeftSensorValue == False:
        CarRun.spin_right(0.05,35)  			
    elif RightSensorValue == False and LeftSensorValue == False :
        if car_angle < 0:
            CarRun.spin_left(0.65,35)
            car_angle += 180
        else:
            CarRun.spin_right(0.65,35)
            car_angle -= 180
        CarRun.brake(0)
        servo_appointed_direction(90-car_angle) 
        time.sleep(0.8)


"""
Looks for an opening in the original dirctoon and realligns the car once
an opening is found
@param power the speed of the car during the method
"""
def look_for_opening(power):
    global car_angle
    distance = avoid_ultrasonic.Distance_test()
    while distance < 40:
        travelling_infra_avoid(power)
        distance = avoid_ultrasonic.Distance_test()

    CarRun.run(0.5,30)
    CarRun.brake(0)

    if car_angle < 0:
        CarRun.spin_left(0.5, 50)
        car_angle += 90
    else:
        CarRun.spin_right(0.5, 50)
        car_angle -= 90
    CarRun.brake(0)
    servo_appointed_direction(90)
    time.sleep(0.8)
    

		
#delay 1s	
time.sleep(1)


try:
    print(1)
    init()
    car_angle = 0
    servo_appointed_direction(90)
    time.sleep(0.8)
    while True:
        distance = avoid_ultrasonic.Distance_test()
        if distance > 60:
            infrared_avoid.infr_avoid(50)
        elif 30 <= distance <= 60:
            infrared_avoid.infr_avoid(20)
        else:
            print(2)
            CarRun.brake(0)
            #servo_distance_check()
            time.sleep(5)
            CarRun.brake(0)
            look_for_opening(40)
except KeyboardInterrupt:
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()

"""
#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
try:
    init()
    car_angle = 0
    while True:
        distance = avoid_ultrasonic.Distance_test()
	if distance > 60:
         infrared_avoid.infr_avoid(50)  
	elif 30 <= distance <= 60:
         infrared_avoid.infr_avoid(20)  
	elif distance < 30:
            CarRun.brake(0)
        if servo_distance_check:
            car_angle -= 90
        else:
            car_angle += 90
        look_for_opening(40)

       
except KeyboardInterrupt:
    pass
pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup()
"""