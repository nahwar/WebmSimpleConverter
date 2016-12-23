#!/usr/bin/env python
from subprocess import call
from sys import argv
import re

# Regexs

regex_resize = r'^(\d+)?x(\d+)?'
regex_time   = r'^([\d:]*)(?:$|-([\d:]*)$)'
filenameReg  = r'(.+)(\.\w+)'


noSound   = False
resize    = False
startTime = False
elapse    = False
timed     = False

# Info
if len(argv) == 1:
	print "webm.py FILENAME\n-ns -> No audio\n[START FROM]-[DURATION] -> Trims the video duration, use 00:00:00 format or seconds\n[WIDTH]x[HEIGHT] -> Blank keeps aspect ratio - Examples: 640x480 , 640x , x480"
	quit()

# Parameters
for i in argv:

	# Check if Sound Off

	if i == "-nosound" or i == "-ns":
		soundstring = i
		noSound     = True

	# Check if Resize parameters
	if re.search(regex_resize, i):
		match = re.search(regex_resize, i)

		if match.group(1) is None:
			width = "-1"
		else:
			width = match.group(1)

		if match.group(2) is None:
			height = "-1"
		else:
			height = match.group(2)
		resize = True

	# Check if Time frame
	if re.search(regex_time, i):
		match = re.search(regex_time, i)

		if match.group(1) is not None:
			startTime = match.group(1)
		if match.group(2) is not None:
			elapse = match.group(2)
		timed = True

	# Get filename
	if re.search(filenameReg, i):
		match = re.search(filenameReg, i)

		filename    = match.group(1)
		filenameext = match.group(2)

# Create Command

command = []                                       		# Create array
command.append("ffmpeg")                           		# ffmpeg
if timed:                                          		# Check if timed
	if startTime:
		command.append("-ss")
		command.append(startTime)
	if elapse:
		command.append("-t")
		command.append(elapse)
command.append("-i")
command.append(filename + filenameext)             		# File to convert
command.append("-c:v")                             		# Video Codec
command.append("libvpx")                           		# Video Codec
command.append("-crf")                             		# Quality settings
command.append("32")                               		# Quality settings
command.append("-b:v")                             		# Quality settings - Bitrate
command.append("900K")                             		# Quality settings - Bitrate
command.append("-threads")                         		# Quality settings - Threads
command.append("1")                                		# Quality settings - Threads
if noSound:
	command.append("-an")                          		# Disable sound
else:
	command.append("-c:a")                         		# Audio Codec
	command.append("libvorbis")                    		# Audio Codec
if resize:
	command.append("-vf")                          		# Size
	command.append("scale=" + width + ":" + height)		# Size
command.append(filename + ".webm")                 		# New Filename

print command

# Call the command

call(command)

quit()
