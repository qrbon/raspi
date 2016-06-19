import RPi.GPIO as GPIO
import time
import subprocess
import os
from bon_generator import generate_bon
from multiprocessing import Process

process = Process(target=generate_bon)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)
    while True:
        if GPIO.wait_for_edge(17, GPIO.FALLING):
            GPIO.output(22, GPIO.HIGH)
            GPIO.output(23, GPIO.LOW)
            generate_show_code()

        if GPIO.wait_for_edge(17, GPIO.RISING):
            GPIO.output(22, GPIO.LOW)
            GPIO.output(23, GPIO.HIGH)


def generate_show_code():
    global process
    if "process" in globals() and process.is_alive():
        print("terminating")
        process.terminate()

    process = Process(target=generate_bon)
    process.start()


if __name__ == '__main__':
    main()
