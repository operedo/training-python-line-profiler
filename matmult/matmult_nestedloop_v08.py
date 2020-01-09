# Program to multiply two matrices
# using nested loops

#@profile
def multmat(X,Y,result):

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

	result[0][0]= X00 * Y00 + X01 * Y10 + X02 * Y20 
	result[0][1]= X00 * Y01 + X01 * Y11 + X02 * Y21 
	result[0][2]= X00 * Y02 + X01 * Y12 + X02 * Y22 
	result[0][3]= X00 * Y03 + X01 * Y13 + X02 * Y23 

	result[1][0]= X10 * Y00 + X11 * Y10 + X12 * Y20 
	result[1][1]= X10 * Y01 + X11 * Y11 + X12 * Y21 
	result[1][2]= X10 * Y02 + X11 * Y12 + X12 * Y22 
	result[1][3]= X10 * Y03 + X11 * Y13 + X12 * Y23 

	result[2][0]= X20 * Y00 + X21 * Y10 + X22 * Y20 
	result[2][1]= X20 * Y01 + X21 * Y11 + X22 * Y21 
	result[2][2]= X20 * Y02 + X21 * Y12 + X22 * Y22 
	result[2][3]= X20 * Y03 + X21 * Y13 + X22 * Y23 


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

