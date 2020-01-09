import math
import random


@profile
def decrement(value,vec,i,lim,div):
	if(vec[i]>=lim):
		return value
	else:
		return value-vec[i]/div

@profile
def increment(value,vec,i,lim,div):
	if(vec[i]<lim):
		return value+vec[i]/div
	else:
		return value
@profile
def sumvec(vec,n,lim,div):
	value=0.0
	i=0
	for i in range(0,n-1,2):
		if(vec[i]<lim):
			value = value+vec[i]/div
		if(vec[i+1]<lim):
			value = value-vec[i+1]/div

	#for i in range(0,n):
	#	if(vec[i]<lim):
	#		if(i%2==0):
	#			value = value+vec[i]/div

	#		else:
	#			value = value-vec[i]/div


	return value



n=2500000
vec=[0]*n
for i in range(0,n):
	vec[i]=i

ret=sumvec(vec,n,n/2,2)
print(ret)



