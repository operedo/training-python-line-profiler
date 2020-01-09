# Program to multiply two matrices
# using nested loops

@profile
def multmat(X,Y,result):
	#lenY=len(Y)
	#lenX=len(X)
	#lenY0=len(Y[0])
	#for i in range(lenX):
	#for j in range(lenY0):

	tmp=result[0][0] 
	#for k in range(lenY):
	tmp += X[0][0] * Y[0][0]
	tmp += X[0][1] * Y[1][0]
	tmp += X[0][2] * Y[2][0]
	result[0][0]=tmp

	tmp=result[0][1] 
	#for k in range(lenY):
	tmp += X[0][0] * Y[0][1]
	tmp += X[0][1] * Y[1][1]
	tmp += X[0][2] * Y[2][1]
	result[0][1]=tmp

	tmp=result[0][2] 
	#for k in range(lenY):
	tmp += X[0][0] * Y[0][2]
	tmp += X[0][1] * Y[1][2]
	tmp += X[0][2] * Y[2][2]
	result[0][2]=tmp

	tmp=result[0][3] 
	#for k in range(lenY):
	tmp += X[0][0] * Y[0][3]
	tmp += X[0][1] * Y[1][3]
	tmp += X[0][2] * Y[2][3]
	result[0][3]=tmp


	tmp=result[1][0] 
	#for k 1n range(lenY):
	tmp += X[1][0] * Y[0][0]
	tmp += X[1][1] * Y[1][0]
	tmp += X[1][2] * Y[2][0]
	result[1][0]=tmp

	tmp=result[1][1] 
	#for k 1n range(lenY):
	tmp += X[1][0] * Y[0][1]
	tmp += X[1][1] * Y[1][1]
	tmp += X[1][2] * Y[2][1]
	result[1][1]=tmp

	tmp=result[1][2] 
	#for k 1n range(lenY):
	tmp += X[1][0] * Y[0][2]
	tmp += X[1][1] * Y[1][2]
	tmp += X[1][2] * Y[2][2]
	result[1][2]=tmp

	tmp=result[1][3] 
	#for k 1n range(lenY):
	tmp += X[1][0] * Y[0][3]
	tmp += X[1][1] * Y[1][3]
	tmp += X[1][2] * Y[2][3]
	result[1][3]=tmp


	tmp=result[2][0] 
	#for k 2n range(lenY):
	tmp += X[2][0] * Y[0][0]
	tmp += X[2][1] * Y[1][0]
	tmp += X[2][2] * Y[2][0]
	result[2][0]=tmp

	tmp=result[2][1] 
	#for k 2n range(lenY):
	tmp += X[2][0] * Y[0][1]
	tmp += X[2][1] * Y[1][1]
	tmp += X[2][2] * Y[2][1]
	result[2][1]=tmp

	tmp=result[2][2] 
	#for k 2n range(lenY):
	tmp += X[2][0] * Y[0][2]
	tmp += X[2][1] * Y[1][2]
	tmp += X[2][2] * Y[2][2]
	result[2][2]=tmp

	tmp=result[2][3] 
	#for k 2n range(lenY):
	tmp += X[2][0] * Y[0][3]
	tmp += X[2][1] * Y[1][3]
	tmp += X[2][2] * Y[2][3]
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

