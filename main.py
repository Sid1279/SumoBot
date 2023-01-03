from cyberbot import *
from random import randint
from machine import time_pulse_us
from qti import *

#Setup code to declare pins and functions (similar to void setup in Arduino)
trig = pin13 #Set pin 13 as trig
echo = pin14 #Set pin 14 as echo
right = bot(18) #Pin 18 controls motion of right servo motor
left = bot(19) #Pin 19 controls motion of left servo motor

#Functions to control the bot
def forward(): #function to make the bot go forward
    right.servo_speed(75)
    left.servo_speed(-75)

def backward(): #function to make the bot go backward
    right.servo_speed(-75)
    left.servo_speed(75)

def turnLeft(): #function to make the bot go left
    right.servo_speed(-20)
    left.servo_speed(-75)

def turnRight(): #function to make the bot go right
    right.servo_speed(75)
    left.servo_speed(20)

def leftBackward(): #function to make the bot go backward, turning left
    right.servo_speed(-75)
    left.servo_speed(-20)

def rightBackward(): #function to make the bot go backward, turning right
    right.servo_speed(-20)
    left.servo_speed(-75)

while True: #while loop runs repeatedly (similar to void loop in Arduino)
    #start US measurement section
    distance = 0
    trig.write_digital(1)
    trig.write_digital(0)
    time = time_pulse_us(echo, 1)
    distance = (time * 0.034) / 2
    #end US measurement section

    #reads inputs from QTI sensors
    pattern = qti(9, 8).read()

    #reads inputs from IR Sensors
    IRright = bot(1, 2).ir_detect(37500) #Input from right Infrared Sensor
    IRleft = bot(14, 13).ir_detect(37500) #Input from left Infrared Sensor

    if pattern == 3: #Both QTI sensors detect Black
        if distance < 30 and IRright == 1 and IRleft == 1:
        #if an object is in front of US sensor, but not IR sensors
            #charge forward
            forward()
            display.show(Image.SWORD) #displays a sword to show that the bot is charging
        elif distance >= 30 and IRright == 1 and IRleft == 1:
            #if no object is in front of US sensor or IR sensors
            forward()#move in a default forward motion
            display.show(Image.HAPPY) #displays a happy face
        elif distance < 30 and IRright == 0 and IRleft == 0:
            #if an object is in front of US sensor, and BOTH IR sensors detect an object
            forward()#charge forward
            display.show(Image.SWORD) #displays a sword to show that the bot is charging
        elif IRright == 0:
            #if right IR sensor detects an object, keep turning right until object is detected by the US sensor
            if distance > 30: #checks if object is in front of US sensor while turning right
                turnRight() #turns right
                display.scroll(“R”) #displays R: Right
            else:
                forward() #charges forward if US sensor detects object in front
                display.show(Image.SWORD)

    elif IRleft == 0:
    #if left IR sensor detects an object, keep turning left until object is detected by the US sensor
        if distance > 30: #checks if object is in front of US sensor while turning left
            turnLeft() #turns left
            display.scroll(“L”) #Displays L: Left
        else:
            forward() #charges forward if US sensor detects object in front
            display.show(Image.SWORD)

    elif pattern == 2: #right QTI sensor detects White, left QTI sensor detects Black
        backward() #goes backwards
        sleep(randint(500, 750)) #random delay for going backwards: between 500ms - 750ms
        rightBackward() #goes right backwards
        display.scroll("RB") #displays RB: Right Backwards
        sleep(randint(150, 350)) #random delay for right backwards: between 150ms - 350ms

    elif pattern == 1: #left QTI sensor detects White, right QTI sensor detects Black
        backward() #goes backwards
        sleep(randint(500, 750)) #random delay for going backwards: between 500ms - 750ms
        leftBackward() #goes left backwards
        display.scroll("LB") #displays LB: Left Backwards
        sleep(randint(150, 350)) #random delay for left backwards: between 150ms - 350ms

    else: #both QTI sensors detect are White
        backward() #goes backwards
        display.scroll("Rev") #displays Rev: Reverse
        sleep(randint(500, 750)) #random delay for going backwards between 500ms - 750ms

        #Randomly turn either left or right after going backwards
        if randint(1, 3) == 1: #Chooses either 1 or 2
            turnRight() #turns right if the number is 1
        else:
            turnLeft() #turns left if the number is 2
        sleep(randint(150, 350)) #Random delay between 150ms - 350ms