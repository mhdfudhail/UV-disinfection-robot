import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def checkFrontDistance(limitation):
    TRIG = 20
    GPIO.setup(TRIG,GPIO.OUT)
    ECHO = 21
    GPIO.setup(ECHO,GPIO.IN)
    i = 0
    verification = False
    avgDistance = 0
    for i in range(5):
        GPIO.output(TRIG, False)
        time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance,2)
    avgDistance=avgDistance+distance

    print(" Front Distance" + str(avgDistance))

    if avgDistance < limitation:
        verification = False
    if avgDistance > limitation:
        verification = True
    return verification


def checkBackDistance(limitation):
    TRIG = 8
    GPIO.setup(TRIG,GPIO.OUT)
    ECHO = 7
    GPIO.setup(ECHO,GPIO.IN)
    i = 0
    verification = False
    avgDistance = 0
    for i in range(5):
        GPIO.output(TRIG, False)
        time.sleep(0.1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance,2)
    avgDistance=avgDistance+distance

    print("Back Distance" + str(avgDistance))

    if avgDistance < limitation:
        verification = False
    if avgDistance > limitation:
        verification = True
    return verification