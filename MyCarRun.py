import RPi.GPIO as GPIO
import time

#Definition of  motor pin 
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

#Declaring default values
TOP_SPEED = 100
FAST = 80
MEDIUM = 50
SLOW = 20
STOPPED = 0



#setup for the program
def setup():
    #Set the GPIO port to BCM encoding mode
    GPIO.setmode(GPIO.BCM)
    #Ignore warning information
    GPIO.setwarnings(False)
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

"""
moves the car forward in a straight line
takes up to 2 arguements, otherwise will use defaults
@param runtime the runtime in seconds for this command
@param speed the speed at which the car will travel on a scale 0-100
"""
def run(*args):
    runtime = 1  #default runtime of 1 second
    speed = MEDIUM  #default speed of medium (pwm=50)
    if(len(args) > 2):
        print("run only takes 2 parameters (runtime, speed)")
    if(len(args) > 1):
        if((args[1] >= 0) and (args[1] <= 100)):
            speed = args[1]
        else:
            print("Please input a speed value within 0-100")
    if(len(args) > 0):
        if(args[0] > 0):
            runtime = args[0]
        else:
            print("Please input a positive number for runtime (seconds)")

    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(runtime)

"""
moves the car backward in a straight line
takes up to 2 arguements, otherwise will use defaults
@param runtime the runtime in seconds for this command
@param speed the speed at which the car will travel on a scale 0-100
"""
def back(*args):
    runtime = 1  #default runtime of 1 second
    speed = MEDIUM  #default speed of medium (pwm=50)
    if(len(args) > 2):
        print("run only takes 2 parameters (runtime, speed)")
    if(len(args) > 1):
        if((args[1] >= 0) and (args[1] <= 100)):
            speed = args[1]
        else:
            print("Please input a speed value within 0-100")
    if(len(args) > 0):
        if(args[0] > 0):
            runtime = args[0]
        else:
            print("Please input a positive number for runtime (seconds)")
    
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(runtime)

"""
Turns the car left by having the right wheels move forward, and left wheels
stationary
takes up to 2 arguements, otherwise will use defaults
@param runtime the runtime in seconds for this command
@param speed the speed at which the car will travel on a scale 0-100
"""
def left(*args):
    runtime = 1  #default runtime of 1 second
    speed = MEDIUM  #default speed of medium (pwm=50)
    if(len(args) > 2):
        print("run only takes 2 parameters (runtime, speed)")
    if(len(args) > 1):
        if((args[1] >= 0) and (args[1] <= 100)):
            speed = args[1]
        else:
            print("Please input a speed value within 0-100")
    if(len(args) > 0):
        if(args[0] > 0):
            runtime = args[0]
        else:
            print("Please input a positive number for runtime (seconds)")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(runtime)

"""
Turns the car right by having the left wheels move forward, and right wheels
stationary
takes up to 2 arguements, otherwise will use defaults
@param runtime the runtime in seconds for this command
@param speed the speed at which the car will travel on a scale 0-100
"""
def right(*args):
    runtime = 1  #default runtime of 1 second
    speed = MEDIUM  #default speed of medium (pwm=50)
    if(len(args) > 2):
        print("run only takes 2 parameters (runtime, speed)")
    if(len(args) > 1):
        if((args[1] >= 0) and (args[1] <= 100)):
            speed = args[1]
        else:
            print("Please input a speed value within 0-100")
    if(len(args) > 0):
        if(args[0] > 0):
            runtime = args[0]
        else:
            print("Please input a positive number for runtime (seconds)")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(runtime)

"""
Turns the car left in place by having the right wheels move forward, 
and left wheels spin in reverse
takes up to 2 arguements, otherwise will use defaults
@param runtime the runtime in seconds for this command
@param speed the speed at which the car will travel on a scale 0-100
"""
def spin_left(*args):
    runtime = 1  #default runtime of 1 second
    speed = MEDIUM  #default speed of medium (pwm=50)
    if(len(args) > 2):
        print("run only takes 2 parameters (runtime, speed)")
    if(len(args) > 1):
        if((args[1] >= 0) and (args[1] <= 100)):
            speed = args[1]
        else:
            print("Please input a speed value within 0-100")
    if(len(args) > 0):
        if(args[0] > 0):
            runtime = args[0]
        else:
            print("Please input a positive number for runtime (seconds)")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(runtime)

"""
Turns the car right by having the left wheels move forward, 
and right wheels spin in reverse
takes up to 2 arguements, otherwise will use defaults
@param runtime the runtime in seconds for this command
@param speed the speed at which the car will travel on a scale 0-100
"""
def spin_right(*args):
    runtime = 1  #default runtime of 1 second
    speed = MEDIUM  #default speed of medium (pwm=50)
    if(len(args) > 2):
        print("run only takes 2 parameters (runtime, speed)")
    if(len(args) > 1):
        if((args[1] >= 0) and (args[1] <= 100)):
            speed = args[1]
        else:
            print("Please input a speed value within 0-100")
    if(len(args) > 0):
        if(args[0] > 0):
            runtime = args[0]
        else:
            print("Please input a positive number for runtime (seconds)")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    time.sleep(runtime)

"""
Stops the car for the specified amount of time
"""
def brake(*args):
    runtime = 1  #default runtime
    if(len(args) > 1):
        print("brake only takes 1 arg  (runtime)")
    if(len(args) == 1):
        if(args[0] > 0):
            runtime = args[0]
        else:
            print("Please input a positive number for runtime (seconds)")
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(runtime)
"""
def check_validity(arguement):
    if((arguement >= 0) and (arguement <= 100)):
        return True
    else:
        print("Please input a numbers between 0-100")
"""

#Delay 2s	
time.sleep(2)

#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
#The robot car advance 1s，back 1s，turn left 2s，turn right 2s，turn left  in place 3s
#turn right  in place 3s，stop 1s。
try:
    setup()
    while True:
        run(1, FAST)
        back(1, SLOW)
        left(1)
        right(1, MEDIUM)
        spin_left(1, TOP_SPEED)
        spin_right()
        brake(1)
except KeyboardInterrupt:
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()