data = open(r'/Users/kevinkleinguetl/Documents/Python_Projects/dev/AdventofCode/RawData.txt' , 'r')
myinput = data.read()#.strip('\n')
myinput = myinput.split('\n')

myinput = [i.split(' ') for i in myinput]

dictionaryinputs = {}
