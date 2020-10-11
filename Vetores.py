# MÓDULO DE OPERAÇÕES COM VETORES

from sympy import *

def escalar(v1, v2):
    if (len(v1) == 2 and len(v2) == 2):
        return v1[0]*v2[0]+v1[1]*v2[1]
    if (len(v1) == 3 and len(v2) == 3):
        return v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
    if (len(v1) > 3 and len(v2) > 3):
        print('Vetor maior que 3 dimensões (x,y,z)')
    else:
        print('Erro de dimensão de vetores.')

def absoluto(v1):
    if len(v1) == 2:
        resultado = sqrt(v1[0]**2+v1[1]**2)
        resultado = resultado.evalf()
        return resultado
    if len(v1) == 3:
        resultado = sqrt(v1[0] ** 2 + v1[1] ** 2 + v1[2] ** 2)
        resultado = resultado.evalf()
        return resultado
    if len(v1) > 3:
        print('Vetor maior que 3 dimensões (x,y,z)')

def vetorial(v1, v2):
    vi = (v1[1]*v2[2]-v1[2]*v2[1])
    vj = -(v1[0]*v2[2]-v1[2]*v2[0])
    vk = (v1[0]*v2[1]-v1[1]*v2[0])
    return Matrix([[vi, vj, vk]])

def versor(v1):
    abt = absoluto(v1)
    return Matrix([[v1[0]/abt, v1[1]/abt, v1[2]/abt]])

def angulo(v1, v2):
    teta = acos(escalar(v1, v2)/(absoluto(v1)*absoluto(v2)))*180/pi
    teta = teta.evalf()
    return teta

def projecao(v1, v2):
    proj = (escalar(v1, v2)/escalar(v2, v2)) * v2
    proj = proj.evalf()
    return proj

'''
# *************************************************************************
# EXEMPLO DE USO
init_printing()

print('\nDeclarando um vetor no R2')
vec1 = Matrix([[1, 2]])
vec2 = Matrix([[3, 4]])
pprint(vec1)
pprint(vec2)
print('A dimensão do vetor é: ' + str(len(vec1)))

print('\nDeclarando um vetor no R3')
vec3 = Matrix([[1, 2, 3]])
vec4 = Matrix([[4, 5, 6]])
pprint(vec3)
pprint(vec4)
print('A dimensão do vetor é: ' + str(len(vec4)))

print('\nSoma de vetores')
pprint(vec1+vec2)
pprint(vec3+vec4)
#pprint(vec1+vec4)   #Erro de diferença de dimensão

print('\nMultiplicação por um escalar')
pprint(5*vec1)

print('\nProduto Escalar')
print(escalar(vec1, vec2))

print('\nProduto vetorial')
pprint(vetorial(vec3, vec4))

print('\nMódulo de um vetor')
print(absoluto(vec1))
print(absoluto(vec4))

print('\nVersor')
pprint(versor(vec4))

print('\nÂngulo entre dois vetores')
print(angulo(vec3, vec4))

print('\nProjeção de v1 sobre v2')
pprint(projecao(vec3, vec4))
'''
