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

#Definition of  ultrasonic module pins
EchoPin = 0
TrigPin = 1

#Definition of RGB module pins
LED_R = 22
LED_G = 27
LED_B = 24

#Definition of servo pin
ServoPin = 23
SERVO_OFFSET = -0.9

#Definition of infrared obstacle avoidance module pins
AvoidSensorLeft = 12
AvoidSensorRight = 17

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
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(ServoPin, GPIO.OUT)
    GPIO.setup(AvoidSensorLeft,GPIO.IN)
    GPIO.setup(AvoidSensorRight,GPIO.IN)
    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)

    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)
	


#The servo rotates to the specified angle
def servo_appointed_detection(pos):
    for i in range(18):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180 + SERVO_OFFSET)	
		
def servo_color_carstate():
    servo_appointed_detection(0)
    time.sleep(0.8)
    rightdistance = avoid_ultrasonic.Distance_test()
  
    servo_appointed_detection(180)
    time.sleep(0.8)
    leftdistance = avoid_ultrasonic.Distance_test()

    servo_appointed_detection(90)
    time.sleep(0.8)
    frontdistance = avoid_ultrasonic.Distance_test()
 
    if leftdistance < 30 and rightdistance < 30 and frontdistance < 30:
        CarRun.spin_right(0.58, 35)
    elif leftdistance >= rightdistance:
	CarRun.spin_left(0.28, 35)
    elif leftdistance <= rightdistance:
	CarRun.spin_right(0.28, 35)
		
#delay 2s	
time.sleep(2)

#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
try:
    init()
    while True:
        distance = avoid_ultrasonic.Distance_test()
	if distance > 60:
         infrared_avoid.infr_avoid(50)  
	elif 30 <= distance <= 60:
         infrared_avoid.infr_avoid(20)  
	elif distance < 30:
            CarRun.brake(0)
	    servo_color_carstate()

       
except KeyboardInterrupt:
    pass
pwm_ENA.stop()
pwm_ENB.stop()
GPIO.cleanup()
