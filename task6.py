import numpy as np
from sympy import simplify,Symbol,expand,latex,Function,N
from sympy.utilities.lambdify import lambdify
import matplotlib.pylab as plt


def spline(xdata,ydata):
    xdata=np.array(xdata)
    ydata=np.array(ydata)

    size=len(xdata)
    delta_x=np.diff(xdata)
    delta_y=np.diff(ydata)

    A=np.zeros(shape=(size,size))
    B=np.zeros(shape=(size,1))
    A[0,0]=1
    A[-1,-1]=1

    for i in range(1,size-1):
        A[i,i-1]=delta_x[i-1]
        A[i,i+1]=delta_x[i]
        A[i,i]=2*(delta_x[i-1]+delta_x[i])
        B[i,0]=3*(delta_y[i]/delta_x[i]-delta_y[i-1]/delta_x[i-1])
    c=np.dot(np.linalg.inv(A),B)

    d = np.zeros(shape = (size-1,1))
    b = np.zeros(shape = (size-1,1))
    for i in range(0,len(d)):
        d[i] = (c[i+1] - c[i]) / (3*delta_x[i])
        b[i] = (delta_y[i]/delta_x[i]) - (delta_x[i]/3)*(2*c[i] + c[i+1])    
    c=c.squeeze()
    d=d.squeeze()
    b=b.squeeze()

    x=Symbol('x')

    func=[]
    for i in range(1,size):
        func.append(expand(ydata[i-1]+b[i-1]*(x-xdata[i-1])+c[i-1]*(x-xdata[i-1])**2+d[i-1]*(x-xdata[i-1])**3))
    return func

def f_spline(x0,xdata,f):
    x=Symbol('x')
    for i in range(1,len(xdata)):
        if (x0>=xdata[i-1]) & (x0<xdata[i]):
            f_func=lambdify(x,f[i-1])
    return f_func(x0)


xdata=[0.11,0.114,0.118,0.122,0.126,0.13]
ydata=[8.65729,8.29329,7.95829,7.64893,7.36235,7.09613]


coeffs=spline(xdata,ydata)

print("Данные")
print("  x    y  ")
for i in range(len(xdata)):
    print("{:05.3f} {:05.3f}".format(xdata[i],ydata[i]))
print("Сплайн")
for i in range(1,len(xdata)):
    print("{} <= x < {} , S(x) = {}".format(xdata[i-1],xdata[i],coeffs[i-1]))
x_val=[min(xdata)+i*0.0001 for i in range(0,int(1/0.0001*(max(xdata)-min(xdata))))]
y_val=[f_spline(i,xdata,coeffs) for i in x_val]
plt.figure()
plt.plot(xdata,ydata,'ro',label='data')
plt.plot(x_val,y_val,'b-',label='spline')
plt.grid(True)
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Сплайн интерполяция')
plt.show()
