import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self,EnaA,In1A,In2A,EnaB,In1B,In2B):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.EnaA,GPIO.OUT)
        GPIO.setup(self.In1A,GPIO.OUT)
        GPIO.setup(self.In2A,GPIO.OUT)
        GPIO.setup(self.EnaB,GPIO.OUT)
        GPIO.setup(self.In1B,GPIO.OUT)
        GPIO.setup(self.In2B,GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnaA,100)
        self.pwmA.start(0)
        self.pwmB = GPIO.PWM(self.EnaB,100)
        self.pwmB.start(0)

    def move(self,speed=0.5,turn=0,t=0):
        speed *= 100
        turn *= 100
        Leftspeed = speed - turn
        Rightspeed = speed + turn

        if Leftspeed >100: Leftspeed = 100
        elif Leftspeed <-100: Leftspeed = -100
        if Rightspeed >100: Rightspeed = 100
        elif Rightspeed <-100: Rightspeed =-100

        self.pwmA.ChangeDutyCycle(abs(Leftspeed))
        self.pwmB.ChangeDutyCycle(abs(Rightspeed))

        if Leftspeed>0:
            GPIO.output(self.In1A,GPIO.HIGH)
            GPIO.output(self.In2A,GPIO.LOW)
        else :
            GPIO.output(self.In1A,GPIO.LOW)
            GPIO.output(self.In2A,GPIO.HIGH)

        if Rightspeed>0:
            GPIO.output(self.In1B,GPIO.HIGH)
            GPIO.output(self.In2B,GPIO.LOW)
        else :
            GPIO.output(self.In1B,GPIO.LOW)
            GPIO.output(self.In2B,GPIO.HIGH)

        sleep(t)

    def stop(self,t=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        sleep(t)

def main():
    motor1.move(0.6,0,0.1)
    motor1.stop(2)
    motor1.move(0.6,0,0.1)
    motor1.stop(2)

if __name__ == '__main__':
    motor1 = Motor(2,3,4,17,22,27)
    main()