data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
<<<<<<< HEAD
	return x

x = readData(data1)
y = readData(data2)
txt = []

for i in x:
	for j in y:
		if (i==j):
			if (i not in txt):
				txt.append(i)
			
txt = ' '.join(txt)

print (txt)
=======
return x
>>>>>>> 1a2b95e15fae8cc748d0f0e905f60a36e15a9760
