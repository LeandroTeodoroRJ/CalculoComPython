#***********************************************************************************************
#                               MÓDULO MÉTODOS COMPUTACIONAIS
#***********************************************************************************************
'''
File name: MetodosComputacionais.py
Package folder: <nome da pasta do código>
Description: Arquivo com os algoritmos mais usados em cálculo numérico
Homepage: https://github.com/LeandroTeodoroRJ/CalculoComPython
Stable: Yes
Version: 1.0
Current: Yes
Maintainer: leandroteodoro.rj@gmail.com
Depends: numpy, sympy, matplotlib
Architecture: All
Compile/Interpreter: Python 3.5.4
Access: Public
Changelog: No
Readme: No
Documents:	No
Links: No
Files: Arquivo Exemplo de Uso	Exemplos_MetodosComputacionais.py
Other Notes: No
Code Structs Comments:
    CLASSE BISSECAO
        init(self, equacao) :: equacao[Symbolic] -> [void]  --Instância um objeto com variável da equação em 'x'
        set_limites(self, inf, sup) :: inf[float], sup[float] -> [void]   --Define os Limites Superiores e Inferiores
        gera_grafico(self) :: [void] -> [void]  --Gera o gráfico da função dentro do intervalo
        checa_raiz(self) :: [void] -> [Bool]  --Checa para saber se houve raiz no intervalo
        monotona(self) :: [void] -> [void]  --Gera gráfico da função para saber se é monótona
        retorna_iteracao(self, tol) :: tol[Float] -> [Int]  --Retorna o provável número de iterações para a tolerância
        calcula_zero(self, tol, N) :: tol[Float], N[Int] -> [Float]  --Retorna o zero da função
'''

#** MÓDULOS NECESSÁRIOS **
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#Variáveis simbólicas
from sympy.abc import x


#** MÉTODO DA BISSEÇÃO **
class bissecao(object):        #Nome da classe(classe Pai)

#** Constructor ***
    def __init__(self, equacao):
        self._exp = equacao
        self._limite_sup = 0
        self._limite_inf = 0

# ** Destructor **
    def __del__(self):
        pass

#** Mátodos de Classe **
    def set_limites(self, inf, sup):
        self._limite_inf = inf
        self._limite_sup = sup

    def gera_grafico(self):
        self.intervalo = np.linspace(self._limite_inf, self._limite_sup)  #Cria o intervalo de plotagem
        self._eixo_y = []   #Cria uma lista de valores para o eixo y de plotagem
        for i in self.intervalo:
            self._eixo_y.append(self._exp.subs(x, i).evalf())  #Resolve a função
        plt.plot(self.intervalo, self._eixo_y)
        plt.title("Gráfico da Função")
        plt.grid()
        plt.show()

    def checa_raiz(self):   #Checa se o intervalo passou pela raiz
        if ((np.sign(self._exp.subs(x, self._limite_inf).evalf())*np.sign(self._exp.subs(x, self._limite_sup).evalf())) < 0):
            return True
        else:
            return False

    def monotona(self):
        self.func_diff = diff(self._exp, x, 1)
        self.intervalo = np.linspace(self._limite_inf, self._limite_sup)  # Cria o intervalo de plotagem
        self._eixo_y = []  # Cria uma lista de valores para o eixo y de plotagem
        for i in self.intervalo:
            self._eixo_y.append(self.func_diff.subs(x, i).evalf())  # Resolve a função
        plt.plot(self.intervalo, self._eixo_y)
        plt.title("Gráfico Função Monótona")
        plt.grid()
        plt.show()

    def retorna_iteracao(self, tol):  #Retorna o número provável de iterações
        return floor(abs((log((self._limite_sup - self._limite_inf) / 2 * tol, 10) / 0.301).evalf()))

    def calcula_zero(self, tol, N):
        self.i = 1  # Esse seria o início da iteração
        self.fa = self._exp.subs(x, self._limite_inf).evalf()  # O valor da variável f(x) em "a"
        while (self.i <= N):     # Definindo as repetições
            self.k = self._limite_inf + (self._limite_sup - self._limite_inf) / 2    #Ponto médio dos intervalo
            self.fk = self._exp.subs(x, self.k).evalf()
            if ((self.fk == 0) or (np.absolute(self._limite_sup - self._limite_inf) / 2) < tol): # Condições de parada
                return self.k
            self.i = self.i + 1  # Vamos iniciar mais uma iteração
            if (self.fa * self.fk > 0):  # Aqui estamos analisando se o zero da função está do lado
                # direito de 'k', caso ele esteja vamos arrastar o limite da
                # esquerda parao valor k. O limite do intervalo será entr 'k'
                # e 'b'.
                self._limite_inf = self.k
                self.fa = self.fk
            else:  # Em caso contrário, o intervalo o limite intervalo será entre 'a'
                # 'k'
                self._limite_sup = self.k
        raise NameError('Número máximo de iterações foi excedido!!!')



