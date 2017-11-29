from textblob import TextBlob
import re
with open("sentences.txt") as f14:
    text14= f14.read()
after4 = re.split(r'[\n\r]+', text14)
after4 =after4[:-1]
print after4[0]
it=-1
for text in after4:
	blob = TextBlob(text)

	mini=0.0
	maxi=0.0
	for sentence in blob.sentences:
		with open("sentiment2.txt","a") as f4:
			f4.write("%f\n" % (sentence.sentiment.polarity))
		#print sentence.sentiment.polarity

		#if(mini>sentence.sentiment.polarity):
			#mini=sentence.sentiment.polarity
		#if(maxi<sentence.sentiment.polarity):
			#maxi=sentence.sentiment.polarity
	it=it+1
	#print it
	#if(it <20000):
		#with open("sentiment.txt","a") as f4:
			#f4.write("%f\n" % (mini))
	#elif(it<30000):
		#with open("sentiment.txt","a") as f4:
			#f4.write("%f\n" % ((mini+maxi)/2.0))
	#else:
		#with open("sentiment.txt","a") as f4:
			#f4.write("%f\n" % (maxi))

	#print summation/count
#blob.translate(to="es")

