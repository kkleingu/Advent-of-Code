data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read().strip('\n')

#####Part 1 ######
##summation = 0
##for i in range(len(myinput)):
##    if i+1 == len(myinput): # end of string
##        if int(myinput[i]) == int(myinput[0]):
##            summation += int(myinput[i])
##    else:
##        if int(myinput[i]) == int(myinput[i+1]):
##            summation += int(myinput[i])
##print(summation)

#####Part 2 ######

summation = 0
for i in range(len(myinput)):
    comparisondigit = int(i + len(myinput)/2)
    if comparisondigit >= len(myinput): #Circles back around
        comparisondigit -= len(myinput)
    if int(myinput[i]) == int(myinput[comparisondigit]):
        summation += int(myinput[i])
print(summation)

