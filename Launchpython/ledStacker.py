import sys
import time
import os

stack = []
stack.append([['3', '7', 'B', 'F', 'E', 'D', 'C'], ['2', '6', 'A', '9', '8'], ['1', '4', '5'], ['0']])
stack.append([['C', 'D' ,'E' ,'F'], ['8', '9', 'A', 'B', '7', '3'], ['0', '2', '4', '5', '6'], ['1']])
stack.append([['C', 'D', 'E', 'F'], ['0', '4', '8', '9', 'A', 'B'], ['1', '5', '6', '7', '3'], ['2']])
stack.append([['0', '4', '8', 'C', 'D', 'E', 'F'], ['1', '5', '9', 'A', 'B'], ['2', '6', '7'], ['3']])
stack.append([['3', '7', 'B', 'F'], ['2', '6', 'A', 'E', 'D', 'C'], ['0', '1', '5', '9', '8'], ['4']])
stack.append([[], ['3', '7', 'B', 'C', 'D', 'E', 'F'], ['0', '1', '2', '4', '6', '8', '9', 'A'], ['5']])
stack.append([[], ['0', '4', '8', 'C', 'D', 'E', 'F'], ['1', '2', '3', '5', '7', '9', 'A', 'B'], ['6']])
stack.append([['0', '4', '8', 'B'], ['1', '5', '9', 'D', 'E', 'F'], ['3', '2', '6', 'A', 'B'], ['7']])
stack.append([['3', '7', 'B', 'F'], ['0', '1', '2', '6', 'A', 'E'], ['4', '5', '9', 'C', 'D'], ['8']])
stack.append([[], ['0', '1', '2', '3', '7', 'B', 'F'], ['4', '5', '6', '8', 'A', 'C', 'D', 'E'], ['9']])
stack.append([[], ['C', '8', '4', '0', '1', '2', '3'], ['5', '6', '7', '9', 'B', 'D', 'E', 'F'], ['A']])
stack.append([['0', '4', '8', 'C'], ['D', '9', '5', '1', '2', '3'], ['E', 'D', 'A', '6', '7'], ['B']])
stack.append([['0', '1', '2', '3', '7', 'B', 'F'], ['4', '5', '6', 'A', 'E'], ['8', '9', 'D'], ['C']])
stack.append([['0', '1', '2', '3'], ['4', '5', '6', '7', 'B', 'F'], ['C', '8', '9', 'A', 'E'], ['D']])
stack.append([['0', '1', '2', '3'], ['C', '8', '4', '5', '6', '7'], ['D', '9', 'A', 'B', 'F'], ['E']])
stack.append([['C', '8', '4', '0', '1', '2', '3'], ['D', '9', '5', '6', '7'], ['E', 'A', 'B'], ['F']])

inputList = []
inputListTemp = []
iterat = []
times = []

data = []
previous = []

while 1:
	data = []
	previous = []

	isEmpty = os.stat("re_input").st_size == 0
	if(not isEmpty):
		with open("re_input", 'r+') as inputFile:
			for line in inputFile:
				inputList.append([])
				inputListTemp.append([])
				inputList[len(inputList)-1] = stack[int(line[0], 16)][:]
				inputListTemp[len(inputListTemp)-1] = stack[int(line[0], 16)][:]
				iterat.append(4)
				times.append(0)
		
			inputFile.truncate(0)

	for j in range(0, len(inputList)):
		if iterat == -1:
			del inputList[j]
			del inputListTemp[j]
			del iterat[j]
			del times[j]
			j -= 1

		elif (iterat[j] == 0) and (time.time() - times[j]) >= 0.250:
			if len(inputListTemp[j]) > 0:
				previous.append(inputListTemp[j].pop())

			iterat[j] -= 1

		elif (time.time() - times[j]) >= 0.250:
			if iterat[j] < 4 and len(inputListTemp[j]) > 0:
				previous.append(inputListTemp[j].pop())

			if len(inputList[j]) > 0:
				data.append(inputList[j].pop())
				
			times[j] = time.time()
			iterat[j] -= 1

	with open('leds', 'a') as file:
			for button in previous:
				for dt in button:
					file.write('O' + dt + '\n')

			for button in data:
				for dt in button:
					file.write('X' + dt + '\n')
