import numpy as np
import matplotlib.pyplot as plt

def mnk(x,y,m):
#Функция которая возвращает вектор коэффициентов полинома
    n=len(x)
    s=[0 for i in range(2*m+1)]
    t=[0 for i in range(m+1)]

    s[0]=n
    t[0]=np.sum(y)
    #Формирование нормальной системы
    for i in range(1,2*m+1):
        s[i]=np.sum([j**i for j in x])
        if i<=m:
            t[i]=np.dot([j**i for j in x],y)
    A=[[0 for i in range(m+1)] for i in range (m+1)]
    
    k=0

    for i in range(m+1):
        for j in range(m+1):
            A[i][j]=s[j+k]
        k=k+1
    #Нахождение коэффициентов полинома
    sol=np.linalg.solve(A,t)
    return sol

def f(coef,x):
    #Функция,которая рассчитывает приближающую функцию
    n=len(coef)
    return np.sum([coef[i]*x**i for i in range(n)])

def print_f(coef):
    #Доп.функция для красивого вывода полинома
    string=''
    for i in range(len(coef)):
        string+='{:.04f}*x^{}+'.format(coef[i],i)
    string=string.replace('*x^0','')
    string=string.replace('+-','-')
    string=string.replace('x^1','x')
    string=string[:-1]
    return string

def calc_nev(x,y,coef):
    #Расчет суммы квадратов ошибки
    y1=[f(coef,i) for i in x]
    nev=np.sum([(y[i]-y1[i])**2 for i in range(len(x))])
    return y1,nev

def plot_mnk(x,y,coef,y1,name,nev):
    #Построение графиков данных и полинома
    x_ar=[np.min(x)+i*(np.max(x)-np.min(x))/1000 for i in range(1000)]
    y_ar=[f(coef,i) for i in x_ar]

    plt.figure()
    plt.plot(x_ar,y_ar,'-',label=r'$ y(x) = {} $'.format(name.replace('*','\\cdot ')))
    plt.plot(x,y,'ro',label='data')
    plt.legend(loc='best')
    plt.grid('on')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.text(np.mean(x),np.mean(y),r'Сумма квадратов ошибок: ${:.03f}$'.format(nev), horizontalalignment='left',
     verticalalignment='center',bbox=dict(facecolor='cyan', alpha=0.3))
    plt.legend()
    plt.title('Метод наименьших квадратов')
    plt.show()


X,Y,m=[0,0.12,0.19,0.35,0.4,0.45,0.62,0.71,0.84,0.91,1],[1.2,1,1.3,2.1,1.6,2.6,3.6,4.5,5.5,5.5,7.1],1
C=mnk(X,Y,m)
y1,nev=calc_nev(X,Y,C)
print("Многочлен: ",print_f(C))
print("Сумма квадратов ошибок: {:.04f}".format(nev))
plot_mnk(X,Y,C,y1,print_f(C),nev)

C=mnk(X,Y,2)
y1,nev=calc_nev(X,Y,C)
print("Многочлен: ",print_f(C))
print("Сумма квадратов ошибок: {:.04f}".format(nev))
plot_mnk(X,Y,C,y1,print_f(C),nev)