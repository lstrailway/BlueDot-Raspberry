# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import RPi.GPIO as GPIO
import time 
from bluedot import BlueDot



A1 = 15
A2 = 19
ENA = 21
B1 = 16
B2 = 18
ENB = 22


GPIO.setmode(GPIO.BOARD)


GPIO.setup(A1,GPIO.OUT)
GPIO.setup(A2,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)


GPIO.setup(B1,GPIO.OUT)
GPIO.setup(B2,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)



GPIO.output(A1,GPIO.LOW)
GPIO.output(A2,GPIO.LOW)
p1=0
p1=GPIO.PWM(ENA,1000)

GPIO.output(A1,GPIO.LOW)
GPIO.output(A2,GPIO.LOW)
p2=0
p2=GPIO.PWM(ENB,1000)


def runF(x):
    p1.start(80)
    p2.start(80)
    GPIO.output(A1,GPIO.HIGH)
    GPIO.output(A2,GPIO.LOW)
    GPIO.output(B1,GPIO.HIGH)
    GPIO.output(B2,GPIO.LOW)
    
    time.sleep(x)
    
    GPIO.output(A1,GPIO.LOW)
    GPIO.output(A2,GPIO.LOW)
    GPIO.output(B1,GPIO.LOW)
    GPIO.output(B2,GPIO.LOW)
    

def runB(x):
    p1.start(80)
    p2.start(80)
    GPIO.output(A1,GPIO.LOW)
    GPIO.output(A2,GPIO.HIGH)
    GPIO.output(B1,GPIO.LOW)
    GPIO.output(B2,GPIO.HIGH)
    
    time.sleep(x)
    
    GPIO.output(A1,GPIO.LOW)
    GPIO.output(A2,GPIO.LOW)
    GPIO.output(B1,GPIO.LOW)
    GPIO.output(B2,GPIO.LOW)
    
    
def turnL():
    p1.start(30)
    p2.start(90)
    GPIO.output(A1,GPIO.HIGH)
    GPIO.output(A2,GPIO.LOW)
    GPIO.output(B1,GPIO.HIGH)
    GPIO.output(B2,GPIO.LOW)
    
    time.sleep(1)
    
    GPIO.output(A1,GPIO.LOW)
    GPIO.output(A2,GPIO.LOW)
    GPIO.output(B1,GPIO.LOW)
    GPIO.output(B2,GPIO.LOW)
    

def turnR():
    p1.start(90)
    p2.start(30)
    GPIO.output(A1,GPIO.HIGH)
    GPIO.output(A2,GPIO.LOW)
    GPIO.output(B1,GPIO.HIGH)
    GPIO.output(B2,GPIO.LOW)
    
    time.sleep(1)
    
    GPIO.output(A1,GPIO.LOW)
    GPIO.output(A2,GPIO.LOW)
    GPIO.output(B1,GPIO.LOW)
    GPIO.output(B2,GPIO.LOW)
    
    
bd=BlueDot()

try :
    
    
    def main(pos):
        
        if pos.top:
            runF(4)
            print("top ",pos.x,pos.y)
            
            
        if pos.bottom:
            runB(4)
            print("bottom ", pos.x)
            
        if pos.right:
            turnR()
            print("right ",pos.y)
            
            
        if pos.left:
            turnL()
            print("left ", pos.x)
            
        if pos.middle:
            print("middle ",pos.x,pos.y)
            
            
       
    while 1:
        bd.when_pressed=main
        if bd.wait_for_double_press():
            break

finally :
    GPIO.cleanup()
    bd.stop()    




