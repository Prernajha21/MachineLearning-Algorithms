import sys

# Read files from the command line
datafile = sys.argv[1]
f = open(datafile, 'r')
data = []
i = 0
l = f.readline()

#Read Data
while(l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
print("rows:",rows," ","columns:",cols)

#Read Training Labels   
trainlabelfile = sys.argv[2]

f = open(trainlabelfile, 'r')
trainlabels = {}
n = [0,0]
l = f.readline()
while(l != ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	l = f.readline()
	n[int(a[0])] += 1

#print(data)
#print(trainlabels) 
print("================================================")

#Determine mean of each class
m0=[]
m1=[]
for j in range(0, cols, 1):
	m0.append(1)
	m1.append(1)

for i in range(0, rows,1):
	if(trainlabels.get(i) != None and trainlabels[i] == 0):
		#n0 += 1
		for j in range(0, cols, 1):
			m0[j] += data[i][j]
	if(trainlabels.get(i) != None and trainlabels[i] == 1):
		#n1 += 1
		for j in range(0, cols, 1):
			m1[j] += data[i][j]
for j in range(0, cols, 1):
	m0[j] /= n[0]
	m1[j] /= n[1]

#print(m0)
#print(m1)

#Calculation of Standard Deviation
sd0 = []
sd1 = []
for j in range(0, cols, 1):
	sd0.append(0)
	sd1.append(0)
for i in range(0,rows,1):
	if(trainlabels.get(i) != None and trainlabels[i] == 0):
		for j in range(0, cols, 1):
			sd0[j] += (data[i][j]-m0[j])**2
	if(trainlabels.get(i) != None and trainlabels[i] == 1):
		for j in range(0, cols, 1):
			sd1[j] += (data[i][j]-m1[j])**2
for j in range(0, cols, 1):
	sd0[j] = (sd0[j]/n[0]) ** 0.5
	sd1[j] = (sd1[j]/n[1]) ** 0.5	 

#Classification of unlabeled point
for i in range(0, rows,1):
    if(trainlabels.get(i) == None):
    	d0 = 0
    	for j in range(0, cols, 1):
    		d0 += ((data[i][j] - m0[j])/sd0[j])**2
    	d1 = 0 
    	for j in range(0, cols, 1):
    		d1 += ((data[i][j] - m1[j])/sd1[j])**2
    	if(d0<d1):
    		print("0 ",i)
    	else:
    		print("1 ",i)
