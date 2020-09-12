import numpy as np
from sympy import *  #(symbols, cos, diff)

#DERIVADA DE FUNÇÃO
x = symbols('x')
y = x**2 + 5*x + 6
derivada = diff(y, x, 1)    #Função diff(<função derivável>, <variável de derivação>, <ordem>)
                            #<ordem> pode ser 1 para primeira derivada, 2 para segunda, etc...
print("derivada da função y = ", derivada)

derivada_no_ponto = diff(y, x).subs(x, 1)    #Faz x = 1
print("Derivada no ponto 1: ", derivada_no_ponto)



