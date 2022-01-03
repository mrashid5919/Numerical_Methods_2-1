import numpy as np
from math import fabs

a_in=[]
b_in=[]

def take_input():
    n=input()
    n=int(n)

    for i in range(n):
        line=input()
        line=line.split()
        for j in range(n):
            line[j]=float(line[j])
        a_in.append(line)

    for i in range(n):
        b_in.append(float(input()))

    return n

def print_intermediate(A,B):
    print("Coefficient Matrix: ")
    for i in range(n):
        for j in range(n):
            t = "{:.4f}".format(A[i, j])
            print(t, end=" ")
        print()
    print()

    print("Right hand constant Matrix: ")
    for i in range(n):
        t2 = "{:.4f}".format(B[i])
        print(t2)
    print()

def GaussianElimination(A,B,pivot=True,ShowAll=True):
    flag=True
    #Elimination
    for k in range(n-1):
        if flag==False:
            break
        if pivot==True:
            #Partial pivoting
            tempA=[]
            for i in range(n):
                tempA.append(A[k,i])
            temp = B[k]
            idx = k
            for i in range(k+1,n):
                if fabs(A[i,k])>fabs(A[idx,k]):
                    idx=i
                    for x in range(n):
                        tempA[x]=A[i,x]
                        temp=B[i]

            for i in range(n):
                A[idx,i]=A[k,i]
            for i in range(n):
                A[k,i]=tempA[i]
            B[idx]=B[k]
            B[k]=temp

            if idx!=k and ShowAll==True:
                print_intermediate(A,B)

        for i in range(k+1,n):
            if(A[k,k]==0):
                print("Division by zero occured")
                flag=False
                break
            factor=A[i,k]/A[k,k]
            for j in range(k,n):
                A[i,j]=A[i,j]-A[k,j]*factor
            B[i]=B[i]-B[k]*factor
            if(ShowAll==True):
                print_intermediate(A,B)

    if(flag==True):
    # Back substitution
        ans[n - 1] = B[n - 1] / A[n - 1, n - 1]
        for i in range(n - 2, -1, -1):
            sum = 0
            for j in range(i + 1, n):
                sum += A[i, j] * ans[j]
            ans[i] = (B[i] - sum) / A[i, i]

        print("The solution matrix:")
        for i in range(n):
            x = "{:.4f}".format(ans[i])
            print(x)
#From the equation of the circle and the coordinates of the three points we get the following system of linear equations

#2a + 0b - c = 4
#a - 7b - c = 50
#5a - b + c = -26

#So the coordinate matrix will be [[2,0,-1],[1,-7,-1],[5,-1,1]]
#The right hand side matrix will be [4,50,-26]

#Taking input
n=take_input()

#Converting them to numpy arrays and declaring the solution matrix
a=np.array(a_in,float)
b=np.array(b_in,float)
ans=np.zeros(n,float)

#Using Gaussian Elimination
GaussianElimination(a,b)
