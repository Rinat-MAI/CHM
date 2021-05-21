xdata1=[0.11,0.114,0.118,0.122,0.126,0.13]
ydata1=[8.65729,8.29329,7.95829,7.64893,7.36235,7.09613]

x0=0.1232
x2=xdata1[1]

print("Производные первого порядка")

print("y'(",x0,")=",(ydata1[4]-ydata1[3])/(2*(xdata1[4]-xdata1[3])))
print("y'(",x2,")=",(ydata1[2]-ydata1[0])/(2*(xdata1[4]-xdata1[3])))

print("Производные второго порядка")

d2y=(ydata1[-1]-2*ydata1[-2]+ydata1[-3])/(xdata1[-1]-xdata1[-2])**2

d2y1=(ydata1[2]-2*ydata1[1]+ydata1[0])/(xdata1[-1]-xdata1[-2])**2

print("y''(",x0,")=",d2y)
print("y''(",x2,")=",d2y1)