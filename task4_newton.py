import matplotlib.pyplot as plt
from math import *

#Функция
def f(x):
    return x**2-cos(x)
#Производная
def df(x):
    return 2*x+sin(x)

def solve_eq(x0,eps):
    #Массив для хранения значения х
    x=[]
    x.append(x0)
    x.append(x0-f(x0)/df(x0))
    i=1
    #Итерационный процесс метода Ньютона
    while (abs(x[i]-x[i-1])>eps) and (abs(f(x[i]))>eps):
        x.append(x[i]-f(x[i])/df(x[i]))
        i=i+1
    #Вывод результата
    print("Iteration № {}, solution is x = {}".format(i,x[i]))


#Вызов основной функции решения
solve_eq(1,0.01)

