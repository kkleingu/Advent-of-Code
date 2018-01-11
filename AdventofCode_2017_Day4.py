from collections import Counter
data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()
myinput = myinput.split('\n')

##### Part 1 #######
##totalvalid = 0
##for passphrase in myinput:
##    if passphrase != '':
##        passphrase = passphrase.split(' ')
##        x = sorted(Counter(passphrase).values())
##        if x[-1] == 1:
##            totalvalid +=1
##
##print(totalvalid)    

##myinput =['abcde fghij', 'abcde xyz ecdab', 'a ab abc abd abf abj',
##          'iiii oiii ooii oooi oooo', 'oiii ioii iioi iiio'] 
##

##### Part 2 #######
totalvalid = 0
for passphrase in myinput:
    if passphrase != '':
        passphrase = passphrase.split(' ')
        newpassphrase = []
        for i in range(len(passphrase)):
            #print(passphrase[i])
            newpassphrase.append(''.join(sorted(passphrase[i])))
            #temp = ''.join(sorted(passphrase[i]))
            #newpassphrase[i] = temp.join
            #print(newpassphrase[i])
        #print(newpassphrase)
        x = sorted(Counter(newpassphrase).values())
        if x[-1] == 1:
            totalvalid +=1

print(totalvalid)    















