from numpy import linalg as LA
import numpy as NP

X = NP.matrix("12 7 3; 4 5 6; 7 8 9")
Y = NP.matrix("5 8 1 2; 6 7 3 0; 4 5 9 1")
for it in range(1,100000):
	result=X * Y

print(result)
# same as NP.dot(a1, a2t) 
#matrix([[127,  84,  85,  89],
#        [218, 139, 142, 173],
#        [226, 157, 136, 103],
#        [352, 197, 214, 393]])
