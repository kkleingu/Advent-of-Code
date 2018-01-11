from collections import Counter
data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()
myinput = myinput.split('\n')

path = [int(i) for i in myinput]# turns stings into ints

#path = [0,3,0,1,-3]

##### Part 1 #######
##step = 0
##location = 0
##while True:
##    travel = path[location]
##    newlocation = location + travel
##    path[location] += 1
##    location = newlocation
##    step +=1
##    #print(step, location)
##    #print(path)
##    if location > len(path) -1: #we are outside
##        break
##print(step)


##### Part 2 #######
step = 0
location = 0
while True:
    travel = path[location]
    newlocation = location + travel
    if travel >= 3:
        path[location] -= 1
    else:
        path[location] += 1
    location = newlocation
    step +=1
    #print(step, location)
    #print(path)
    if location > len(path) -1: #we are outside
        break
print(step)




