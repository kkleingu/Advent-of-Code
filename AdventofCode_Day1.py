location = [0,0, 0]

#print('please')
theinput = 'L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2'

#theinput = 'R8, R4, R4, R8'
path = theinput.split(' ,')
#print(path)
#pathx = path[0]
path = path[0].split(', ')
#print(path[0])

def moving(Movement, Location):
    newlocation = Location.copy()
    #print(newlocation)
    #print(Movement[0])
    #print(Movement[1])
    if Movement[0] == 'L':
        #print(newlocation[2])
        newlocation[2] = newlocation[2] - 90
        if newlocation[2] < 0:
            newlocation[2] = 270
    if Movement[0] == 'R':
        newlocation[2] = newlocation[2] + 90
        if newlocation[2] == 360:
            newlocation[2] = 0
    #else:
        #print('Location Error')
    if newlocation[2] == 0:
        newlocation[1] += int(Movement[1:])
    if newlocation[2] == 90:
        newlocation[0] += int(Movement[1:])
    if newlocation[2] == 180:
        newlocation[1] -= int(Movement[1:])
    if newlocation[2] == 270:
        newlocation[0] -= int(Movement[1:])
    #else:
        #print('Movement Error')
    return newlocation

location = [0,0,0]
previous_locations= [[location[0],location[1]]]
#print(previous_locations)
for i in path:
    #print(i)
    #print(location)
    currentlocation = moving(i,location)
    #print(currentlocation)

    if currentlocation[0] == location[0]: #I moved north and south
        #print('y')
        change = currentlocation[1] - location[1]+1
        #print(change)
        for j in range(1,change):
            #print(j)
            temp = [location[0],location[1]+j]
            #print(temp)
            if temp in previous_locations:
                print(temp)
                print(abs(temp[0])+abs(temp[1]))
                print('home')
                break
            else:
                previous_locations.append(temp)
                #print('yes')
        location = currentlocation
    if currentlocation[1] == location[1]: #I moved East and West
        #print('x')
        change = currentlocation[0] - location[0]+1
        #print(change)
        for j in range(1,change):
            #print(j)
            temp = [location[0]+j,location[1]]
            if temp in previous_locations:
                print(temp)
                print(abs(temp[0])+abs(temp[1]))
                print('home')
                break
            else:
                previous_locations.append(temp)
        location = currentlocation
     #location = newlocation
     
##    for j in range
##    if [location[0],location[1]] in previous_locations:
##        #print(location)
##        #print('home')
##        break
##    else:
##        previous_locations.append([location[0],location[1]])
    
print(location)
#print(location[0]+location[1])
#print(previous_locations)
