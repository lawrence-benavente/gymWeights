#! python3
# rackMultipleWeights.py - Input (the number for rep max, the weight for rep max from previous number, reps for each set separated by spaces) Output- weight and how much per side.

import sys, logging

#Set Up Logging
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")
logging.disable(logging.CRITICAL) #Will delete logging info

#Establish Constants
bar			= 45
bluePlate	= 45
yellowPlate	= 35
greenPlate	= 25
whitePlate	= 10
redPlate	= 5
blackPlate	= 2.5
plateArray	= [bluePlate, yellowPlate, greenPlate, whitePlate, redPlate, blackPlate]

#From strengthlevel.com, percentage of 1RM for #RM's
repPercentage = [1.00, 0.97, 0.94, 0.89, 0.86, 0.83, 0.81, 0.78, 0.75, 0.73, 0.71, 0.70, 0.68, 0.67, 0.65, 0.64, 0.63, 0.61, 0.60, 0.59, 0.58, 0.57, 0.56, 0.55, 0.54, 0.53, 0.52, 0.51, 0.50]

#Pull total weight from command line
logging.info("Starting to find the sets and reps")
repRange 	= []
numberRM 	= int(sys.argv[1])
RM 			= numberRM - 1
numberRM 	= int(sys.argv[2])
oneRM 		= numberRM / repPercentage[RM]

try:
	for i in range(10):
		repRange.append(int(sys.argv[i+3]))
		logging.debug("For set %s there are %s reps", i,repRange[i])
except:
	pass
	logging.debug("There are %s sets total", i)
logging.info("Finished finding the sets and reps")

#Create new array of new weights 
totalWeight	= []
for j in range(len(repRange)):
	placement = repRange[j] - 1 #placement should equal reprange 
	totalWeight.append(int(repPercentage[placement] * oneRM))
	logging.debug("For set %s the weight is %s", j,totalWeight[j])

def platesNeeded(weight, set): #Input weight needed, output plates needed per side
	neededWeight	= weight - bar
	perSideWeightBeforeExcess	= neededWeight / 2
	logging.debug("Weight needed per side of set %s is %s per side before subtracting excess", set, perSideWeightBeforeExcess)
	unusableWeight 	= perSideWeightBeforeExcess % plateArray[-1]
	perSideWeight = perSideWeightBeforeExcess - unusableWeight 
	weightPerSide.append(perSideWeight)

	#If weight less than bar print no weights neccessary
	if weight <= bar:
		print("No weights neccessary")
	#Find the plates needed
	else:
		for plates in range(len(plateArray)):
			plateColorNeeded = int(perSideWeight / plateArray[plates])
			perSideWeight 	 = perSideWeight % plateArray[plates]
			setPlatesNeeded[set].append(plateColorNeeded)
			logging.debug("For set %s %s plate at weight %s is needed total weight is %s", set,plateColorNeeded, plateArray[plates], perSideWeight)
			if plates == len(plateArray) - 1:
				excessWeight.append(perSideWeight)
				logging.debug("Excess weight for set %s is %s", set,excessWeight[set])
				logging.debug("Weight needed per side of set %s is %s per side after subtracting excess", set, perSideWeight)

#Print plates needed for first set
def printWeightsNeeded(set):
	platesNeededperSet = setPlatesNeeded[set]
	print('Set ' + str(set + 1))
	print('Total Weight: %d 	Weight Per Side: %d' %(totalWeight[set], weightPerSide[set]))
	for plates in range(len(plateArray)):
		if plates == 0:
			plate = "blue plate(s)		(45)"
		if plates == 1:
			plate = "yellow plate(s)	(35)"
		if plates == 2:
			plate = "green plate(s)	(25)"
		if plates == 3:
			plate = "white plate(s)	(10)"
		if plates == 4:
			plate = "red plate(s)		(5)"
		if plates == 5:
			plate = "black plate(s)	(2.5)"
		print(str(platesNeededperSet[plates]) + ' ' + plate)

#Find out how much weight per side needed to remove
def weightRemoval(weightChangeNumber, weight1, weight2):
	logging.info("Starting weight removal process")
	difference = weight1 - weight2
	if difference >= 0:
		sign = " subtract "
	else:
		sign = " add "
	logging.debug("During this transition one should%sweight", sign)
	print('Between set %d and %d' %(weightChangeNumber, weightChangeNumber + 1) + sign + str(difference) + ' lbs per side')

#Establish arrays necessary before using functions
setPlatesNeeded = []
weightPerSide	= []
excessWeight 	= []

#Solving for plates needed using "printPlatesNeeded"
for k in range(len(totalWeight)):
	logging.info("Started finding plates needed for set %s", k)
	setPlatesNeeded.append([]) #Add array for set
	platesNeeded(totalWeight[k], k)
	logging.info("Finished finding plates needed for set %s", k)
logging.debug("Array for setPlatesNeeded %s", setPlatesNeeded)
logging.debug("Array for weightPerSide %s", weightPerSide)
logging.debug("Array for excessWEight %s", excessWeight)

#Printing plates needed using function "printWeightsNeeded"
for l in range(len(setPlatesNeeded)):
	print('')
	logging.info("Starting to print set weights and plates needed")
	printWeightsNeeded(l)
	logging.info("Finished printing set weights and plates needed")

#Add a space for formatting
print('')

#Find out and print plates needed to remove for each set
for m in range(len(weightPerSide) - 1):
	weightChangeNumber = m + 1
	logging.info("Starting to print weights needed to remove")
	weightRemoval(weightChangeNumber, weightPerSide[m], weightPerSide[m + 1])
	logging.info("Finished printing weights needed to remove")