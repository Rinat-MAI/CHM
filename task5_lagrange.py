from math import *
import numpy as np
from sympy import simplify,Symbol,expand,latex,Function,N
from sympy.utilities.lambdify import lambdify
import matplotlib.pylab as plt



def lagrange(xdata,ydata,x0=None):
    x=Symbol('x')
    #Расчет многочлена Лагранжа
    polyval=0
    for j in range(len(xdata)):
        prod=1
        for i in range(len(xdata)):
            if i==j:
                prod=prod*1
            else:
                prod=prod*(x-xdata[i])/(xdata[j]-xdata[i])
        polyval=polyval+prod*ydata[j]
    #Формирование строки для вывода,и функции для расчета значений
    polyval=N(expand(polyval),5)
    string=str(polyval).replace("**","^")
    string=string.replace("*"," \\cdot ")
    poly_fun=lambdify(x,polyval)
    #Массивы для построения графиков
    x_val=[min(xdata)+0.00001*i for i in range(int(1/0.00001*(max(xdata)-min(xdata))))]
    y_val=[poly_fun(i) for i in x_val]

    print("Данные")
    print("  x    y  ")
    for i in range(len(xdata)):
        print("{:05.3f} {:05.3f}".format(xdata[i],ydata[i]))
    print("Многочлен Лагранжа:")
    print('P(x) = '+string.replace('\\cdot','*'))
    if x0 != None:
        #Расчет значения в точке,погрешности
        poly_x0_val=poly_fun(x0)
        print('Значение в точке,P(x0) = {}'.format(poly_x0_val))

    plt.figure(figsize=[8,6])
    #Создание графиков
    plt.plot(x_val,y_val,'b-',label=r'$ P(x)={} $'.format(string))
    plt.plot(xdata,ydata,'ro',label=r'Табличная функция  $y(x)$')
    if x0 != None:
        plt.text(np.mean(x_val),np.mean(y_val),r' Значение полинома в точке $ P({})= {:0.4f}$'.format(x0,poly_x0_val), horizontalalignment='left',
     verticalalignment='center',bbox=dict(facecolor='cyan', alpha=0.3))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Полином Лагранжа')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()


    

xdata1=[0.11,0.114,0.118,0.122,0.126,0.13]
ydata1=[8.65729,8.29329,7.95829,7.64893,7.36235,7.09613]

#Вызов функции с двумя наборами данных
lagrange(xdata1,ydata1,0.1232)