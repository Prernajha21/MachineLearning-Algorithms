import sys
import random
import math

#########################################################
# Read files from the command line
#########################################################
datafile = sys.argv[1]
f = open(datafile, 'r')
data = []
l = f.readline()

#Read Data
while(l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
		#data.append(l2)
	l2.append(float(1))
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])
print("rows", rows, "cols", cols)
f.close()
#########################################################
#Read Training Labels
#########################################################   
trainlabelfile = sys.argv[2]

f = open(trainlabelfile, 'r')
trainlabels = {}
n = [0, 0]
l = f.readline()

while(l != ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	#if(trainlabels[int(a[1])] == 0):
	#	trainlabels[int(a[1])] = -1
	l = f.readline()

	n[int(a[0])] += 1
 
f.close()
#print(data)
#print(trainlabels)

###########################################################
# Dot product function definition 
###########################################################
def dot(vector1,vector2):
	dp = 0
	#return sum(x*y for x,y in zip(v1,v2))
	#return sum([v1[i][0]*v2[i] for i in range(len(v2))])
	for j in range(0,cols,1):
		dp += vector1[j] * vector2[j]
	return dp

###########################################################
#Initialize W
###########################################################
w = []
for j in range(0,cols,1):
	w.append(0.02 * random.random() - 0.01) 

###########################################################
# Gradient descent iteration
###########################################################
eta = 0.01
diff = 1
error = 100000000 
dellf = []
stop_condition = 0.0000001

while(diff > stop_condition):
	dellf = [0] * cols
	#for j in range(0,cols,1):
		#prev_dellf[j] = dellf[j]
		#dellf.append(0)
		#dellf[j]*cols 
	for i in range(0, rows,1):
		if(trainlabels.get(i) != None):
			dp = dot(w,data[i])
			expo = (trainlabels.get(i))-(1/(1+(math.exp(-1*dp))))
			#distance_function = (trainlabels.get(i))*(dot(w,data[i]))
			for j in range(0,cols,1):
				#if(distance_function < 1):
					#dellf[j] += -1 * ((trainlabels.get(i))*data[i][j])
					dellf[j] += expo * data[i][j]
				#else:
				#	dellf[j] += 0


##############################################################
#Update w
##############################################################
	for j in range(0,cols,1):
		w[j] += eta*dellf[j]

	prev_error = error
	error = 0
	
##############################################################
#Compute hingeloss 
##############################################################
	for i in range(0,rows,1):
		if(trainlabels.get(i) != None):
			#error += max(0,1-(trainlabels.get(i)* dot(w,data[i])))
			dp = dot(w,data[i])
			error += math.log(1 + math.exp((-1 * (trainlabels.get(i))) * dp)) 

##############################################################
# Calculate  convergence
##############################################################
		diff = abs(prev_error - error)
	print()
	print("loss = ", error)

normw = 0
for j in range(0,(cols-1),1):
	normw += w[j] ** 2
print("====================================================")
print()
print("w = ",w[0],",",w[1])
print()
normw = math.sqrt(normw)
print("||w||=",normw)
d_origin = abs(w[len(w)-1]/normw)
print("====================================================")
print()
print("Distance to origin = ", d_origin)

print("====================================================")
print()
print("Predictions:")
##############################################################
#Prediction
##############################################################
for i in range(0, rows,1):
	if(trainlabels.get(i) == None):
    		dp = dot(w,data[i])
    		if(dp > 0):
    			print("1",i)
    		else:
    			print("0",i)







