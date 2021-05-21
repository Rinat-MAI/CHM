import numpy as np


def slau_iter(A,b,eps0):
    n=len(A)
    print("Iteration method")
    print('Matrix A')
    for i in range(n):
        print(A[i])
    print("Vector b")
    print(b)

    A=np.array(A)
    b=np.array(b)
    
    B=np.zeros(shape=(n,n))
    beta=np.zeros(shape=(n,1))
    #Итерационный процесс
    for i in range(n):
        for j in range(n):
            B[i,j]=-A[i,j]/A[i,i]
            if i==j:
                B[i,j]=0
        beta[i]=b[i]/A[i,i]
    normb=np.linalg.norm(beta)
    normB=np.linalg.norm(B)
    x=[]
    x.append(beta)
    eps,delta = 100,100
    i=0
    while (eps>eps0) and (delta>eps0):
        sol=np.dot(B,x[i])+beta
        x.append(sol)
        eps=normB**i/abs(1-normB)*normb
        delta=np.linalg.norm(sol-x[i])
        i=i+1
    print("After iteration # {}, with eps = {}".format(i,eps0))
    print("Solution,vector x:")
    print(np.array(sol).squeeze())

A=[[1.6,0.12,0.57],[0.38,1.25,-0.54],[0.28,0.46,-1.12]]
b=[0.18,0.63,0.88]

slau_iter(A,b,1e-2)

