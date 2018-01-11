data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
myinput = data.read()
myinput = myinput.split('\n')


myinput = 'abba[mnop]qrst'
print(myinput)

partiallydividedstring = myinput.split('[')
goodstring = []
badstring = []
for i in partiallydividedstring:
    if ']' in i:
        temp = i.split(']')
        goodstring.append(temp[1])
        badstring.append(temp[0])
    else:
       goodstring.append(i)

print(goodstring)
print(badstring)           

def supportsTLS(gstring, bstring):
   if gstring == True and bstring == False:
       return 1
    else:
    return 0

    
