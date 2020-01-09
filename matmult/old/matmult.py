
@profile
def multmat(a,b):
	m=len(a)
	n=len(a[0])
	k=len(b)
	res=[]
	if len(b) != 1:
		p=len(b[0])-1
	else:
		p=0
	if len(b)==0:
		print('bad size')
	elif n!=k:
		print('bad size')
	else:
		#print('good size')
		n=k
		#print('k=',k,'n=',n)
		for it in range(1,10000):
			for q in range(m):
				res.append([0])
				#print('res=',res)
			for q in range(m):
				for w in range(p):
					res[q].append(0)
			for i in range(m):
				for j in range(p+1):
					for r in range(n):
						#print('ijr:res',i,j,r,res)
						res[i][j] =a[i][r]*b[r][j]+res[i][j]
	return res


#if __name__ ==  "__main__":

a = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
b = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

multmat(a,b)
