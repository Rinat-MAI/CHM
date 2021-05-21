from math import *

def f(x,y):
    return 1-sin(2*x+y)+0.3*y/(x+2)

def rk4(x0,y0,xn,h):
    
    # Calculating step size
    n= int((xn-x0)/h)
    
    print('\n--------SOLUTION--------')
    print('-------------------------')    
    print('x0\ty0\tyn')
    print('-------------------------')
    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        print('-------------------------')
        y0 = yn
        x0 = x0+h
    
    print('\nAt x=%.4f, y=%.4f' %(xn,yn))

# Inputs
x0=0
y0=0
xn=1
h=0.1

# RK4 method call
rk4(x0,y0,xn,h)