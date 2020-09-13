# EXEMPLO DE USO DA BIBLIOTECA DE MÉTODOS COMPUTACIONAIS

import MetodosComputacionais as mc
#import numpy as np
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