# """"""
# Formatação básica de strings
# s - string 
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal 
# (Caractere) (><^) (quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro 
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s ! = vamos aprender mais na frente
# """"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
# o $ pode ser substituido pelo que escolher 
print(f'{variavel:#^11}')
print(f'{variavel: ^10}')
# = - Força o número a aparecer antes dos zeros  
print(f'{1000.482525178416515:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')

