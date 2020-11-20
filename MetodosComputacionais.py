#***********************************************************************************************
#                               MÓDULO MÉTODOS COMPUTACIONAIS
#***********************************************************************************************

header = '''
File name: MetodosComputacionais.py
Package folder: <nome da pasta do código>
Description: Arquivo com os algoritmos mais usados em cálculo numérico
Homepage: https://github.com/LeandroTeodoroRJ/CalculoComPython
Stable: Yes
Version: 1.0
Last Update: 20.11.20
Current: Yes
Maintainer: leandroteodoro.rj@gmail.com
Contributor(special thanks): Prof. Eric Amâncio (UNESA) 
Depends: numpy, sympy, matplotlib
Architecture: PC-32, PC-64
Compile/Interpreter: Python 3.5.4
Access: Public
Changelog: No
Readme: No
Documents:	No
Links: No
Files:  * Características de funcionamento          Caracteristicas_e_Limitacoes.txt
        e limitações dos métodos compu-
        tacionais.
Other Notes: No
Code Structs Comments:
    FUNCTIONS:
        help(void): --Retorna instruções de ajuda do módulo
        exemplos(void): --Retorna exemplos de uso do módulo

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
        init(self, A, b, x0) :: A, b, x0[numpy array] -> [void]  --Cria o objeto com as respectivas matrizes de Jacobi
                                                                   Onde:
                                                                   A: Matriz dos coeficientes
                                                                   b: Matriz dos termos independentes
                                                                   x0: Matriz de iteração inicial
        calcula(self, TOL, N) :: TOL[float], N[int] -> [numpy array]  --Calcula o sist. linear onde TOL é a tolerância
                                                                        e N é o número máximo de iterações
        retorna_erro(self) :: [void] -> [float]  --Retorna o erro depois que calculado a resulução do sistema
        retorna_iteração(self) :: [void] -> [int] --Retorna o número de iterações que foi necessário
        pivotemanto_parcial(self) :: [void] -> [void]  --Executa o pivoteamento parcial que gera outro sistema linear 
                                                         equivalente quando o original não converge para uma solução
        retorna_matriz_A(self) :: [void] -> [np.array]  --Retorna a matriz A 
        retorna_matriz_b(self) :: [void] -> [np.array]  --Retorna a matriz b

    CLASSE DADOS
        init(self, ex, ey) :: ex[np.array], ey[np.array] -> [void]  --Cria um objeto a partir de pontos coletados, onde
                                                                      ex: São os ponto do eixo x, e
                                                                      ey: São os pontos do eixo y.
        set_limites(self, inf, sup) :: inf[float], sup[float] -> [void]   --Define os Limites Superiores e Inferiores,
                                                                            os pontos devem pertencer a lista ex.
        gera_grafico(self) :: [void] -> [void]  --Gera o gráfico da função dentro do intervalo
        integral(self) :: [void] -> [float]  --Retorna o valor da integral definida dentros dos limites especificados
        get_valores_x(self) :: [void] -> [numpy array]  --Retorna os valores do eixo X
        get_valores_y(self) :: [void] -> [numpy array]  --Retorna os valores do eixo Y

    CLASSE INTERPOLAÇÃO POLINOMIAL
        init(self, objDados) :: objDados[Dados] -> [void]  --Gera um objeto do tipo Interpolação Polinomial
        regressao(self) :: [void] -> [void]  --Faz os cálculos necessários para a regressão
        get_poli(self) ::  [void]  -> [symbol]   --Retorna o polinômio em x
        matriz_dd(self) :: [void] -> [numpy array]  --Retorna matriz dos coeficientes do polinômio não simplificado
        poli_x(self)  :: [void]  -> [symbol]   --Retorna o polinômio simplificado em 'x'
        matriz(self) :: [void] -> [numpy array]  --Retorna matriz da Diferença Dividida
        gera_grafico(self) :: [void] -> [void]  --Gera o gráfico do polinômio 
        
'''

