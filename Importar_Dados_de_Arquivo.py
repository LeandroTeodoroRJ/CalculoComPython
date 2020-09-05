# ** IMPORTAR DADOS DE UM ARQUIIVO **

import numpy as np

#Utilizando o loadtxt do pacote numpy
dado = np.loadtxt('dados.txt', skiprows=1)      #Importa os dados e pula a primeira linha
print(dado)
print(type(dado))
print(dado.shape)

x, y, z = np.loadtxt('dados.txt', skiprows=1, unpack=True)      #Importa os dados e pula a primeira linha
                                                                #e desempacota em x, y, z
print(x)        #Vira uma matriz linha
print(y)
print(z)

#Importando uma Planilha Eletrônica salva no formato csv
print(" ")

dado2 = np.genfromtxt('planilha.csv', delimiter=',', skip_header=1, usecols=(1,2,3))    #Retorna colunas 1, 2 e 3
#Observar o caractere delimitador. Em user cols pode ser usado a função range

print(dado2)


# ** Utilizando o módulo Pandas **
# Para instalar: pip install pandas
import pandas as pd

#Abrindo um arquivo .csv (arquivo separado por vírgulas)
dado3 = pd.read_csv('planilha.csv',sep=',')

#Podemos plotar apenas alguns elementos da nossa tabela.
print(dado3.head(2))    #O número passado como argumento indica quantas linhas da tabela
                        #serão lidas. Por default(caso vazio) são 5 linhas.

#Podemos plotar apenas uma coluna
print(dado3[['Fisica']])

'''
OBS:
Em muitos casos podemos atribuir para as abscissas e ordenas os valores de cada uma das colunas,
para uma futura plotagem.
Por exemplo:
x = dados_coletados['velocidade']
y = dados_coletados['tempo']

'''
