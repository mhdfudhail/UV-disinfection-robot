from motor_driver import Motor  #motor driver module
import key_press as kp     #keyboard module for movements of robot and control Uv light
from camera import piCam  #camera module for camera view
import RPi.GPIO as GPIO #gpio module for relay and pir sensor
import ultrasonic as ults #importing ultrasonic modules
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


motor = Motor(2,3,4,17,22,27) #motor driver pins
runCamera = True
GPIO.setup(14,GPIO.OUT) #defining the relay pin(relay control the UV light)
GPIO.setup(15,GPIO.IN)  #defining the first pir module
GPIO.setup(18,GPIO.IN)  #defining the second pir module
GPIO.setup(23,GPIO.OUT) #extra uv light control
GPIO.setup(5,GPIO.OUT) #buzzer



kp.init() #initialization of keyboard
if runCamera: piCam(x=1,y=1)

def main():

    if kp.getKey('UP'): #if press 'UP' key move forward
        result = ults.checkFrontDistance(30) # checking the Front limit distance at 30cm
        if result== True:
            print("moving forward")
            GPIO.output(5,GPIO.LOW)
            motor.move(0.6,0,0.1) #motor run '60%' of speed with '0'turning and '100ms'delay
        else :
            print("limit is over")
            GPIO.output(5,GPIO.HIGH) #buzzer on
            motor.stop(1)
    elif kp.getKey('DOWN'):# if press 'DOWN' key the motor move backward
        result = ults.checkBackDistance(30)# checking the Back limit distance at 30cm
        if result == True:
            print("moving backward")
            GPIO.output(5,GPIO.LOW)
            motor.move(-0.6,0,0.1) #motor run '60%' of speed with '0'turning and '100ms'delay
        else :
            print("limit is over")
            GPIO.output(5,GPIO.HIGH) #buzzer on
            motor.stop(1)
    elif kp.getKey('LEFT'): #if press 'LEFT' key turn left
        result = ults.checkFrontDistance(30)# checking the Front limit distance at 30cm
        if result == True:
            print("turnng left")
            GPIO.output(5,GPIO.LOW)
            motor.move(0.6,0.4,0.1) #motor turn at '60%'speed with '0.3' turning and 100ms delay
        else:
            print("limit is over")
            GPIO.output(5,GPIO.HIGH) #buzzer on
            motor.stop(1)
    elif kp.getKey('RIGHT'): #if press 'RIGHT'key turn right
        result = ults.checkFrontDistance(30)# checking the Front limit distance at 30cm
        if result == True :
            print("turning right")
            GPIO.output(5,GPIO.LOW)
            motor.move(0.6,-0.5,0.1) #motor run '60%' of speed with '-0.5'turning and '100ms'delay
        else:
            print("limit is over")
            GPIO.output(5,GPIO.HIGH) #buzzer on
            motor.stop(1)
    elif kp.getKey('q'): #for on
        GPIO.output(23,GPIO.LOW) # uv light on
    elif kp.getKey('w'): #for off
        GPIO.output(23,GPIO.HIGH) #uv light off
    elif kp.getKey('o'): # if press 'o' key turn ON relay  (for manuel control of relay)
        GPIO.output(14,GPIO.LOW) # it means the UV light turn on
    elif kp.getKey('f'): # if press 'f' key turn OFF relay
        GPIO.output(14,GPIO.HIGH) # it means the UV light turn off
        GPIO.output(5,GPIO.LOW)
    elif GPIO.input(15): # when the first pir sensor reads
        print("pir 2 ")
        GPIO.output(14,GPIO.LOW) # the UV light turn off
        GPIO.output(5,GPIO.HIGH) #buzzer on
        print("Humen detected")
    elif GPIO.input(18): # when the second pir sensor reads
        print("pir 1 ")
        GPIO.output(14,GPIO.LOW) # the UV light turn off
        GPIO.output(5,GPIO.HIGH) #buzzer on
        print("Humen detected")

    else :
        motor.stop(0.2) # else motor delay for 200ms

if __name__ == '__main__': #when run this code the __name__ is return to __main__
    while True:
        main() # then work the main function