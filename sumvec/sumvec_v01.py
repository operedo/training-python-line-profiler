import math
import random


#@profile
def decrement(value,vec,i,lim,div):
	if(vec[i]>=lim):
		return value
	else:
		return value-vec[i]/div

#@profile
def increment(value,vec,i,lim,div):
	if(vec[i]<lim):
		return value+vec[i]/div
	else:
		return value
#@profile
def sumvec(vec,n,lim,div):
	value=0.0
	for i in range(0,n):
		if(i%2==0):
			value=increment(value,vec,i,lim,div)
		else:
			value=decrement(value,vec,i,lim,div)
	return value



n=2500000
vec=[0]*n
for i in range(0,n):
	vec[i]=i

ret=sumvec(vec,n,n/2,2)
print(ret)



