import RPi.GPIO as GPIO
import signal
import sys
import time

GPIO.setmode(GPIO.BCM)

rows = [14, 4, 3, 2]
columns = [24, 23, 22, 27]
data = []

for i in rows:
	GPIO.setup(i, GPIO.OUT)

for j in columns:
	GPIO.setup(j, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def signal_handler(signal, frame):
	for i in rows:
		GPIO.output(i, GPIO.LOW)

	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

while 1:
	time.sleep(0.25)
	for i in range(0,4):
		GPIO.output(rows[i], GPIO.HIGH)		

		for j in range(0, 4):
			if GPIO.input(columns[j]):
				data.append(hex(j*4+i).upper()[2])
		
		time.sleep(0.001)

		GPIO.output(rows[i], GPIO.LOW)

	with open('input', 'a') as file:
		for dt in data:
			file.write(dt+'\n')

	data = []
