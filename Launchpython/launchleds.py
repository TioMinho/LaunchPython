import RPi.GPIO as GPIO
import signal
import sys
import os
import time

GPIO.setmode(GPIO.BCM)

rows = [7, 8, 11, 9]
columns = [10, 25] # Multiplexer
pins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def signal_handler(signal, frame):
	for i in rows:
		GPIO.output(i, GPIO.LOW)
	for j in columns:
		GPIO.output(j, GPIO.LOW)

	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

for i in rows:
	GPIO.setup(i, GPIO.OUT)

for j in columns:
	GPIO.setup(j, GPIO.OUT)

while 1:
	for i in range(0,4):
		if(i == 0):
			GPIO.output(columns[0], GPIO.LOW)
			GPIO.output(columns[1], GPIO.LOW)
		elif(i == 1):
			GPIO.output(columns[0], GPIO.HIGH)
			GPIO.output(columns[1], GPIO.LOW)
		elif(i == 2):
			GPIO.output(columns[0], GPIO.LOW)
			GPIO.output(columns[1], GPIO.HIGH)
		elif(i == 3):
			GPIO.output(columns[0], GPIO.HIGH)
			GPIO.output(columns[1], GPIO.HIGH)

		for j in range(0, 4):
			if(pins[j*4 + i] == 1):
				GPIO.output(rows[j], GPIO.HIGH)
			else:
				GPIO.output(rows[j], GPIO.LOW)

			time.sleep(0.0008)

			GPIO.output(rows[j], GPIO.LOW)

	isEmpty = os.stat("leds").st_size == 0
	if(not isEmpty):
		with open("leds", 'r+') as inputFile:
			for line in inputFile:
				if(line[0] == 'X'):
					pins[int(line[1], 16)] = 1
				elif(line[0] == 'O'):	
					pins[int(line[1], 16)] = 0		
	
			inputFile.truncate(0)
