import math
import numpy as np
from matplotlib import pyplot as plt


def func(x,c=5*10**(-4)):
    return (6.73 * x + 6.725 * 10**(-8) + 7.26 * 10**(-4) *c)/(3.62 * 10**(-12) * x + 3.908 * 10**(-8) * x * c)

def trapezoid(num,lower=6.1 * 10**(-5),upper=1.22* 10**(-4)):
    h=(upper-lower)/num
    ans=func(lower)+func(upper)
    for i in range(num-1):
        ans+=2*func(lower+(i+1)*h)
    ans=(h*ans)/2
    return ans

def print_result_trapezoid(subinterval):
    print("Sub intervals\t\t\tValue\t\t\t\t\tAbsolute Relative Approximate Error")
    for i in range(subinterval):
        value=trapezoid(i+1)
        if i>0:
            rel_approx_error=math.fabs((trapezoid(i+1)-trapezoid(i))/trapezoid(i+1))
        if i==0:
            info="{0} \t\t\t\t\t{1} \t\t\t{2}".format(i+1, value, "N/A")
        else:
            info="{0} \t\t\t\t\t{1} \t\t\t{2} %".format(i+1, value, rel_approx_error * 100)
        print(info)

def single_simpson(val,height):
    term=(val+2*height-val)*(func(val)+4*func(val+height)+func(val+2*height))/6
    return term

def multiple_segment_simpson(num2,lower=6.1 * 10**(-5),upper=1.22* 10**(-4)):
    height=(upper-lower)/(2*num2)
    ans=0
    for i in range(0,(2*num2)-1,2):
        ans+=single_simpson(lower+i*height,height)
        #print(ans)
    return ans

def print_result_simpson(subinterval):
    print("Sub intervals\t\t\tValue\t\t\t\t\tAbsolute Relative Approximate Error")
    for i in range(subinterval):
        value = multiple_segment_simpson(i+1)
        if i > 0:
            rel_approx_error = math.fabs((multiple_segment_simpson(i+1) - multiple_segment_simpson(i)) / multiple_segment_simpson(i+1))
        if i == 0:
            info = "{0} \t\t\t\t\t{1} \t\t\t{2}".format(2*(i + 1), value, "N/A")
        else:
            info = "{0} \t\t\t\t\t{1} \t\t\t{2} %".format(2*(i + 1), value, rel_approx_error * 100)
        print(info)

def plot_graph():
    x = [1.22 * 10**(-4), 1.20 * 10**(-4), 1.0 * 10**(-4), 0.8 * 10**(-4), 0.6 * 10**(-4), 0.4 * 10**(-4), 0.2 * 10**(-4)]
    y=list()
    for i in x:
        y.append(multiple_segment_simpson(5,i))
    x=np.array(x)
    y=np.array(y)
    fig, ax = plt.subplots()
    ax.plot(x, y, color='r', marker='o')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_xlabel("Oxygen concentration")
    ax.set_ylabel("Time")
    plt.show()

#Main
n=int(input("Enter the number of subintervals:"))
print("Trapezoid output:")
print("Approximate value calculated using " + str(n)+ " subintervals:",end=" ")
print(trapezoid(n))
print_result_trapezoid(5)
print()
print("==========================================================")
print()
print("Simpson output:")
print("Approximate value calculated using " + str(2*n)+ " subintervals:",end=" ")
print(multiple_segment_simpson(n))
print_result_simpson(5)
plot_graph()