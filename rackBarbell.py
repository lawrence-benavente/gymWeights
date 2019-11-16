#! python3
# rackBarbell.py - Output the least amount of plates needed per side. 

import sys

#Establish constants
bar 	= 45
blue 	= 45
yellow	= 35
green	= 25
white 	= 10
red 	= 5
black	= 2.5
platesColor = [blue, yellow, green, white, red, black]
	
#Pull total weight from command line
totalWeight = int(sys.argv[1])
try:
	percentageOff = int(sys.argv[2])
except:
	percentageOff = 0
percentage = (100 - percentageOff)/100

#Find out how much per side and unusuable weight
percentageWeight= totalWeight * percentage
neededWeight 	= percentageWeight - bar
perSideWeight 	= neededWeight / 2
unusableWeight	= perSideWeight % platesColor[-1]
if perSideWeight >= platesColor[0]*2:		#Add weights with more than 2x largest plate
	multipleOf45 	= int(perSideWeight / platesColor[0])
	excessAfter45 	= perSideWeight % ((platesColor[0])*2) #Add excess in multiples of two to avoid 70 per side problem
else:
	multipleOf45 = 0
	excessAfter45 = perSideWeight

#If weight less than bar catch
if percentageWeight <= bar:
	print('No weights necessary \nTotal Weight: %.1f' %percentageWeight)

else:
	# Create empty arrays for each plate
	totalPlates		= []
	bluePlates 		= []
	newBluePlates	= [] #To adjust for multiples of each 45 plate
	yellowPlates 	= []
	greenPlates 	= []
	whitePlates 	= []
	redPlates 		= []
	blackPlates		= []
	platesArray = [bluePlates, yellowPlates, greenPlates, whitePlates, redPlates, blackPlates]

	#Find easiest way to split up using (45, 35, 25, 10, 5, 2.5)
	for i in range(len(platesArray) - 1): #reestablish constants
		#Round out multiple of largest plate 
		pSW = excessAfter45
		totalPlates.append(0)
		plates 	= platesColor
		if i != len(plates):
			plates[i] = 0
		for j in range(len(plates)):
			try:		#Cannot divide by zero
				addCount = int(pSW / plates[j])
			except:
				addCount = 0
			platesArray[j].append(addCount)
			pSW -= plates[j] * addCount
			totalPlates[i] += addCount
	newBluePlates = [x + multipleOf45 for x in bluePlates]	#Add on multiple of blue plates
	newPlatesArray = [newBluePlates, yellowPlates, greenPlates, whitePlates, redPlates, blackPlates]

	#Find and print total plates needed
	minP = totalPlates.index(min(totalPlates))
	print('Total Weight: %d 	 Weight Per Side: %.1f' %(percentageWeight, perSideWeight))
	
	#Output colors and weight
	print('%d blue plates 	(%d) \n%d yellow plates	(%d) \n%d green plates 	(%d) \n%d white plates 	(%d) \n%d red plates 	(%d) \n%d black plates 	(%.1f)' 
		%(newBluePlates[minP], blue, yellowPlates[minP], yellow, greenPlates[minP], green, whitePlates[minP], white, redPlates[minP], red, blackPlates[minP], black))
	if unusableWeight != 0:
		print('Weight unable to add per side %.1f' %unusableWeight)