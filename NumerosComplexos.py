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
Last Update: 28.10.20
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
    FUNCTIONS:
        help(void): --Retorna instruções de ajuda do módulo
        exemplos(void): --Retorna exemplos de uso do módulo
        
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
        return Complexo(mod=self._rm, arg=self._rarg)

    def div(self, comp):
        self._tmp = comp.polar()
        self._rm = self._mod / self._tmp[1]
        self._rarg = self._arg - self._tmp[2]
        if (self._rarg < 0):
            self._rarg = 360 + self._rarg
        return Complexo(mod=self._rm, arg=self._rarg)



extext = '''
EXEMPLOS DE USO DA BIBLIOTECA NÚMEROS COMPLEXOS

Python 3.5.4 |Continuum Analytics, Inc.| (default, Aug 14 2017, 13:41:13) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import NumerosComplexos as nc

Calcule
a) 3L25 + (2+3j)
>>> ex1 = nc.Complexo(mod=3, arg=25)
>>> ex2 = nc.Complexo(a=2, b=3)
>>> resp = ex1.sum(ex2)
>>> resp.show()
('ret', 4.718923361109949, 4.267854785222099, 'polar', 6.362611268635888, 42.126594767168)

b) 2L142 + 2L22
>>> ex1 = nc.Complexo(mod=2, arg=142)
>>> ex2 = nc.Complexo(mod=3, arg=22)
>>> resp = ex1.sum(ex2)
>>> resp.retangular()
('ret', 1.2055300564869185, 2.355142730899053)

c) 3L298 + 2L307
>>> ex1 = nc.Complexo(None, None, 3, 298)
>>> ex2 = nc.Complexo(None, None, 2, 307)
>>> resp = ex1.sum(ex2)
>>> resp.show()
('ret', 2.612044734661767, -4.2461137986713675, 'polar', 4.9852041168984895, 301.5982193413364)

d) (2+3j) + (-3+4j)
>>> ex1 = nc.Complexo(2,3)
>>> ex2 = nc.Complexo(-3,4)
>>> resp = ex1.sum(ex2)
>>> resp.retangular()
('ret', -1, 7)

d) (2+3j) * (-3+4j)
>>> ex1 = nc.Complexo(2,3)
>>> ex1.polar()
('polar', 3.605551275463989, 56.309932474020215)
>>> ex2 = nc.Complexo(-3,4)
>>> ex2.polar()
('polar', 5.0, 126.86989764584402)
>>> resp = ex1.multi(ex2)
>>> resp.polar()
('polar', 18.027756377319946, 183.17983011986422)

g) (-2-3j) / (3-5j)
>>> ex1 = nc.Complexo(-2,-3)
>>> ex2 = nc.Complexo(3,-5)
>>> resp = ex1.div(ex2)
>>> resp.polar()
('polar', 0.6183469424008422, 295.34617594194674)

'''

def exemplos():         #Imprime o cabeçalho
    print(extext)
