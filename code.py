import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

LED = [24, 25, 8, 7, 12, 16, 20, 21]

def LightUp(ledNumber, period):
    GPIO.output(LED[ledNumber], 1)
    time.sleep(period)
    GPIO.output(LED[ledNumber], 0)


def blink(ledNumber, blinkCount, blinkPeriod):
    i = 0
    while i < blinkCount:
        LightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
        i += 1


def runningLight(count, period):
    j = 0
    while j < count:
        for i in range(len(LED)):
            LightUp(i, period)
        j += 1


def runningDark(count, period):
    GPIO.output(LED[0], 1)
    GPIO.output(LED[1], 1)
    GPIO.output(LED[2], 1)
    GPIO.output(LED[3], 1)
    GPIO.output(LED[4], 1)
    GPIO.output(LED[5], 1)
    GPIO.output(LED[6], 1)
    GPIO.output(LED[7], 1)
    j = 0
    while j < count:
        for i in range(len(LED)):
            GPIO.output(LED[i], 0)
            time.sleep(period)
            GPIO.output(LED[i], 1)
        j += 1
    GPIO.output(LED[0], 0)
    GPIO.output(LED[1], 0)
    GPIO.output(LED[2], 0)
    GPIO.output(LED[3], 0)
    GPIO.output(LED[4], 0)
    GPIO.output(LED[5], 0)
    GPIO.output(LED[6], 0)
    GPIO.output(LED[7], 0)


def decToBinList(decNumber):
    s = str(bin(decNumber))
    s = s[2:]
    i = len(s) - 1
    j = 0
    A = [0]*8
    while i >= 0:
        A[j] = s[i]
        i -= 1
        j += 1
    return A


def lightNumber(number):
    BinList = decToBinList(number)
    print(*BinList)
    for i in range(len(BinList)):
        if int(BinList[i]) == 1:
            GPIO.output(LED[i], 1)
    time.sleep(1)
    GPIO.output(LED[0], 0)
    GPIO.output(LED[1], 0)
    GPIO.output(LED[2], 0)
    GPIO.output(LED[3], 0)
    GPIO.output(LED[4], 0)
    GPIO.output(LED[5], 0)
    GPIO.output(LED[6], 0)
    GPIO.output(LED[7], 0)


def runningPattern(pattern, direction):          

