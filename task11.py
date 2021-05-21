from math import *
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

    return x
def K(x):
    return 1
def L(x):
    return 2*x*x
def M(x):
    return 1
def F(x):
    return x

def bde_sol(n=10,printing=True):
    """ 
    Solve: 
    K(x)*y''(x)+L(x)*y'(x)+M(x)*y(x)=F(x)
    R*y'(a)+S*y(a)=T, V*y'(b)+W*y(b)=Z 
    """
    R=-1
    S=2
    V=0
    W=1
    T=1
    Z=3

    a=0.5
    b=0.8

    h=0.1
    n=int((b-a)/h)
    #Формирование матриц
    x=[a+h*i for i in range(0,n+1)]
    A=[[0 for i in range(n+1)] for j in range(n+1)]
    A[0][0]=-R/h+S
    A[0][1]=R/h

    B=[0 for i in range(n+1)]
    B[0]=T

    #Заполнение матриц
    for i in range(1,n):
        A[i][i-1]=1/pow(h,2)*K(x[i])-1/(2*h)*L(x[i])
        A[i][i]=-(2*K(x[i])/pow(h,2)-M(x[i]))
        A[i][i+1]=K(x[i])/pow(h,2)+L(x[i])/(2*h)
        B[i]=F(x[i])

    
    A[n][n-1]=V/h
    A[n][n]=-V/h-W
    B[n]=-Z

    A=np.array(A)
    B=np.array(B)

    y=solve_system(A,B)

    
    #Вывод результата
    if printing:
        print("BVP.Solution with step h = {}".format(h))
        for i in range(n+1):
            print(" x = {:.2f}, y = {:.4f}".format(x[i],y[i]))
    
    return x,y




    

   





x1,y1 = bde_sol()#Расчет количеством узлов 10
