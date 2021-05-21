
from math import *
import matplotlib.pyplot as plt

#Функция
def f(x):
    return x**2-cos(x)
#Функция,к котоорой приводим для итераций
def phi(x):
    return sqrt(cos(x))

def solve_eq(x0,eps):
    #Массив для х
    x=[]
    x.append(x0)
    x.append(phi(x[0]))
    i=0
    #Итерационный процесс
    print("table")
    while abs(x[i+1]-x[i])>eps and abs(f(x[i]))>eps:
        x.append(phi(x[i+1]))
        i=i+1
        print(i,x[i],abs(x[i+1]-x[i]))
    print("Iteration № {}, solution is x = {}".format(i,x[i]))


#Основная функция
solve_eq(1,0.01)

