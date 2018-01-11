data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()
myinput = myinput.split('\n')


myinput  = ['aaaaa-bbb-z-y-x-123[abxyz]','a-b-c-d-e-f-g-h-987[abcde]','not-a-real-room-404[oarel]','totally-real-room-200[decoy]']

#temp = myinput[0].split('[')
#temp = myinput.split('[')




##
##summation = 0
##for i in range(len(myinput)-1):
##    temp = myinput[i].split('[')
##    #print(temp)
##    checksum = temp[1][0:-1]
##    name = temp[0]
##
##    x =''
##    for s in temp[0]:
##        if s.isdigit():
##            x += s
##
##    sectorID = int(x)
##
##    alphabet = 'abcdefghijklmnopqrstuvwxyz'
##    d = {}
##    for letter in alphabet:
##        amount = name.count(letter)
##        d[letter] = amount
##
##    least = 100
##    lol = alphabet
##    for letter in checksum:
##        #print(letter)
##        if d[letter] <= least:
##            least = d[letter]
##            d[letter] = 0
##            #print(least)
##        lol = lol.replace(str(letter), '')
##        #print(lol)
##
##    if max(d.values()) <= least:
##        summation += sectorID
##
##
##print(summation)

#myinput =['qzmt-zixmtkozy-ivhz-343[abcd]']

alphabet = 'abcdefghijklmnopqrstuvwxyz'
codee = []
for j in alphabet:
    codee.append(j)

##code = {'a': 'b', 'b': 'c','c': 'd', 'd': 'e', 'e': 'f','f': 'g', 'g': 'h', 'h': 'i', 'i': 'j',
##        'j':'k' ,'k': 'l', 'l': 'm', 'm': 'n', 'n':'o', 'o': 'p',
##        'p': 'q', 'q':'r', 'r': 's', 's':'t', 't':'u', 'u':'v', 'v': 'w',
##        'w': 'x', 'x':'y', 'y':'z', 'z':'a', '-':' ' }

newnames = []
##summation = 0
for i in range(len(myinput)-1):
    temp = myinput[i].split('[')

    #temp = myinput.split('[')
    checksum = temp[1][0:-1]
    name = temp[0]

    x =''
    for s in temp[0]:
        if s.isdigit():
            x += s

    sectorID = int(x)
    movement = sectorID %26

    #alphabet = 'abcdefghijklmnopqrstuvwxyz'

    newname=''

    for letter in name:
        #print(letter)
        if letter == '-':
            newname = newname + ' '
        if letter in alphabet:
            #print(letter)
            ok = alphabet.index(letter)+movement
            if ok >=26:
                ok = ok - 26
            newname = newname + codee[ok]
            #print(newname)
    if 'north pole' in newname:
        print(newname)
        print(sectorID)
    print(newname)
    print(sectorID)
    newnames.append(newname)
#print(newnames)



##newnames = []
##summation = 0
##for i in range(len(myinput)-1):
##    temp = myinput[i].split('[')
##    #print(temp)
##    checksum = temp[1][0:-1]
##    name = temp[0]
##
##    x =''
##    for s in temp[0]:
##        if s.isdigit():
##            x += s
##
##    sectorID = int(x)
##
##    alphabet = 'abcdefghijklmnopqrstuvwxyz-'
##    newname=''
##    for letter in name:
##        print(letter)
##        if letter in alphabet:
##            newname = newname + code[letter]
##    newnames.append(newname)
##    print(newnames)
##print(newnames)
##
##    least = 100
##    lol = alphabet
##    for letter in checksum:
##        #print(letter)
##        if d[letter] <= least:
##            least = d[letter]
##            d[letter] = 0
##            #print(least)
##        lol = lol.replace(str(letter), '')
##        #print(lol)
##
##    if max(d.values()) <= least:
##        summation += sectorID
##
##
##print(summation)
x = 7
t = 5
print(x)
