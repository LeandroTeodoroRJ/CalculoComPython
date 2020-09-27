#***********************************************************************
#           OPERANDO VARIÁVEIS SIMBÓLICAS NO PYTHON
#***********************************************************************
# Editor GNU Nano 2.9.3
# Interpretador Python Ver 3.6.7

#Trata s,t,x,y,z como variáveis simbólicas, ou seja, variáveis
#matemáticas que podem ser operadas
#Se quiser variávei simbólicas com mais de um caractere use, por exemplo:
# R1, C1, Lb = symbols('R1 C1 Lb')
from sympy.abc import s,t,x,y,z

from sympy import *  #Importa a biblioteca sympy

Z1 = t+1/(x*s)      #Expressão 1
Z2 = 1/(y*s+1/z)    #Expressão 2

print(Z1)
print(Z2)

FT = (Z2/Z1)+1          #Opeando as expressões
print(FT)

#Utilizando o comando simplify, note que tanto o numerador quanto o denominador
#não são expandidos.
FT_simp = simplify(FT)
print(FT_simp)

#A função cancel() mostra a expressão na formatação padrão p/q expandindo
#o numerador e o denominador
print(cancel(FT_simp))

#A função expand() expande a expressão fatorada
FT_exp = expand((x+3)*(x-2))
print(FT_exp)

#Cast string para simbólico(sympy)
>>> from sympy.abc import x
>>> a = x
>>> type(a)
<class 'sympy.core.symbol.Symbol'>
>>> from sympy.parsing.sympy_parser import parse_expr
>>> parse_expr('x')
x
>>> type(_)
<class 'sympy.core.symbol.Symbol'>


