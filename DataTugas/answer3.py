data1 = "DataSet.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
#step 1 :
y = readData(data1)
z = []
reversed_number = []
for i in y:
    if (i.isdigit() == True) :
        z.append(i)
# end of step 1 : to show the numbers, you can uncomment syntax below
#print (z)

#step 2:
for i in y :
    if (i.isdigit() == True) :
         reversed_number.append(z.pop())
    else : reversed_number.append(i)

# end of step 2 : to show the reversed_number, you can uncomment syntax below
#print (reversed_number)

#step 3 :
answer3 = []
i = reversed_number[0]
i = ' '.join(word[0].upper() + word[1:] for word in i.split())
answer3.append(i)

for count in range(1,len(reversed_number)):
    i = reversed_number[count]
    iprev = reversed_number[count-1]
    if (iprev[len(iprev)-1] == '.') :
        i = ' '.join(word[0].upper() + word[1:] for word in i.split())
    answer3.append(i)

answer3 = ' '.join(answer3)
print (answer3)
