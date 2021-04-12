import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.output(17, 1)
GPIO.setwarnings(False)

LED = [10, 9, 11, 5, 6, 13, 19, 26]

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
    for i in range(len(BinList)):
        if int(BinList[i]) == 1:
            GPIO.output(LED[i], 1)
        else:
            GPIO.output(LED[i], 0)


try:
    F = 0
    while F == 0:
        N = 7
        k = 128
        while N > 0:
            lightNumber(k)
            if GPIO.input(4) == 0:
                k -= 2**(N - 1)
            else:
                k += 2**(N - 1)
            N -= 1
            print(k)
            F = 1

        value = k
            
        V = round(value*3.3/255, 2)
        print("Digital value:", value, "| Analog value:", V, "V")
        time.sleep(0.1)
       

except KeyboardInterrupt:
    print("   Fine...")
except ValueError:
    print("I need a number")

finally:
    GPIO.output(LED, 0)
    GPIO.cleanup()