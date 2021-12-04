import numpy as np
import matplotlib.pyplot as plt
import math


def func(x, r=0.06, gamma=0.55):
    return x ** 3 - 3 * r * (x ** 2) + 4 * (r ** 3) * gamma


def plot_func():
    x=np.arange(-0.02,0.12,0.001)
    fig, ax=plt.subplots()
    ax.plot(x,func(x),color='r')
    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k')
    plt.show()


def bisection_algo(lower_bound,upper_bound,max_iteration,error_tolerance=0.005):
    iteration=0
    while(True):
        if iteration == max_iteration:
            break
        mid=(lower_bound+upper_bound)/2
        if func(lower_bound)*func(mid)>0:
            lower_bound=mid
        elif func(upper_bound)*func(mid)>0:
            upper_bound=mid

        mid2=(lower_bound+upper_bound)/2
        rel_approx_error=math.fabs((mid2-mid)/mid)

        root=mid2
        iteration+=1
        if(rel_approx_error<error_tolerance):
            break

    return root




def print_table(lower_bound,upper_bound,max_iteration=20):
    print("Lower bound: ",lower_bound)
    print("Upper bound: ",upper_bound)
    print()
    print("Iteration no\t\t\tAbsolute Relative Approximate Error")
    iteration = 0
    while (True):
        iteration+=1
        if iteration == max_iteration+1:
            break
        mid = (lower_bound + upper_bound) / 2
        if func(lower_bound) * func(mid) > 0:
            lower_bound = mid
        elif func(upper_bound) * func(mid) > 0:
            upper_bound = mid

        if iteration==1:
            info="Iteration {0} \t\t\t{1}".format(iteration, "N/A")
        elif iteration<10:
            info = "Iteration {0} \t\t\t{1}".format(iteration, rel_approx_error * 100)
        else:
            info = "Iteration {0}\t\t\t{1}".format(iteration, rel_approx_error * 100)
        print(info)
        mid2 = (lower_bound + upper_bound) / 2
        rel_approx_error = math.fabs((mid2 - mid) / mid)

        root = mid2



#plotting the function
plot_func()

#Finding the approximate root
print("Approximate root of the function: ")
print(bisection_algo(0.04,0.08,20))

#Printing table showing the absolute relative approximate error
print("Table: ")
print_table(0.04,0.08)




