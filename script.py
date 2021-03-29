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
    while True:
        t = int(input("Введите время работы: "))
        f = int(input("Введите частоту: "))

        if f > 100000000000:
            print ("Давай поменьше что-нибудь")
            continue
        
        if t > 10:
            print ("Я так долго работать не буду")
            continue

        elif f < 0 or t < 0:
            print("Отрицательные числа у нас тут не приняты")
            continue

        else:
            break
    
    T = np.arange(0, t, 1/f)
    Q = []
    for i in T:
        Q.append(round(np.sin(i*2*3.14)*255/2 + 255/2))
    plt.plot(T, Q)
    plt.show()
    for j in Q:
        lightNumber(j)
        time.sleep(1/f)

except KeyboardInterrupt:
    print("   Ну ладно...")
except ValueError:
    print("Число, я сказал")

finally:
    GPIO.output(LED, 0)
    GPIO.cleanup()
