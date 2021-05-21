import numpy as np

def index_max_val(mat):
    #функция,для нахождения индекса максимального элемента в матрице
    mat=np.array(mat)
    result=np.where(mat==np.amax(mat))
    listOfCoords=list(zip(result[0],result[1]))
    return listOfCoords

def jacobi(A,eps0):
    (n,n)=np.shape(A)
    print("Matrix A")
    for i in range(n):
        print(A[i])
    upperA=np.triu(A,1)
    #Нахождение максимального элемента вне главной диагонали
    max_el=np.amax(upperA)
    (k,m)=index_max_val(upperA)[0]
    #угол поворота
    phi=1/2*np.arctan(2*A[k][m]/(A[k][k]-A[m][m]))

    E=np.eye(n)
    H=E
    H[k][k]=np.cos(phi)
    H[k][m]=-np.sin(phi)
    H[m][k]=np.sin(phi)
    H[m][m]=np.cos(phi)

    matH=[]
    matH.append(H)
    matA=[]
    matA.append(A)

    
    matA.append(np.dot(np.dot(np.linalg.inv(H),A),H))

    error=100
    i=1
    while error>eps0:
        #Итерационный процесс
        A=matA[i]
        upperA=np.triu(A,1)
        max_el=np.amax(upperA)
        (k,m)=index_max_val(upperA)[0]
        phi=1/2*np.arctan(2*A[k][m]/(A[k][k]-A[m][m]))
        E=np.eye(n)
        H=E
        H[k][k]=np.cos(phi)
        H[k][m]=-np.sin(phi)
        H[m][k]=np.sin(phi)
        H[m][m]=np.cos(phi)
        matH.append(H)
        matA.append(np.dot(np.dot(np.linalg.inv(H),A),H))
        error=max_el
        i=i+1
    print("Eigenvalues:")
    print(np.diag(matA[i]))
    print("Eigenvectors")
    vecs=np.eye(n)
    for i in range(len(matH)):
        vecs=np.dot(vecs,matH[i])
    print(vecs)

    






A=[[50+3*14,10-14,3],[10-14,20+2*14,10-14],[3,10-14,90-14]]

jacobi(A,1e-2)