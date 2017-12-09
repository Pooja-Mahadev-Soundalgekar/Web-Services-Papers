from math import sqrt
 
def standard_deviation(lst, population=True):
    """Calculates the standard deviation for a list of numbers."""
    num_items = len(lst)
    mean = sum(lst) / num_items
    differences = [x - mean for x in lst]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
 
    # Note: it would be better to return a value and then print it outside
    # the function, but this is just a quick way to print out the values along
    # the way.
    if population is True:
        print('This is POPULATION standard deviation.')
        variance = ssd / num_items
    else:
        print('This is SAMPLE standard deviation.')
        variance = ssd / (num_items - 1)
    sd = sqrt(variance)
    # You could `return sd` here.
 
    print('The mean of {} is {}.'.format(lst, mean))
    print('The differences are {}.'.format(differences))
    print('The sum of squared differences is {}.'.format(ssd))
    print('The variance is {}.'.format(variance))
    print('The standard deviation is {}.'.format(sd))
    print('--------------------------')



#def savg(c):
    #savg=0.0
    #count=0.0
    #for i in qos[c]:
        #if(qos[c][i]>0):
            #count++
            #savg=savg+qos[c][i]
    #if(count >0):
        #savg=savg/count
    #return savg
#def cavg(s):
    #cavg=0.0
    #count=0.0
    #for i in qos:
        #if(qos[i][s]>0):
            #count++
            #cavg=cavg+qos[i][s]
    #if(count >0):
        #cavg=cavg/count
    #return cavg
#def utopsum(c):
    #topsum=0.0
    #for cj in N[c]:
        #topsum=topsum+qsimdash[c][cj]* ((qos[cj][s]-savg(cj))/standard_deviation(qos[cj]))
    #return topsum
#def ubottomsum(c):
    #bottomsum=0.0
    #for cj in N[c]:
        #bottomsum=bottomsum+qsimdash[c][cj]
    #return bottomsum
def std_s(s):
    #add to a list qos[i][s] and return list
#assume c to be the consumer and s to be the webservice we are concerned with qos[c][s]
#uqos[c][s]= savg(c) + standard_deviation(qos[c])*(utopsum(c)/ubottomsum(c))
#iqos[c][s]=cavg(s) + standard_deviation(std_s(s))*()
#
#
s = [98, 127, 133, 147, 170, 197, 201, 211, 255]
standard_deviation(s)
standard_deviation(s, population=False)