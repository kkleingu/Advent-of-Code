from collections import Counter

data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()#.strip('\n')
myinput = myinput.split('\n')

#myinput = ['pbga (66)','padx (45) -> pbga, havc, qoyq']

registers = {}
conditions = []
for i in myinput:
    temp = i.split(' ')
    registers[temp[0]] = 0
    if temp[1] == 'inc':
        addition = int(temp[2])
    elif temp[1] == 'dec':
        addition = int(temp[2]) * -1
    else:
        print('Not inc or dec')
    conditional = [temp[4],temp[5],int(temp[6])]
    conditions.append([temp[0],addition,conditional])
    
#####Part 1 ######

##for i in conditions:
##    conditional = i[2]
##    if conditional[1] == '>':
##        if registers[conditional[0]] > conditional[2]:
##            registers[i[0]] += i[1]
##    elif conditional[1] == '<':
##        if registers[conditional[0]] < conditional[2]:
##            registers[i[0]] += i[1]
##    elif conditional[1] == '<=':
##        if registers[conditional[0]] <= conditional[2]:
##            registers[i[0]] += i[1]
##    elif conditional[1] == '>=':
##        if registers[conditional[0]] >= conditional[2]:
##            registers[i[0]] += i[1]
##    elif conditional[1] == '==':
##        if registers[conditional[0]] == conditional[2]:
##            registers[i[0]] += i[1]
##    elif conditional[1] == '!=':
##        if registers[conditional[0]] != conditional[2]:
##            registers[i[0]] += i[1]
##    else:
##        print(i[2][1], ' operation not found')
##
##print(max(registers.values()))

#####Part 2 ######
maxvalue = 0
for i in conditions:
    conditional = i[2]
    if conditional[1] == '>':
        if registers[conditional[0]] > conditional[2]:
            registers[i[0]] += i[1]
    elif conditional[1] == '<':
        if registers[conditional[0]] < conditional[2]:
            registers[i[0]] += i[1]
    elif conditional[1] == '<=':
        if registers[conditional[0]] <= conditional[2]:
            registers[i[0]] += i[1]
    elif conditional[1] == '>=':
        if registers[conditional[0]] >= conditional[2]:
            registers[i[0]] += i[1]
    elif conditional[1] == '==':
        if registers[conditional[0]] == conditional[2]:
            registers[i[0]] += i[1]
    elif conditional[1] == '!=':
        if registers[conditional[0]] != conditional[2]:
            registers[i[0]] += i[1]
    else:
        print(i[2][1], ' operation not found')
    if registers[i[0]] > maxvalue:
        maxvalue = registers[i[0]]
        
print(maxvalue)
