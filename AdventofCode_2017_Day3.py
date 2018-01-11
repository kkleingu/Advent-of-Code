import math

#data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
#myinput = data.read()#.strip('\n')

##number = 368078
########## Part 1 ##########
##x = math.ceil(math.sqrt(number))
##if x%2 == 1: #Odd Number
##    sizeofbox = x
##else:
##    sizeofbox = x+ 1
##
##perimeter = 2* sizeofbox + 2* (sizeofbox - 2)
##cornersofbox = [sizeofbox**2, sizeofbox**2 - (sizeofbox-1),
##                sizeofbox**2 - 2* (sizeofbox-1),sizeofbox**2 - 3* (sizeofbox-1)]
##
##middlesofbox = [sizeofbox**2 - (sizeofbox-1)/2,
##                sizeofbox**2 - (sizeofbox-1)- (sizeofbox-1)/2,
##                sizeofbox**2 - 2* (sizeofbox-1) - (sizeofbox-1)/2,
##                sizeofbox**2 - 3* (sizeofbox-1) - (sizeofbox-1)/2]
##
##cornersofbox = (sorted(cornersofbox))
##middlesofbox = (sorted(middlesofbox))
###print(sizeofbox, cornersofbox, middlesofbox)
##
##if number in middlesofbox:
##    distance = (sizeofbox - 1)/2
##elif number in cornersofbox:
##    distance = (sizeofbox - 1)
##else: #Not in box
##    previousdistance = sizeofbox *2
##    for i in cornersofbox:
##        cornerdistance = abs(number-i)
##        #print(i, cornerdistance)
##        if cornerdistance < previousdistance:
##            previousdistance = cornerdistance
##            nearestcorner = i
##    distance = (sizeofbox - 1) - abs(nearestcorner - number)
##        
##print(distance)


######## Part 2 ##########

number = 368078

####Look up value based on coordinates

def getValue(coord):
    value2 = 0
    for i in range(len(ALLDATA)):
        if coord == ALLDATA[i][1]:
            value2 = ALLDATA[i][0]
            return value2
    return value2

ALLDATA =[[1, (0, 0),1, 1,'R'],[1, (1, 0),3, 1,'R']]
numbering =[1, (1, 0),3, 1,'R']
for i in range(1,10000):
    value = numbering[0]
    coordinates = numbering[1]
    sizeofbox = numbering[2]
    numberinbox = numbering[3]
    wall = numbering[4]
    maxcoordinate = (sizeofbox - 1)/2

    if wall == 'R':
        
        if coordinates[1] != maxcoordinate:
            coordinates = (coordinates[0], coordinates[1] +1)
            value += getValue((coordinates[0]-1,coordinates[1]))
            value += getValue((coordinates[0]-1,coordinates[1]+1))
            value += getValue((coordinates[0]-1,coordinates[1]-1))
        else:
            wall = 'U'
    if wall == 'U':
        if coordinates[0] != -1* maxcoordinate:
            coordinates = (coordinates[0] -1 , coordinates[1])
            value = value + getValue((coordinates[0],coordinates[1]-1))
            value = value + getValue((coordinates[0]+1,coordinates[1]-1))
            value = value + getValue((coordinates[0]-1,coordinates[1]-1))
        else:
            wall = 'L'
    if wall == 'L':
        if coordinates[1] != -1* maxcoordinate:
            coordinates = (coordinates[0], coordinates[1] -1)
            value = value + getValue((coordinates[0]+1,coordinates[1]+1))
            value = value + getValue((coordinates[0]+1,coordinates[1]))
            value = value + getValue((coordinates[0]+1,coordinates[1]-1))
        else:
            wall = 'D'
    if wall == 'D':
        if coordinates[0] != maxcoordinate:
            coordinates = (coordinates[0] +1, coordinates[1])
            value = value + getValue((coordinates[0]-1,coordinates[1]+1))
            value = value + getValue((coordinates[0],coordinates[1]+1))
            value = value + getValue((coordinates[0]+1,coordinates[1]+1))
        else:
            wall = 'R'
            coordinates = (coordinates[0] +1, coordinates[1])
            sizeofbox +=2
            numberinbox = 0
            #print(coordinates)
            value += getValue((coordinates[0]-1,coordinates[1]+1))

    print(value)
    if value > number:
        print(value, coordinates)
        break
    numbering =[value, coordinates, sizeofbox, numberinbox + 1,wall]
    #print(numbering)
    ALLDATA.append(numbering)

##for i in ALLDATA:
##    print(i)
##    if i[0]> number:
##        print(i)
##        break
