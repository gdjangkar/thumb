#!/usr/bin/python3

import sys
import datetime
import csv

def read_file(events):
	
	#filename = input("Enter a filename to read > ");
	
	with open("dates.txt", "r") as csvfile:
		f = csv.reader(csvfile, delimiter=',')
		flist = list(f)

	#print (flist[0][1])
	
	events = []

	for i in range (0,len(flist)):
		
		j = 0
		tmp = []
		while (j < 4):
			if (j == 0):
				tmp.append(flist[i][j])
			elif (j == 3):
				
				day = int(flist[i][1])
				month = int(flist[i][2])
				year = int(flist[i][3])
				
				tmpDate = datetime.date(year, month, day)
				tmp.append(tmpDate)
			j += 1
		events.append(tmp)
		
	#print (events)
	
	return events

def save_file(events):
	
	f = open("dates.txt", "w")
	
	# Extract description and dates from current event list

	i = 0

	for i in range (0, len(events)):
		tmp = ""
		for j in range (0, 2):
			if (j == 0):
				tmpDesc = events[i][j]
			else:
				tmpDate = str(events[i][j].day)
				tmpMonth = str(events[i][j].month)
				tmpYear = str(events[i][j].year)
		
		tmp = tmpDesc + ',' + tmpDate + ',' + tmpMonth + ',' + tmpYear + '\n'
		
		#tmp.extend((tmpDesc, tmpDate, tmpMonth, tmpYear))
		
		f.write(tmp)

	# Add into comma-separated lines on file pointer
	
	f.close()
	
	print ("File saved successfully")

def command_n(events):
	tmpDesc = input("Enter event description > ")
	
	day = int(input("Enter event date > "))
	month = int(input("Enter event month > "))
	year = int(input("Enter event year > "))
	
	tmpDate = datetime.date(year, month, day)
	
	event = [tmpDesc, tmpDate]
	
	events.append(event)
	
	return events

def command_p(events):
	
	if (len(events) > 2):
		events = sorted(events, key=lambda tup: tup[1])
	
		for event in events:	
			print ("You have " + event[0], end=" ")
			print ("on " + str(event[1].day) + "/" + str(event[1].month) + "/" + str(event[1].year))
	else:	
		print ("You have " + events[0], end=" ")
		print ("on " + str(events[1].day) + "/" + str(events[1].month) + "/" + str(events[1].year))
		
	return events

def command_d(events):
	
	i = 0
	
	for i in range (0, len(events)):
		print (str(i+1) + " :", end=" ")
		print (events[i][0] + ", " + str(events[i][1]))
	
	delIndex = int(input("Enter event to delete > ")) - 1
	
	events.pop(delIndex)
	
	return events

def command_s(events):
	
	searchWord = input("Enter string to search > ")
	
	for i in range (0, len(events)):
		s1 = str(events[i][0]).find(searchWord)
		s2 = str(events[i][1]).find(searchWord)
		
		if ((s1 != -1) or (s2 != -1)):
			command_p(events[i])
	
	return events

if __name__ == "__main__":

	myEvents = []

	myEvents = read_file(myEvents)

	while (True):
		
		command = input("> ")
		
		if (command == "q"):
			save_file(myEvents)
			break
		elif (command == "n"):
			myEvents = command_n(myEvents)		
		elif (command == "p"):
			myEvents = command_p(myEvents)
		elif (command == "d"):
			myEvents = command_d(myEvents)
		elif (command == "s"):
			myEvents = command_s(myEvents)
