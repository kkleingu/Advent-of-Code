from collections import Counter
data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()
myinput = myinput.split('\t')

myinput = [int(i) for i in myinput]# turns stings into ints

memorybanks = myinput[:]
#memorybanks = [0, 2, 7, 0]

####### Part 1 #######
##cycles = 0
##allmemorybanks = [memorybanks]
##while True:
##    cycles += 1
##    maxbanklocation = memorybanks.index(max(memorybanks))
##    #print(maxbanklocation, memorybanks)
##    newmemorybanks = memorybanks[:]
##    newmemorybanks[maxbanklocation] = 0
##    location = maxbanklocation + 1
##    for i in range(max(memorybanks)):
##        if location >= len(memorybanks):
##            location = 0
##        newmemorybanks[location] = newmemorybanks[location] + 1
##        #print(i,newmemorybanks)
##        location += 1
##    if newmemorybanks in allmemorybanks:
##        break
##    allmemorybanks.append(newmemorybanks)
##    memorybanks = newmemorybanks[:]
##    #print(memorybanks)
##
##print(cycles, newmemorybanks)

##### Part 2 #######

cycles = 0
allmemorybanks = [memorybanks]
while True:
    cycles += 1
    maxbanklocation = memorybanks.index(max(memorybanks))
    #print(maxbanklocation, memorybanks)
    newmemorybanks = memorybanks[:]
    newmemorybanks[maxbanklocation] = 0
    location = maxbanklocation + 1
    for i in range(max(memorybanks)):
        if location >= len(memorybanks):
            location = 0
        newmemorybanks[location] = newmemorybanks[location] + 1
        #print(i,newmemorybanks)
        location += 1
    if newmemorybanks in allmemorybanks:
        allmemorybanks.append(newmemorybanks)
        break
    allmemorybanks.append(newmemorybanks)
    memorybanks = newmemorybanks[:]
    #print(memorybanks)

print(newmemorybanks)
print(cycles - allmemorybanks.index(newmemorybanks))


