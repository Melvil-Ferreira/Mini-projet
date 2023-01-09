#!/usr/bin/env python3
import serial
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()
try:
    while True:
        if ser.in_waiting == "3":
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
except KeyboardInterrupt:
    exit()
