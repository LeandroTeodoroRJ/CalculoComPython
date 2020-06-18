#**************************************************************************
# 			PACOTE MATPLOTLIB
#**************************************************************************

import numpy as np
import matplotlib.pyplot as plt
# ou import pylab as plt

eixo_x = np.arange(0,10)	#Cria um array de 0 a 9
eixo_y = 2*eixo_x
curva2 = 10/(eixo_x+1)

print(eixo_x)
print(eixo_y)

#Abaixo temos as opções de plotagem, descomente para ver os resultados

#Na última linha desse arquivo temos plt.show() que é o método para
#mostrar a tela de plotagem, assim é obrigatório.

'''
plt.plot(eixo_x, eixo_y)        #Plota


plt.plot(eixo_x, eixo_y, 'r')   #Altera a cor da linha da curva
                                #r-vermelho g-verde c-ciano k-preto y-amarelo w-branco m-magenta

plt.plot(eixo_x, eixo_y, 'r--')     #Muda o estilo da linha da curva(tracejado)

plt.plot(eixo_x, eixo_y, 'r--', marker='s', linewidth=4, markersize=8)  #Marcador quadrado


plt.plot(eixo_x, eixo_y, label="Legenda da curva")
plt.xlabel("Nome eixo x")
plt.ylabel("Nome eixo y")
plt.legend()
plt.title("Título do gráfico")
plt.grid(True)                  #Plota com as linhas guia


grafico = plt.plot(eixo_x, eixo_y, eixo_x, curva2)    #Plota 2 curvas, ambas estão em função do eixo_x
plt.setp(grafico[0], label='Legenda da Curva 1')
plt.setp(grafico[1], label='Legenda da Curva 2')
plt.legend()


#Alternando para escala logaritmica
plt.plot(eixo_x, curva2)
plt.yscale("log")

#Gráfico de pontos
plt.scatter(eixo_x, eixo_y)


#Gráfico de imagem, onde os valores mais baixos são levados para o azul e os mais altos para
#o amarelo, o grafico de imagem é mais utilizado com uma matriz de muitos pontos,
#por exemplo em gráficos de arrastos aerodinâmicos.
matriz = [[1,2,3],[4,5,6]]
plt.imshow(matriz)


#imshow
mt2 = np.loadtxt("Dados_imshow.txt", float)   #Carrega os dados de um arquivo
plt.imshow(mt2, origin="lower")     #Para alterar o ponto de origem para baixo
#Cores disponíveis
#plt.gray()
#plt.jet()
#plt.hot()
#plt.bone()
#plt.hsv()
'''

plt.show()	#Mostra a tela de plotagem (Obrigatório)

