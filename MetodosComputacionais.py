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
Last Update: 24.10.20
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
Files:  * Arquivo Exemplo de Uso	                Exemplos_MetodosComputacionais.py
        * Características de funcionamento          Caracteristicas_e_Limitacoes.txt
        e limitações dos métodos compu-
        tacionais.
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

    CLASSE NEWTON :: <- Ext classe bissecao
        calcula_zero(self, tol, N) :: tol[Float], N[Int] -> [Float]  --Retorna o zero da função pelo método de Newton
        retorna_iteracao(self, tol) :: --Método não implementado

    CLASSE JACOBI
        __init__(self, A, b, x0) :: A, b, x0[numpy array] -> [void]  --Cria o objeto com as respectivas matrizes de Jacobi
        calcula(self, TOL, N) :: TOL[float], N[int] -> [numpy array]  --Calcula o sist. linear onde TOL é a tolerância
                                                                        e N é o número máximo de iterações
        retorna_erro(self) :: [void] -> [float]  --Retorna o erro depois que calculado a resulução do sistema
        retorna_iteração(self) :: [void] -> [int] --Retorna o número de iterações que foi necessário

    CLASSE DADOS
        __init__(self, ex, ey) :: ex[list], ey[list] -> [void]  --Cria um objeto a partir de pontos coletados, onde
                                                                  ex são os ponto do eixo x, e
                                                                  ey são os pontos do eixo y.
        set_limites(self, inf, sup) :: inf[float], sup[float] -> [void]   --Define os Limites Superiores e Inferiores,
                                                                            os pontos devem pertencer a lista ex.
        gera_grafico(self) :: [void] -> [void]  --Gera o gráfico da função dentro do intervalo
        integral(self) :: [void] -> [float]  --Retorna o valor da integral definida dentros dos limites especificados
'''

#** MÓDULOS NECESSÁRIOS **
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from numpy import linalg

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

#** Métodos de Classe **
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
        return floor(abs((log((self._limite_sup - self._limite_inf) / tol, 2)).evalf()))

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


#** MÉTODO DE NEWTON-RAPHSON **
class Newton(bissecao):

# ** Métodos de Classe **
    def calcula_zero(self, tol, N):
        self._x0 = self._limite_sup
        self.func_diff = diff(self._exp, x, 1)
        #x1 = x0 - funcao(x0)/derivada(x0)
        self._x1 = self._x0 - (self._exp.subs(x, self._x0)/self.func_diff.subs(x, self._x0))
        self._i = 1
        while ((abs( self._x1 - self._x0) > tol) and (self._i <= N)):
            self._x0 = self._x1
            self._x1 = self._x0 - (self._exp.subs(x, self._x0) / self.func_diff.subs(x, self._x0))
            self._i = self._i + 1
        if (self._i > N):
            print('Nao houve convergencia!')
            return 0
        else:
            self._x1 = self._x1.evalf()  #Calcula a raíz
            return self._x1

    def retorna_iteracao(self, tol):  # Retorna o número provável de iterações
        print('Não implementado.')


# ** CLASSE DADOS **
class Dados(object):
    def __init__(self, ex, ey):
        self._ex = ex
        self._ey = ey

    def __del__(self):
        pass

    def set_limites(self, inf, sup):
        self._limite_inf = inf
        self._limite_sup = sup

    def integral(self):    #Aproximação do retângulo
        self.i = self._ex.index(self._limite_inf)
        self._area = 0
        while self.i < (self._ex.index(self._limite_sup)):
            self._area = self._area + ((self._ex[self.i+1]-self._ex[self.i])*self._ey[self.i])
            self.i = self.i+1
        return self._area

    def gera_grafico(self):
        self.intervalo = np.linspace(self._limite_inf, self._limite_sup)  #Cria o intervalo de plotagem
        for self.i in self._ex:
            if self.i == self._limite_inf:
                self._menor = self._ex.index(self.i)
            if self.i == self._limite_sup:
                self._maior = self._ex.index(self.i)
        self.intervalo = self._ex[self._menor:self._maior+1]
        self._eixo_y = self._ey[self._menor:self._maior+1]
        plt.plot(self.intervalo, self._eixo_y)
        plt.title("Gráfico da Função")
        plt.grid()
        plt.show()


#** MÉTODO DE JACOBI **
class Jacobi(object):

#** Constructor ***
    def __init__(self, A, b, x0):
        # Tratamento preliminar das matrizes
        self._A = A.astype('double')
        self._b = b.astype('double')
        self._x0 = x0.astype('double')
        self._erro = 0
        self._it = 0

# ** Destructor **
    def __del__(self):
        pass

#** Métodos de Classe **
    def calcula(self, TOL, N):
        self._n = np.shape(self._A)[0]  # Vai atribuir a incógnita "n" o valor do número de linhas
        # da matriz A.
        self._x = np.copy(self._x0)
        # Iterações de Jacobi
        while (self._it < N):
            self._it = self._it + 1
            for self._i in np.arange(self._n):
                self._x[self._i] = self._b[self._i]
                for self._j in np.concatenate((np.arange(0, self._i), np.arange(self._i + 1, self._n))):
                    self._x[self._i] -= self._A[self._i, self._j] * self._x0[self._j]
                self._x[self._i] /= self._A[self._i, self._i]
                # Tolerância
                if (np.linalg.norm(self._x - self._x0, np.inf) / np.linalg.norm(self._x0, np.inf) < TOL):
                    self._erro = np.linalg.norm(self._x - self._x0, np.inf) / np.linalg.norm(self._x0, np.inf)
                    return self._x
                self._x0 = np.copy(self._x)
        raise NameError('Número máximo de iterações foi ultrapassado!!')

    def retorna_erro(self):
        return self._erro

    def retorna_iteração(self):
        return self._it

