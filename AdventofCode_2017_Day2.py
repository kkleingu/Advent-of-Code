import numpy as np

#data = open(r'C:\Users\H129057\Documents\Personal\Python\RawData.txt' , 'r')
#myinput = data.read()#.strip('\n')

myfile = r'C:\Users\H129057\Documents\Personal\Python\RawData.csv'
myinput = np.genfromtxt(myfile, delimiter=",")

##### Part 1 #####
#checksum = 0
#for i in range(len(myinput)):
#    checksum+= max(myinput[i]) - min(myinput[i])
#
#print(checksum)

##### Part 2 #####
checksum = 0
for i in range(len(myinput)):
    for temp1 in range(len(myinput[i])):
        j = myinput[i][temp1]
        for temp2 in range(len(myinput[i])):
            k = myinput[i][temp2]
            if temp1 != temp2:
                if j%k == 0:
                    checksum += j/k
                    break

print(checksum)
