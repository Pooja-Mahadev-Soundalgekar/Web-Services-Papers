import re
import random
with open("dataset_reviews.txt") as f1:
    text1 = f1.read()
with open("4.csv") as f2:
    text2= f2.read()
with open("5.csv") as f3:
    text3= f3.read()
with open("6.csv") as f4:
    text4= f4.read()
with open("dataset_reviews_qos.txt") as f5:
    text5= f5.read()
with open("dataset_reviews_negation.txt") as f6:
    text6= f6.read()
with open("Badwords.csv") as f7:
    text7= f7.read()
adj4 = re.split(r'[\n\r]+', text2)
sentences = re.split(r'[\n\r]+', text1)
adj5 = re.split(r'[\n\r]+', text3)
qos = re.split(r'[\n\r]+', text4)
qossentences = re.split(r'[\n\r]+', text5)
negsentences = re.split(r'[\n\r]+', text6)
neg = re.split(r'[\n\r]+', text7)
adj4 =adj4[:-1]
adj5 =adj5[:-1]
sentences =sentences[:-1]
qossentences =qossentences[:-1]
qos =qos[:-1]
neg =neg[:-1]
negsentences =negsentences[:-1]
a=1
def add1 (adj4,sentences,filename):
	for sentence in sentences:
		for a41 in adj4:
			sentence_array = sentence
			pos= sentence_array.find('_')
			sentence_array= sentence_array.replace(sentence_array[pos],a41,1)
			pos= sentence_array.find('_')
			for a42 in adj4:
				if(a42 == a41):
					a42=a41
				else:
					sent= sentence_array
					sent= sent.replace(sent[pos],a42)
					with open(filename,"a") as f4:
						f4.write("%s\n" % (sent))
def add2 (adj4,sentences,filename):
	for sentence in sentences:
		for a41 in adj4:
			sentence_array = sentence
			pos= sentence_array.find('_')
			sentence_array= sentence_array.replace(sentence_array[pos],a41,1)
			with open(filename,"a") as f4:
				f4.write("%s\n" % (sentence_array))
#add1(adj4,sentences,"dataset_reviews4.txt")
#add1(adj5,sentences,"dataset_reviews5.txt")
#add1(qos,qossentences,"dataset_reviewsqos.txt")
#add2(neg,negsentences,"dataset_reviewsnegation.txt")

def random1 (sentences1,sentences2,sentences3,filename,i1,i2,j1,j2,k1,k2):	
	for i in range(10000):
		x1=random.randint(1,i2)
		x2=random.randint(1,k2)
		while x1==x2:
			x2=random.randint(1,k2)
		x3=random.randint(1,j2)

		y1=random.randint(1,i1)
		y2=random.randint(1,k1)
		while y1==y2:
			y2=random.randint(1,k1)
		y3=random.randint(1,j1)
		x=random.randint(1,13)
		#print x1,x2,x3,y1,y2,y3
		z1=sentences1[(x1-1)*i1+y1-2]
		#z2=sentences3[(x2-1)*k1+y2-2]
		z3=sentences2[(x3-1)*j1+y3-2]
		z2=sentences[x]
		x=random.randint(1,3)
		with open(filename,"a") as f4:
			if(x == 1):
				f4.write("%s %s %s\n" % (z1,z2,z3))
			if(x == 2):
				f4.write("%s %s %s\n" % (z3,z2,z1))
			if(x == 3):
				f4.write("%s %s %s\n" % (z1,z3,z2))
		
		
with open("okdataset_reviewsqos.txt") as f8:
    text8= f8.read()
with open("dataset_reviews3.txt") as f9:
    text9= f9.read()
with open("dataset_reviews1.txt") as f10:
    text10= f10.read()
review5 = re.split(r'[\n\r]+', text10)
review5 =review5[:-1]
reviewqos = re.split(r'[\n\r]+', text8)
review4 = re.split(r'[\n\r]+', text9)
review4 =review4[:-1]
reviewqos =reviewqos[:-1]
print len(reviewqos), len(review4)
#random1(review4,reviewqos,review4,"review3.txt",182,22,342,6,182,22)
#random1(review5,reviewqos,review5,"review1.txt",21,13,342,8,21,13)
with open("review3.txt") as f11:
    text11= f11.read()
with open("review1.txt") as f12:
    text12= f12.read()
reviewf5 = re.split(r'[\n\r]+', text12)
reviewf5 =reviewf5[:-1]
reviewf4 = re.split(r'[\n\r]+', text11)
reviewf4 =reviewf4[:-1]
def random2 (sentence,filename):
	for it in range(10000):
		x=random.randint(1,5)
		with open(filename,"a") as f4:
			f4.write("%s\n" % (sentence[(it-1)*5 + x -1]))
#random2(reviewf4,"beforenegation3.txt")
#random2(reviewf5,"beforenegation1.txt")
with open("wordnet.txt") as f13:
    text13= f13.read()
reviewnegation = re.split(r'[\n\r]+', text13)
reviewnegation =reviewnegation[:-1]
print len(reviewnegation)
#random1(review5,reviewqos,reviewnegation,"negation1.txt",21,13,342,8,17,5)
#random1(review4,reviewqos,reviewnegation,"wordnet3.txt",182,22,342,6,17,5)
def random3(filename,sentence1,sentence2):
	for it in range(500):
		y1=random.randint(1,20)
		y2=random.randint(1,20)
		for i in range(20):
			if(i == y2):
				with open(filename,"a") as f4:
					f4.write("%s\n" % (sentence2[(it-1)*20+y1-1]))
			else:
				with open(filename,"a") as f4:
					f4.write("%s\n" % (sentence1[(it-1)*20+i-1]))
with open("negation2.txt") as f13:
    text13= f13.read()
with open("beforenegation2.txt") as f14:
    text14= f14.read()
negationsentence = re.split(r'[\n\r]+', text13)
after4 = re.split(r'[\n\r]+', text14)
after4 =after4[:-1]
print len(after4),len(negationsentence)
random3("afternegation2.txt",after4,negationsentence)		
