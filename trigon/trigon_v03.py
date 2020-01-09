#	unsigned int i, r, j, n;
#	double d, x, y;
#
#	if (argc == 1) n = N; else n = atoi(argv[1]);
#
#	init_lookupTable();
#
#	srand(0);
#	for (i=0; i<n; i++)
#	{
#		r = rand();
#		for (j=0, d=0; j<POINTS; j++)
#		{
#			//x = r*cos(d); y = r*sin(d);
#			x = r*lookupTable[j][0];//cos(d); 
#			y = r*lookupTable[j][1];//sin(d);
#			fwrite(&x, sizeof(x), 1, stdout);
#			fwrite(&y, sizeof(y), 1, stdout);
#			//d += 2*M_PI/POINTS;
#		}
#	}
#
import random
import math

#@profile
def init_lookupTable(lookupTable):
	inc=2.0*math.pi/points
	d=0.0
	for j in range(0,points):
		lookupTable[j][0]=math.cos(d)
		lookupTable[j][1]=math.sin(d)
		d=d+inc
	

#@profile
def trigon(seed,N,points):
	random.seed(seed)
	inc=2.0*math.pi/points
	for i in range(1,N):
		r=random.random()
		d=0.0
		for j in range(0,points):
			#x=r*math.cos(d)
			#y=r*math.sin(d)
			x=r*lookupTable[j][0]
			y=r*lookupTable[j][1]
			if(i==100 and j==100):
				print(x,end="")
				print(y)
			#d=d+2.0*math.pi/points
			#d=d+inc


seed=0
N=1000
points=6000

lookupTable = [[None] * 2 for i in range(points)]

init_lookupTable(lookupTable)

trigon(seed,N,points)



