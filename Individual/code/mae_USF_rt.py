from math import sqrt
import re

with open("rtUSF1.txt") as f1:
    text1 = f1.read()

values = re.split(r'[\n\r]+', text1)
final = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r'\t',val)
	news = news[:-1]
	final.append(news)

with open("USF_predicted_rt_userp_mae.txt") as f2:
    text2 = f2.read()

values = re.split(r'[\n\r]+', text2)
predicted = [] #contains the entire ratings as a list of list
for val in values:
	news = re.split(r' ',val)
	news = news[:-1]
	predicted.append(news)
for i in range(len(final)):
	for j in range(len(final[i])):
		final[i][j] =float(final[i][j])
for i in range(len(predicted)):
	for j in range(len(predicted[i])):
		predicted[i][j] =float(predicted[i][j])
ssum=0.0
asum=0.0
print final[0][0],predicted[0][0]
for c in range(0,99):
	i=0
	for s in final[c]: 
		print c,i
		if(s != -1):
			asum=asum+abs(final[c][i])
			#print abs(final[c][i])
			#print  abs(final[c][i])- abs(predicted[c][i])
			ssum =ssum + abs(abs(final[c][i])- abs(predicted[c][i]))
		i=i+1
M=500*100
MAE= abs(ssum)/M
print "mae"
print MAE
#print ssum/asum
