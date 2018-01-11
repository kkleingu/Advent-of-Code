data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()#.strip('\n')
myinput = myinput.split(',')


######## Part 1 ########

##directions = {}
##directions['n'] = [1,0]
##directions['ne'] = [0.5,0.5]
##directions['nw'] = [0.5,-0.5]
##directions['s'] = [-1,0]
##directions['se'] = [-0.5,0.5]
##directions['sw'] = [-0.5,-0.5]
##
##currentlocation = [0,0]
##
##for i in myinput:
##    currentlocation[0] += directions[i][0]
##    currentlocation[1] += directions[i][1]
##
##print(sum(currentlocation))


######## Part 2 ########

directions = {}
directions['n'] = [1,0]
directions['ne'] = [0.5,0.5]
directions['nw'] = [0.5,-0.5]
directions['s'] = [-1,0]
directions['se'] = [-0.5,0.5]
directions['sw'] = [-0.5,-0.5]

currentlocation = [0,0]
maxlocation = [0,0]

for i in myinput: 
    currentlocation[0] += directions[i][0]
    currentlocation[1] += directions[i][1]
    if sum(currentlocation)> sum(maxlocation):
        maxlocation = currentlocation[:]

print(sum(maxlocation))
