from collections import Counter

data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()#.strip('\n')
#myinput = myinput.split('\n')

#myinput = '{}' #1
#myinput =  '{{{}}}' #6
#myinput =  '{{},{}}' #5.
#myinput =  '{{{},{},{{}}}}' #16.
#myinput = '{<a>,<a>,<a>,<a>}'# score of 1.
#myinput = '{{<ab>},{<ab>},{<ab>},{<ab>}}' #score of 1 + 2 + 2 + 2 + 2 = 9.
#myinput =  '{{<!!>},{<!!>},{<!!>},{<!!>}}' #score of 1 + 2 + 2 + 2 + 2 = 9.
#myinput =  '{{<a!>},{<a!>},{<a!>},{<ab>}}' #score of 1 + 2 = 3.

#####Part 1 ######
##score = 0
##group = 0
##garbage = False
##valid = True
###myinput = ' ' + myinput #adds a default space to help with initial counting
##for i in range(len(myinput)):
##    character = myinput[i]
##    #print(character)
##    #previous = myinput[i-1]
##    if character == '{' and not garbage and valid:
##        group += 1
##    elif character == '}' and not garbage and valid:
##        score += group
##        group -= 1
##    elif character == '<' and valid:
##        garbage = True
##    elif character == '>' and valid:
##        garbage = False    
##    elif character == '!' and valid: #previous != '!':
##        valid = False
##    elif not valid:
##        valid = True
##    #print(character, valid)
##print(score)

#####Part 2 ######

##myinput = '<>'#, 0 characters.
##myinput = '<random characters>'#, 17 characters.
##myinput = '<<<<>'#, 3 characters.
##myinput = '<{!>}>'#, 2 characters.
##myinput = '<!!>'#, 0 characters.
##myinput = '<!!!>>'#, 0 characters.
##myinput = '<{o"i!a,<{i<a>'#, 10 characters.

score = 0
group = 0
garbage = False
garbagecounter = 0
valid = True
for i in range(len(myinput)):
    character = myinput[i]
    #print(character)
    #previous = myinput[i-1]
    if character == '{' and not garbage and valid:
        group += 1
    elif character == '}' and not garbage and valid:
        score += group
        group -= 1
    elif character == '<' and valid and not garbage:
        garbage = True
    elif character == '>' and valid:
        garbage = False    
    elif character == '!' and valid: #previous != '!':
        valid = False
    elif garbage and valid:
        garbagecounter += 1
    elif not valid:
        valid = True
    #print(character, valid)
print(garbagecounter)
