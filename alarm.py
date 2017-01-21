import time
import webbrowser
import random
import os

#Check if the user has the YT.txt file in the same area as alarm.py
check = True 
if os.path.isfile("YT.txt") == False:
	print "ERROR: YT.txt file not present"
	print 'Alarm Video cannot be opened'
	check = False

#The User can set the time they want to wake up. The String the user puts in must be the same as the example to work.
print "What time do you want to wake up?"
print "Use this form.\nExample: 06:30"
Alarm = raw_input("> ")

Time = time.strftime("%H:%M")

with open("YT.txt") as f:
	content = f.readlines()

while Time != Alarm:
	print "The time is " + Time
	Time = time.strftime("%H:%M")
	time.sleep(1)

if Time == Alarm:

	print "Time to Wake up!"
	if check :
		random_video = random.choice(content)
		webbrowser.open(random_video)