def help():
    print(header)


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

    def get_valores_x(self):
        return self._ex

    def get_valores_y(self):
        return self._ey


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

    def pivoteamento_parcial(self):
        # Acesse as linhas
        for self._i in range(len(self._A)):
            # Verifique qual o maior pivô na na coluna de análise
            self._pivo = np.fabs(self._A[self._i][self._i])
            self._linhapivo = self._i
            for self._j in range(self._i + 1, len(self._A)):
                if np.fabs(self._A[self._j][self._i]) > self._pivo:
                    self._pivo = np.fabs(self._A[self._j][self._i])
                    self._linhapivo = self._j
            # Permute as linhas
            if self._linhapivo != self._i:
                self._linhaAuxiliar = self._A[self._i]
                self._A[self._i] = self._A[self._linhapivo]
                self._A[self._linhapivo] = self._linhaAuxiliar

                self._bAuxiliar = self._b[self._i]
                self._b[self._i] = self._b[self._linhapivo]
                self._b[self._linhapivo] = self._bAuxiliar
            # Eliminação Gaussiana
            for self._m in range(self._i + 1, len(self._A)):
                self._multiplicador = self._A[self._m][self._i] / self._A[self._i][self._i]
                for self._n in range(self._i, len(self._A)):
                    self._A[self._m][self._n] -= self._multiplicador * self._A[self._i][self._n]
                self._b[self._m] -= self._multiplicador * self._b[self._i]
        # Printar matriz escalonada e o vetor b escalonado
        self._A_resp = np.empty((len(self._A), len(self._A)))
        for self._k in range(len(self._A)):
            self._A_resp[self._k] = self._A[self._k]
        self._A = self._A_resp
        print('\n')

    def retorna_matriz_A(self):
        return self._A

    def retorna_matriz_b(self):
        return self._b

#** MÉTODO DE INTERPOLAÇÃO POLINOMIAL **
class InterpolacaoPolinomial(object):

#** Constructor ***
    def __init__(self, objDados):
        # Insira os dados de entrada
        self._xi = objDados.get_valores_x()
        self._fi = objDados.get_valores_y()

# ** Destructor **
    def __del__(self):
        pass


