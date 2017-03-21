data1 = "Data_1.txt"
data2 = "Data_2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
return x
