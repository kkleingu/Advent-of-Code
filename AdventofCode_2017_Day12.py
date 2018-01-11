#data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
data = open(r'/Users/kevinkleinguetl/Documents/Python_Projects/dev/AdventofCode/RawData.txt' , 'r')


myinput = data.read()#.strip('\n')
myinput = myinput.split('\n')

myinput = [i.split(' ') for i in myinput]

dictionaryinputs = {}


#myinput = [['0', '<->', '454,', '528,', '621,', '1023,', '1199']]
for i in myinput:
    if len(i) > 3:
        destinations = [] #Could have = [i[len(i)-1]], but I like ascending order
        for j in range(2,len(i)-1):
            destinations.append(i[j].strip(','))
        destinations.append(i[len(i)-1])
        dictionaryinputs[i[0]] = destinations
    else:
        dictionaryinputs[i[0]] = [i[2]]

######## Part 1 ########
##group = ['0']
##while True:
##    addedthisround = 0
##    for i in group:
##        potentialadditions = dictionaryinputs[i]
##        for j in potentialadditions:
##            if j not in group:
##                group.append(j)
##                addedthisround +=1
##    if addedthisround == 0:
##        break
##print(len(group))

######## Part 2 ########
group = ['0']
groupnumber = 1
notingroup = list(dictionaryinputs.keys())
notingroup.remove(group[0])
while len(notingroup) >0:
    while True:
        addedthisround = 0
        for i in group:
            potentialadditions = dictionaryinputs[i]
            for j in potentialadditions:
                if j not in group:
                    group.append(j)
                    notingroup.remove(j)
                    addedthisround +=1
        if addedthisround == 0:
            break
    #notingroup = dictionaryinputs.keys()
    #for todelete in group:
    groupnumber += 1
    if len(notingroup)> 0:
        group = [notingroup[0]]
        notingroup.remove(group[0])
    else:
        break    #Don't really need this

print(groupnumber)
