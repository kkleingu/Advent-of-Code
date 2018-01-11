from collections import Counter

data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()#.strip('\n')




#####Part 1 ######
##myinput = myinput.split(',')
##myinput = [int(i) for i in myinput]
##lengths = myinput
###lengths = [3, 4, 1, 5]
##
##listofnumbers = [i for i in range(256)]
##currentposition = 0
##skipsize = 0
##
##for i in range(len(lengths)):
##    swapsize = lengths[i]
##    if currentposition + swapsize > len(listofnumbers): #Needs to loop around
##        runover = currentposition + swapsize - len(listofnumbers)
##        tobereversed = listofnumbers[currentposition:] +listofnumbers[0: runover]
##        tobereversed.reverse()
##        listofnumbers[currentposition:] = tobereversed[0: (len(listofnumbers)-currentposition)]
##        listofnumbers[0: runover] = tobereversed[(len(listofnumbers)-currentposition):]
##        
##    else:
##        tobereversed = listofnumbers[currentposition: (currentposition+swapsize)]
##        tobereversed.reverse()
##        listofnumbers[currentposition: (currentposition+swapsize)] = tobereversed
##
##    currentposition += lengths[i] +skipsize
##    x= lengths[i] +skipsize
##    skipsize +=1
##    if currentposition >= len(listofnumbers): #needs to loop back around in a circle
##        currentposition -= len(listofnumbers)  
##    #print(listofnumbers)
##    #print(listofnumbers[currentposition])
##print(listofnumbers)
##print(listofnumbers[0] * listofnumbers[1])

#####Part 2 ######

#myinput = ''

ASCIICodes = {}
ASCIICodes[','] = 44
ASCIICodes['0'] = 48
ASCIICodes['1'] = 49
ASCIICodes['2'] = 50
ASCIICodes['3'] = 51
ASCIICodes['4'] = 52
ASCIICodes['5'] = 53
ASCIICodes['6'] = 54
ASCIICodes['7'] = 55
ASCIICodes['8'] = 56
ASCIICodes['9'] = 57

suffix = [17, 31, 73, 47, 23]

lengths = []
for i in myinput:
    lengths.append(ASCIICodes[i])
lengths += suffix

#print(lengths)

listofnumbers = [i for i in range(256)]
currentposition = 0
skipsize = 0

for j in range(64):
    #print(j, skipsize)
    for i in range(len(lengths)):
        swapsize = lengths[i]
        if currentposition + swapsize > len(listofnumbers): #Needs to loop around
            #runover = currentposition + swapsize - len(listofnumbers)
            runover = (currentposition + swapsize) % len(listofnumbers)
            tobereversed = listofnumbers[currentposition:] +listofnumbers[0: runover]
            tobereversed.reverse()
            listofnumbers[currentposition:] = tobereversed[0: (len(listofnumbers)-currentposition)]
            listofnumbers[0: runover] = tobereversed[(len(listofnumbers)-currentposition):]
        
        else:
            tobereversed = listofnumbers[currentposition: (currentposition+swapsize)]
            tobereversed.reverse()
            listofnumbers[currentposition: (currentposition+swapsize)] = tobereversed

        currentposition += lengths[i] +skipsize
        x= lengths[i] +skipsize
        skipsize +=1
        if currentposition >= len(listofnumbers): #needs to loop back around in a circle
            currentposition = currentposition % len(listofnumbers)
        #print(skipsize)
    #print(listofnumbers)
    #print(listofnumbers[currentposition])

#listofnumbers = [i for i in range(256)]
#listofnumbers[0:16] = [65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22] 
#listofnumbers[16:32] = [65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22] 

sparsehash = listofnumbers
densehash = []

#print(sparsehash)

for dh in range(16):
    first = 16* dh 
    second = 16* dh + 16
    numbers = sparsehash[first:second]
    #print(numbers)
    #print(first, second)
    out = numbers[0]
    for i in range(1,len(numbers)):
        out = out ^ numbers[i]
    densehash.append(out)   

#print(densehash)

#densehash = [64, 7, 255]
finalhex = ''
for i in densehash:
    temp = hex(i)
    if len(temp) == 3:
        finalhex += '0'+ temp[2]
    else:
        finalhex += temp[2] + temp[3]
print(finalhex)








