"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""
# em python o indice final não é incluido

variavel = 'Olá mundo'
print(variavel[:]) # não fatia nada
print(variavel[0:5])
print(variavel[0:])
print(variavel[4:])
print(variavel[-9:-3])
print(variavel[4])
print(len(variavel)) # conta os caracteres
print(variavel[0:len(variavel):1])
print(variavel[0:9:1])
print(variavel[0:9:2])
print(variavel[::-1]) # inverte a string









