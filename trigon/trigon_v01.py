
import random
import math

#@profile
def trigon(seed,N,points):
	random.seed(seed)
	for i in range(1,N):
		r=random.random()
		d=0.0
		for j in range(0,points):
			x=r*math.cos(d)
			y=r*math.sin(d)
			if(i==100 and j==100):
				print(x,end="")
				print(y)
			d=d+2.0*math.pi/points


seed=0
N=1000
points=6000

trigon(seed,N,points)



