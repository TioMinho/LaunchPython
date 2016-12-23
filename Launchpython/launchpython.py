import pygame as pg
import os

#                  FUNCTIONS                    #
#################################################
def loadSamplePack(folder):
	samples = []; channels = []

	for i in range(0, 16):
		channels.append(pg.mixer.Channel(i))

	for i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
		temp = pg.mixer.Sound(folder + "/" + i + ".wav")
		temp.set_volume(1)
		samples.append(temp)

	return (samples, channels)	


#                 CONFIGURATIONS                #
#################################################
# Configure the initial configuration for the mixer
freq = 44100
bitsize = -16
channels = 16
buffer = 2048

pg.mixer.init(freq, bitsize, channels, buffer)
pg.mixer.set_num_channels(channels)

# Configure the defaults folders and samples
samples = []; channels = []
directories = []; currentDir = 0;

with open("directories") as dir:
	for lines in dir:
		directories.append(lines.replace('\n', ""))

(samples, channels) = loadSamplePack(directories[0])


#                   EXECUTION                   # 
#################################################

while 1:
	isEmpty = os.stat("input").st_size == 0
	if(not isEmpty):
		with open("input", 'r+') as inputFile:
			for line in inputFile:
				if line[0] == 'K':
					pg.mixer.stop()

					(samples, channels) = loadSamplePack(directories[currentDir])

				elif line[0] == 'N':
					if(currentDir < len(directories)-1):
						currentDir += 1
					else:
						currentDir = 0

				elif line[0] == 'P':
					if(currentDir > 0):
						currentDir -= 1
					else:
						currentDir = len(directories)-1

				else:
					button = int(line[0], 16)
					channels[button].set_volume(1)
					channels[button].play(samples[button])
					
					with open("re_input", 'a') as reinputFile:
						reinputFile.write(line[0]+'\n')
		
			inputFile.truncate(0)