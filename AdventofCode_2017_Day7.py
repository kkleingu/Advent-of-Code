from collections import Counter

data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()#.strip('\n')
myinput = myinput.split('\n')

#myinput = ['pbga (66)','padx (45) -> pbga, havc, qoyq']

data = []
toplayer = []
bottomlayer = []
for i in myinput:
    splitTerm = i.strip(')').split(' (')
    splitTerm2 = splitTerm[1].split(') -> ')
    if len(splitTerm2) == 1:
        data.append([splitTerm[0],int(splitTerm2[0])])
        toplayer.append([splitTerm[0],int(splitTerm2[0])])
    else:
        subtowers = splitTerm2[1].split(', ')
        data.append([splitTerm[0],int(splitTerm2[0]),subtowers])
        bottomlayer.append([splitTerm[0],int(splitTerm2[0]),subtowers])

#####Part 1 ######
#Make a list of names of towers and the ones they are supporting
#In theory the name that only appears once will be the base
##towers = []
##for i in data:
##    if len(i) == 2:
##        towers.append(i[0])
##    else:
##        towers.append(i[0])
##        towers +=  i[2]
##organizedTowers = Counter(towers)
###names = towers.keys()
##for name in organizedTowers:
##    if organizedTowers[name] == 1:
##        print(name)

  
#####Part 2 ######
#del x[1]
weightDict = {}        
for i in toplayer:
    weightDict[i[0]] = i[1]
counting = 1

relevantvalues = []
while len(bottomlayer)>0:
    #print(counting)
    tobedeleted = []
    for i in range(len(bottomlayer)):
        allinlist = False
        listofnames = []
        listofweights = []
        for j in bottomlayer[i][2]:
            if j in weightDict:
                listofnames.append(j)
                listofweights.append(weightDict[j])
                
        if len(listofweights) == len(bottomlayer[i][2]):
            allinlist = True
            if listofweights.count(listofweights[0]) != len(listofweights): #### The weights are equal
                for k in range(len(listofweights)):
                    if listofweights[k] != listofweights[0]:
                        average = float(sum(listofweights))/len(listofweights)
                        tempaverage = float((listofweights[k] + (len(listofweights)-1) * listofweights[0]))/len(listofweights)
                        if tempaverage == average: #k is bad
                            #print(listofnames[k],listofweights[0],(listofweights[0]-listofweights[k]))
                            print(listofnames,listofweights)
                            relevantvalues.append([listofnames[k],(listofweights[0]-listofweights[k])]) #Bad Value and how much its off
                        elif k == 0:
                            relevantvalues = [listofnames[0],(listofweights[1]-listofweights[0])]
                        else:
                            #print(listofnames[0],(listofweights[0]-listofweights[k]))
                            relevantvalues.append([listofnames[k],(listofweights[0]-listofweights[k])])
                            print(listofnames,listofweights)
   

            weightDict[bottomlayer[i][0]] = bottomlayer[i][1] + sum(listofweights)        
            tobedeleted.append(i)
            
    tobedeleted.reverse() # So the smaller numbers don't mess up location of larger numbers
    for i in tobedeleted:
        del bottomlayer[i]
    counting+=1
    #print(bottomlayer)
print('ok')
for i in data:
    #print(i[0])
    if i[0] == 'dqwocyn':
        print(i[1])
    if i[0] == relevantvalues[0][0]:
        print(i[1])
        print(i[1] + relevantvalues[0][1])
