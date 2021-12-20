# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:59:15 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def func(x):
    return 26463592 * x**3 - 266412027 * x**2 + 894000000 * x-1000000000


def func_prime(x):
    return 26463592 * 3 * x**2 - 266412027 * 2* x + 894000000

def plot_func():
    x=np.arange(-1,6,0.001)
    fig, ax=plt.subplots()
    ax.plot(x,func(x),color='r')
    ax.axhline(y=0,color='k')
    ax.axvline(x=0,color='k')
    plt.show()
    
def newton_raphson(root,error_precision):
    print("Iteration no\t\tApprox Root\t\tAbsolute Relative Approximate Error")
    iteration=1
    while(True):
        root2=root-func(root)/func_prime(root)
        relative_approx_error=math.fabs(((root2-root)/root)*100)
        root=root2
        if iteration<10:
            info = "Iteration {0} \t\t\t{1}\t\t{2}".format(iteration, root,relative_approx_error)
        else:
            info = "Iteration {0}\t\t\t{1}\t\t{2}".format(iteration, root,relative_approx_error)
        print(info)
        iteration+=1
        if(relative_approx_error<error_precision):
            break
    out="The break even point is: {0}".format(root)
    return out
        

plot_func()
print(newton_raphson(3.5,0.05))
