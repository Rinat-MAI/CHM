
f1 = lambda x1,x2,x3,x4: 1/8*(11.5+1.5*x2)
f2 = lambda x1,x2,x3,x4: 1/6.5*(5+x1+2*x3)
f3 = lambda x1,x2,x3,x4: 1/10*(15-2*x2-2*x4)
f4 = lambda x1,x2,x3,x4: 1/6*(8.5-2*x3)

# Initial setup
x10,x20,x30,x40=0,0,0,0
count = 1

# Reading tolerable error
e = 1e-2


condition = True

while condition:
    x1 = f1(x10,x20,x30,x40)
    x2=f2(x1,x20,x30,x40)
    x3=f3(x1,x2,x30,x40)
    x4=f4(x1,x2,x3,x40)
    
    e1 = abs(x1-x10)
    e2 = abs(x2-x20)
    e3 = abs(x3-x30)
    e4=abs(x4-x40)
    
    count += 1
    x10=x1
    x20=x2
    x30=x3
    x40=x4
    
    condition = e1>e and e2>e and e3>e

print('\nSolution: x1=%0.3f, x2=%0.3f and x3 = %0.3f and x4 = %0.3f \n'% (x1,x2,x3,x4))