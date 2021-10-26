def crossword(m,n,y,a):
	l, b , li3 ,li4,sum,num = [] , [], [] , [], 0, 0
	for i in range(m):
		l = []
		for j in range(n):
			if (i == 0 or j == 0 or a[i][j-1] == '*' or a[i-1][j] == '*') and a[i][j] != '*':
				sum += 1
				l.append(sum)
			else :
				l.append(0)
		b.append(l)
	print("#Puzzle :",y ,"\nAcross=======================================")
	for i in range(m):
		s = ''
		for j in range(n):
			if(a[i][j] != '*'):
				if len(s) == 0:
					num = b[i][j]
				s = s + a[i][j]
			if(j == n-1 or a[i][j] == '*'):
				s = s + '\0'
				if s[0] != '\0' :
					print(str(num)+'.'+s)
				s = ''	
	print("Down===================================================================")
	for i in range(n):
		s = ''
		for j in range(m):
			if(a[j][i] != '*'):
				if len(s) == 0:
					num = b[j][i]
				s = s + a[j][i]
			if(j == m-1 or a[j][i] == '*'):
				s = s + '\0'
				if s[0] != '\0' :
					li3.append(num)
					li4.append(s)
				s = ''	
	my_dict = dict(zip(li3,li4))
	for i in sorted(my_dict.keys()):
		print(str(i)+'.'+my_dict[i])	
a,li1,li2,li5,n3=[],[5],[],[],0
while(li1[0] != 0):
	li1=[]
	li1 = [int(r) for r in input().split() ]	
	if li1[0] != 0:
		a=[]
		for i in range(li1[0]):
			li = [x for x in input()]
			a.append(li)
		li2.append(li1)
		li5.append(a)
for p in li2:
	n3+=1
	crossword(p[0],p[1],n3,li5[n3-1])
