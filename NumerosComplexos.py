#*********************************************************************
#            MÓDULO DE OPERAÇÃO COM NÚMEROS COMPLEXOS
#*********************************************************************

header = '''
File name: NumerosComplexos.py
Package folder: <nome da pasta do código>
Description: Arquivo com os algoritmos para manipulação de números complexos
Homepage: https://github.com/LeandroTeodoroRJ/CalculoComPython
Stable: Yes
Version: 1.0
Last Update: 27.10.20
Current: Yes
Maintainer: leandroteodoro.rj@gmail.com
Depends: math
Architecture: All
Compile/Interpreter: Python 3.5.4
Access: Public
Changelog: No
Readme: No
Documents: No
Links: No
Files:  No
Other Notes: No
Code Structs Comments:
    CLASSE COMPLEXO
        init(self, a, b, mod, arg) :: a, b, mod, arg[float] -> [void] --Cria um objeto do tipo número comlexo
            -- Criar utilizando notação retangular ou polar
            a: Parte real
            b: Parte imaginária
            mod: Módulo do complexo (polar)
            arg: Argumento do complexo (polar)
        polar(self) :: [void] -> [touple]  --Retorna o complexo na forma polar
        retangular(self) :: [void] -> [touple]  --Retorna o complexo na forma retangular
        show(self) :: [void] -> [touple]  --Retorna o número complexo
        sum(self, comp) :: comp[Complexo] -> [Complexo]  --Soma dois números complexos
        sub(self, comp) :: comp[Complexo] -> [Complexo]  --Subtrai dois números complexos
        multi(self, comp) :: comp[Complexo] -> [Complexo]  --Multiplica dois números complexos
        div(self, comp) :: comp[Complexo] -> [Complexo]  --Divide dois números complexos
'''

#Bibliotecas necessárias
from math import sqrt, atan, pi, cos, sin

def help():         #Imprime o cabeçalho
    print(header)

#CLASSE COMPLEXO
class Complexo(object):
    def __init__(self, a=None, b=None, mod=None, arg=None):
        self._a = a
        self._b = b
        self._mod = mod
        self._arg = arg
        if (self._a == None and self._b == None):
            self._bk = self.retangular()
        else:
            self._bk = self.polar()

    def __del__(self):
        pass

    def polar(self):
        if (self._mod == None and self._arg == None):
            self._mod = sqrt(self._a**2+self._b**2)
            if (self._a >0):
                if (self._b > 0):
                    self._arg = atan(self._b/self._a)*180/pi    #1Q
                else:
                    self._arg = 360-(atan(abs(self._b)/self._a)*180/pi)    #4Q
            else:
                if (self._b > 0):
                    self._arg = 180-(atan(self._b/abs(self._a))*180/pi)    #2Q
                else:
                    self._arg = 180+(atan(abs(self._b)/abs(self._a))*180/pi)    #3Q
            return (('polar', self._mod, self._arg))
        else:
            return (('polar', self._mod, self._arg))

    def retangular(self):
        if (self._a == None and self._b == None):
            self._a = self._mod * cos(self._arg * pi /180)
            self._b = self._mod * sin(self._arg * pi / 180)
            return (('ret', self._a, self._b))
        else:
            return (('ret', self._a, self._b))

    def show(self):
        return (('ret', self._a, self._b, 'polar', self._mod, self._arg))

    def sum(self, comp):
        self._tmp = comp.retangular()
        self._ra = self._a + self._tmp[1]
        self._rb = self._b + self._tmp[2]
        return Complexo(a=self._ra, b=self._rb)

    def sub(self, comp):
        self._tmp = comp.retangular()
        self._ra = self._a - self._tmp[1]
        self._rb = self._b - self._tmp[2]
        return Complexo(a=self._ra, b=self._rb)

    def multi(self, comp):
        self._tmp = comp.polar()
        self._rm = self._mod * self._tmp[1]
        self._rarg = self._arg + self._tmp[2]
        return Complexo(a=self._rm, b=self._rarg)

    def div(self, comp):
        self._tmp = comp.polar()
        self._rm = self._mod / self._tmp[1]
        self._rarg = self._arg - self._tmp[2]
        return Complexo(a=self._rm, b=self._rarg)