# ** Médodos de Classe **
    def regressao(self):
        # PROCEDIMIENTO
        # Tabela para armazenar os resultados do método
        self._titulo = ['i', 'xi', 'fi']

        self._n = len(self._xi)  # Comprimento da linha xi

        self._ki = np.arange(0, self._n, 1)  # Criando uma matriz linha com 4 elementos

        self._matriz = np.concatenate(([self._ki], [self._xi], [self._fi]), axis=0)  # Organizando todos os valore
        # em uma matriz, matriz linha
        # compõe uma linha.

        self._matriz = np.transpose(self._matriz)  # Transponha a matriz para obter o formato onde
        # onde "i", "xi" e "fi" cada um represente uma
        # coluna.

        self._dd = np.zeros(shape=(self._n, self._n), dtype=float)  # Criando uma matriz vazia a qual
        # atribuiremos valores futuros

        self._matriz = np.concatenate((self._matriz, self._dd), axis=1)  # Agora estamos agrupando uma matriz
        # quadrada vazia "n x n" a matriz
        # anterior. Como se trata junção de
        # matrizes axis = 1.

        # Calcula matriz, inicia-se na coluna 4 (lembre-se que 0 é a primeira coluna)
        # Esse valor precisa ser mudado quando estamos trabalhando com polinômio maior
        [self._n, self._m] = np.shape(self._matriz)
        self._coluna = self._n - 1
        self._j = 3
        while (self._j < self._m):
            # Adicionar título para cada coluna (utilizamos j - 2 pq iniciamos com
            # j = 3)
            self._titulo.append('self._dd' + str(self._j - 2))

            self._espassar = self._j - 2  # Servirá para adicionar os valores nas colunas vazias
            self._i = 0
            while (self._i < self._coluna):
                self._numerador = self._matriz[self._i + 1, self._j - 1] - self._matriz[self._i, self._j - 1]
                self._denominador = self._xi[self._i + self._espassar] - self._xi[self._i]
                self._matriz[self._i, self._j] = self._numerador / self._denominador
                self._i = self._i + 1
            self._coluna = self._coluna - 1
            self._j = self._j + 1


        # POLINOMIO com diferencias divididas
        # caso: pontos equidistantes no eixo x
        self._h = self._xi[1] - self._xi[0]

        self._dd = self._matriz[0, 3:]  # pega os valores da primeira linha e quarta coluna

        self._n = len(self._dd)


        # Expressão do polinômio com o Sympy
        #x = sym.Symbol('x')
        self._polinomio = self._fi[0]
        for self._j in range(1, self._n, 1):
            self._fator = self._dd[self._j - 1]
            self._termino = 1
            for self._k in range(0, self._j, 1):
                self._termino = self._termino * (x - self._xi[self._k])
            self._polinomio = self._polinomio + self._termino * self._fator
        # Simplifique multiplicando (x-self._xi)
        self._polisimple = self._polinomio.expand()

        # polinômio para avaliação numérica
        self._px = lambdify(x, self._polisimple)

        # Pontos para o gráfico
        self._amostra = 101
        self._a = np.min(self._xi)
        self._b = np.max(self._xi)
        self._pxi = np.linspace(self._a, self._b, self._amostra)
        self._pfi = self._px(self._pxi)


    def get_poli(self):
        return self._polinomio

    def poli_x(self):
        return self._polisimple

    def matriz_dd(self):
        #print([self._titulo])
        return self._dd

    def matriz(self):
        return self._matriz


    def gera_grafico(self):
        # Gráfico
        plt.plot(self._xi, self._fi, 'o', label='Pontos')
        ##for i in range(0,self._n,1):
        ##    plt.axvline(self._xi[i],ls='--', color='yellow')
        plt.plot(self._pxi, self._pfi, label='Interpolação Polinomial')
        plt.legend()
        plt.xlabel('xi')
        plt.ylabel('fi')
        plt.title('Interpolação Diferenças Divididas de Newton')
        plt.show()

extext = '''
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
print('Resolução de Sistemas Lineares Pelo método de Jacobi')

Sistema em questão:
(I)     -3.x1+x2+x3=2
(II)    2.x1+5.x2+x3=5
(III)   2.x1+3.x2+7.x3=-17

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
print('Retornando o erro')
print(ex1.retorna_erro())
print('Retornando o número de iterações que foi necessário')
print(ex1.retorna_iteração())

# **** MÉTODO DA INTERPOLAÇÃO POLINOMIAL ****
import numpy as np
import MetodosComputacionais as mc

# Insirindo os dados de entrada (pontos)
xi = np.array([-1, 0, 1, 3])    #Pontos no eixo x
fi = np.array([3, 1, 3, 43])    #Pondos do eixo y (imagem)

pontos = mc.Dados(xi, fi)
polinomial = mc.InterpolacaoPolinomial(pontos)

polinomial.regressao()

# Dados de Saída
print('Matriz Diferenças Divididas:')
mtzdd = polinomial.matriz()
print('[[i, xi, fi, dd1, dd2, dd3, dd4]]')
print(mtzdd)
print(type(mtzdd))

print('')
print('Polinomio não simplificado: ')
poli = polinomial.get_poli()
print(poli)
print(type(poli))

print('')
print('Matriz dos coeficientes do polinômio não simplificado:')
print('dd: ')
mdd = polinomial.matriz_dd()
print(mdd)
print(type(mdd))

print('')
print('polinomio simplificado: ')
poli = polinomial.poli_x()
print(poli)
print(type(poli))

#Gera o gráfico do polinimio
polinomial.gera_grafico()

'''

def exemplos():         #Imprime os exemplos
    print(extext)
