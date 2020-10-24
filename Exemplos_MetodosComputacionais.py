# EXEMPLO DE USO DA BIBLIOTECA DE MÉTODOS COMPUTACIONAIS

import MetodosComputacionais as mc
import numpy as np
#import matplotlib.pyplot as plt
from sympy import *

#Variáveis simbólicas
from sympy.abc import x

#Confugurando o ambiente
init_printing()

#Método da Bisseção
#Passo 1 - Criando o gráfico da função
print("Exemplo 1")
func = exp(x)-x-2
pprint(func)
exemp1 = mc.bissecao(func)
exemp1.set_limites(-2, 0)
exemp1.gera_grafico()

#Passo 2 - Saber se o intervalo passou pela raiz
print("Passou pela raiz?")
print(exemp1.checa_raiz())

#Passo 3 - Saber se a função é monotona no intervalo
print("É monótona no intervalo?")
exemp1.monotona()

#Passo 4 - Retornar o múmero de iterações
print("Qual o provável número de iterações?")
print(exemp1.retorna_iteracao(0.1))

#Passo 5 - Calcular o Zero da função
print("Calculando o Zero.")
print(exemp1.calcula_zero(0.1, 5))

#MÉTODO DE JACOBI PARA SISTEMAS LINEARES
print('\nResolução de Sistemas Lineares Pelo método de Jacobi')
'''
Sistema em questão:
(I)     -3.x1+x2+x3=2
(II)    2.x1+5.x2+x3=5
(III)   2.x1+3.x2+7.x3=-17
'''
#Declarando as matrizes
A = np.array ([[-3,1,1],[2,5,1],[2,3,7]])   #Matriz dos coeficientes
b = np.array ([[2],[5],[-17]])              #Matriz dos termos isolados
x0 = np.array ([[1],[1],[-1]])              #Vetor inicial (arbitrado)

#Declarando a tolerência e o número máximo de iterações
TOL = 10**-2
N = 50
ex1 = mc.Jacobi(A, b, x0)
print('Matriz resultado')
print(ex1.calcula(TOL, N))
print('\nRetornando o erro')
print(ex1.retorna_erro())
print('\nRetornando o número de iterações que foi necessário')
print(ex1.retorna_iteração())