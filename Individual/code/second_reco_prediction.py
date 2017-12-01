import re
with open("consumerprovidermatrixfull.csv") as f1:
    text1 = f1.read()
values = re.split(r'[\n\r]+', text1)
conpro = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r'\t',val)
	news = news[:-1]
	conpro.append(news)
with open("IFusers-sim.txt") as f2:
    text2 = f2.read()
values2 = re.split(r'[\n\r]+', text2)
usersim = [] #contains the entire ratings as a list of list
for val in values2:
	news = re.split(r' ',val)
	usersim.append(news)
with open("IFkusers.csv") as f3:
    text3 = f3.read()
values = re.split(r'[\n\r]+', text3)
N1 = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r',',val)
	news = news[:-1]
	N1.append(news)
for i in range(len(conpro)):
	for j in range(len(conpro[i])):
		conpro[i][j] =int(conpro[i][j])
for i in range(len(usersim)):
	for j in range(len(usersim[i])):
		usersim[i][j] =usersim[i][j]
for i in range(len(N1)):
	for j in range(len(N1[i])):
		N1[i][j] =int(N1[i][j])
tempcp=conpro
print len(conpro)
print conpro[321][909]
for c in range(len(conpro)-1):
	for it in range(1023):
		if(conpro[c][it] > 0):
			for index in N1[c]:
				#print it
				#print int(index)
				#print float(usersim[c*339+int(index)-1][2]), conpro[int(index)-1][i]
				if(float(conpro[int(index)-1][i])>20):
					print c,it
					tempcp[c][it]= tempcp[c][it]+ float(usersim[c*339+int(index)-1][2])*20
				else:
					print c
					tempcp[c][it]= tempcp[c][it]+ float(usersim[c*339+int(index)-1][2])*float(conpro[int(index)-1][it])
			tempcp[c][it]=tempcp[c][it]/18.0
			if(tempcp[c][it]> 300):
				tempcp[c][it]=18
for c in range(len(conpro)-1):
	for i in range(1023):
		with open("second_reco_prediction_test.txt","a") as f5:
			f5.write("%f " % (tempcp[c][i]))
	with open("second_reco_prediction_test.txt","a") as f5:
		f5.write("\n")