data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
<<<<<<< HEAD

x = readData(data1)
txt = []
for i in x:
	if i == 'I' : txt.append('*')
	elif i == 'and' or i=='The' or i=='you': txt.append('*'*3)
	# elif i == 'The' : txt.append('*'*3)
	# elif i == 'you' : txt.append('*'*3)
	else: txt.append(i)
txt = ' '.join(txt) 
print (txt)
=======
>>>>>>> 1a2b95e15fae8cc748d0f0e905f60a36e15a9760
