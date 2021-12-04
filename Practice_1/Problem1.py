S1=[1,2,3]
S2=[2,3,3]
S3=[]
S4=[]
checked=[0,0,0]
for i in range(len(S1)):
	p=0
	for j in range(len(S2)):
		if (S1[i]==S2[j]) and (checked[j]==0):
			checked[j]=1
			p=1
			break
	if(p==0):
		S3.append(S1[i])
#print(S3)
checked2=[0,0,0]
for i in range(len(S2)):
	p=0
	#print(checked2)
	for j in range(len(S1)):
		if S2[i]==S1[j] and checked2[j]==0:
			checked2[j]=1
			p=1
			break
	if(p==0):
		S4.append(S2[i])
		
#print(S4)

S=S3+S4
print(S)