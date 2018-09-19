# Skittles solution by Logan Cantin

# IMPORTS
from math import ceil   #for calculating number of handfuls
from sys import stdin
data = stdin.read().split("\n")     #input

## INITIATING VARIABLES 
time = 0 #number of seconds taken to eat the skittles
skttls = {"orange":0, "blue":0, "green":0, "yellow":0, "pink":0, "violet":0, "brown":0, "red":0} #number of skittles by color

## FUNCTIONS
def endoftestcase(): #called at the end of a test case to calculate and output number of seconds taken to eat skittles
    # global keyword is used to reference the global time variable, not initiate a new, local one
    global time 
    global skttls

    #iterate through skittle colors
    for color in skttls:
        #for all colors other than red, calculate number of handfuls necessary to finish the skittles and multiply it by 13 to get total number of seconds, and add it to time
        if color != "red": 
            time += ceil(skttls[color]/7) * 13 
        #for red, add 16 seconds per skittle to time
        else:
            time += skttls["red"] * 16

    print(time) #output number of seconds taken
    
    #resetting varibles for next test case
    time = 0
    skttls = {"orange":0, "blue":0, "green":0, "yellow":0, "pink":0, "violet":0, "brown":0, "red":0}


for skittle in data: #iterate through input
    if skittle == "end of box":
        endoftestcase()
    else:
        skttls[skittle] += 1 #add one to the corresponding color for each skittle in the test case
