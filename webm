#!/usr/bin/env python
from subprocess import call
from sys import argv
import re

# Regexs

regex_resize = ur'^(?:-resize|-r)=(\d+)?[x,](\d+)?'
regex_time = ur'^(?:-time|-t)=([\d:]*)(?:$|\-([\d:]*)$)'
filenameReg = ur'(.+)(\.\w+)'


noSound   = False
resize    = False
startTime = False
elapse    = False
timed     = False

# Info
if len(argv) == 1:
	print "webm.py FILENAME\n-ns -> No audio\nt=[START FROM]-[DURATION] -> Trims the video duration, use 00:00:00 format or seconds\n[WIDTH]x[HEIGHT] -> Blank keeps aspect ratio - Examples: 640x480 , 640x , x480"
	quit()

# Parameters
for i in argv:

	# Check if Sound Off
	
	if i == "-nosound" or "-ns":
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

command = []
command.append("ffmpeg")
if timed:
	if startTime:
		command.append("-ss")
		command.append(startTime)
	if elapse:
		command.append("-t")
		command.append(elapse)
command.append("-i")
command.append(filename + filenameext)
command.append("-c:v")
command.append("libvpx")
command.append("-crf")
command.append("32")
command.append("-b:v")
command.append("900K")
command.append("-threads")
command.append("1")
if noSound:
	command.append("-an")
else:
	command.append("-c:a")
	command.append("libvorbis")
if resize:
	command.append("-vf")
	command.append("scale=" + width + ":" + height)
command.append(filename + ".webm")

print command

# Call the command

call(command)

quit()
