from math import *

def f(x,y):
    return 1-sin(2*x+y)+0.3*y/(x+2)

def rk4(x0,y0,xn,h):
    
    # Calculating step size
    n= int((xn-x0)/h)
    x=[x0+i*h for i in range(n+1)]
    y=[]
    y.append(y0)

    
    print('\n--------SOLUTION--------')
    print('-------------------------')    
    for i in range(1,4):
        K1z=f(x[i-1],y[i-1])
        K2z=f(x[i-1]+h/2,y[i-1]+h/2*K1z)
        K3z=f(x[i-1]+h/2,y[i-1]+h/2*K2z)
        K4z=f(x[i-1]+h,y[i-1]+h*K3z)
        k = h/6*(K1z+2*K2z+2*K3z+K4z)
        
        y.append(y[i-1]+k)
    for i in range(4,n+1):
        y.append(y[i-1]+h/24*(55*f(x[i-1],y[i-1])-59*f(x[i-2],y[i-2])+37*f(x[i-3],y[i-3])-9*f(x[i-4],y[i-4])))
    for i in range(n+1):
        print(" x= {:.2f} , y={:.4f}".format(x[i],y[i]))

# Inputs
x0=0
y0=0
xn=1
h=0.1

# RK4 method call
rk4(x0,y0,xn,h)