# Program to multiply two matrices
# using nested loops

@profile
def multmat(X,Y,result):
	#lenY=len(Y)
	#lenX=len(X)
	#lenY0=len(Y[0])
	#for i in range(lenX):
	#for j in range(lenY0):


	X00=X[0][0];
	X01=X[0][1];
	X02=X[0][2];
	X10=X[1][0];
	X11=X[1][1];
	X12=X[1][2];
	X20=X[2][0];
	X21=X[2][1];
	X22=X[2][2];

	Y00=Y[0][0];
	Y01=Y[0][1];
	Y02=Y[0][2];
	Y03=Y[0][3];
	Y10=Y[1][0];
	Y11=Y[1][1];
	Y12=Y[1][2];
	Y13=Y[1][3];
	Y20=Y[2][0];
	Y21=Y[2][1];
	Y22=Y[2][2];
	Y23=Y[2][3];

	tmp=result[0][0] 
	#for k in range(lenY):
	tmp += X00 * Y00
	tmp += X01 * Y10
	tmp += X02 * Y20
	result[0][0]=tmp

	tmp=result[0][1] 
	#for k in range(lenY):
	tmp += X00 * Y01
	tmp += X01 * Y11
	tmp += X02 * Y21
	result[0][1]=tmp

	tmp=result[0][2] 
	#for k in range(lenY):
	tmp += X00 * Y02
	tmp += X01 * Y12
	tmp += X02 * Y22
	result[0][2]=tmp

	tmp=result[0][3] 
	#for k in range(lenY):
	tmp += X00 * Y03
	tmp += X01 * Y13
	tmp += X02 * Y23
	result[0][3]=tmp


	tmp=result[1][0] 
	#for k 1n range(lenY):
	tmp += X10 * Y00
	tmp += X11 * Y10
	tmp += X12 * Y20
	result[1][0]=tmp

	tmp=result[1][1] 
	#for k 1n range(lenY):
	tmp += X10 * Y01
	tmp += X11 * Y11
	tmp += X12 * Y21
	result[1][1]=tmp

	tmp=result[1][2] 
	#for k 1n range(lenY):
	tmp += X10 * Y02
	tmp += X11 * Y12
	tmp += X12 * Y22
	result[1][2]=tmp

	tmp=result[1][3] 
	#for k 1n range(lenY):
	tmp += X10 * Y03
	tmp += X11 * Y13
	tmp += X12 * Y23
	result[1][3]=tmp


	tmp=result[2][0] 
	#for k 2n range(lenY):
	tmp += X20 * Y00
	tmp += X21 * Y10
	tmp += X22 * Y20
	result[2][0]=tmp

	tmp=result[2][1] 
	#for k 2n range(lenY):
	tmp += X20 * Y01
	tmp += X21 * Y11
	tmp += X22 * Y21
	result[2][1]=tmp

	tmp=result[2][2] 
	#for k 2n range(lenY):
	tmp += X20 * Y02
	tmp += X21 * Y12
	tmp += X22 * Y22
	result[2][2]=tmp

	tmp=result[2][3] 
	#for k 2n range(lenY):
	tmp += X20 * Y03
	tmp += X21 * Y13
	tmp += X22 * Y23
	result[2][3]=tmp







# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

for it in range(1,100000):
	# result is 3x4
	result = [[0,0,0,0],
	         [0,0,0,0],
	         [0,0,0,0]]

	multmat(X,Y,result)


for r in result:
	print(r)

