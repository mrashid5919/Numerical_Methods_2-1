import numpy as np
import matplotlib.pyplot as plt
import math

a=[0,0.01,0.03,0.05,0.07,0.09,0.11,0.13,0.15,0.17,0.19,0.21]
b=[1,1.03,1.06,1.38,2.09,3.54,6.41,12.6,22.1,39.05,65.32,99.78]
a=np.array(a)
b=np.array(b)
z=np.array([np.log(i) for i in b])

def func(d):
    return a0*np.exp(a1*d)

def plot_graph():
    x = np.arange(-0.02, 0.25, 0.001)
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.scatter(a,b)
    ax.plot(x,func(x),color='red')
    plt.show()

def linear(p,q):
    size=len(p)
    sum1=sum(p)
    sum2=sum(q)
    sum3=sum(p*p)
    sum4=sum(p*q)

    a2=((size*sum4)-(sum1*sum2))/((size*sum3)-(sum1**2))
    a1=(sum2/size)-(sum1/size)*a2
    v=math.exp(a1)

    return v,a2

#Main
a0,a1=linear(a,z)
print(a0)
print(a1)
print('y= '+str(a0)+'e^'+str(a1)+'x')
plot_graph()