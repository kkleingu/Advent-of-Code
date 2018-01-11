data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()
myinput = myinput.split('\n')

import operator

def find_most(word):
    dictionary = {}
    #print(word)
    for letter in word:
        #print(letter)
        if letter in dictionary:
            #print('yes')
            dictionary[letter] += 1
        else:
            #print('no')
            dictionary[letter] = 1
    #print(dictionary)
    dictionary = sorted(dictionary.items(),key=operator.itemgetter(1))
    #return dictionary[len(dictionary)-1]
    return dictionary[0]
    


column1 =''
column2 =''
column3 =''
column4 =''
column5 =''
column6 =''
column7 =''
column8 =''

for rows in myinput:
    column1 += rows[0]
    column2 += rows[1]
    column3 += rows[2]
    column4 += rows[3]
    column5 += rows[4]
    column6 += rows[5]
    column7 += rows[6]
    column8 += rows[7]


print(find_most(column1))
print(find_most(column2))
print(find_most(column3))
print(find_most(column4))
print(find_most(column5))
print(find_most(column6))
print(find_most(column7))
print(find_most(column8))
