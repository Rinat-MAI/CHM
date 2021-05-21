import numpy as np

def solve_system(A,B):
    A=np.array(A)
    B=np.array(B)
    n=len(B)
    #Создание диагоналей,главной и боковых
    a=A.diagonal(-1)
    a=np.insert(a,0,0)
    b=A.diagonal()
    c=A.diagonal(1)
    c=np.append(c,0)
    d=B
    print("Progonka method")
    print('Matrix A')
    for i in range(n):
        print(A[i])
    print("Vector b")
    print(b)
    P=[]
    P.append(0)
    Q=[]
    Q.append(0)
    #Расчет прогоночных коэффициентов
    for i in range(1,n+1):
        P.append(-c[i-1]/(b[i-1]+a[i-1]*P[i-1]))
        Q.append((d[i-1]-a[i-1]*Q[i-1])/(b[i-1]+a[i-1]*P[i-1]))
    
    x=[0 for i in range(n)]
    x[-1]=Q[-1]
    #Расчет х
    for i in range(1,n):
        x[n-i-1]=Q[n-i]+P[n-i]*x[n-i]
    
    print("Solution:")
    for i in range(n):
        print("x_{}={}".format(i+1,x[i]))
    return x

A=[[8,-1.5,0,0],[-1,6.5,-2,0],[0,2,10,2],[0,0,2,6]]
b=[11.5,5,15,8.5]

solve_system(A,b)