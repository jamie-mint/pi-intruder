#!/usr/bin/env python3

import argparse
import random
import time
import sys

from pythonosc import osc_message_builder
from pythonosc import udp_client


import RPi.GPIO as GPIO

BUTTON_GPIO = 18

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
                        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)


    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.RISING)
        client.send_message("/intruder", 1)
        print("Button pressed!")
        sys.stdout.flush()
