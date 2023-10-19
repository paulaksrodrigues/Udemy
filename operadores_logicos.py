# OPERADOR AND
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')

# else:
#     print('Sair')

# OPERADOR OR
# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')

# else:
#     print('Sair')

#OPERADOR NOT
# senha = input('Senha: ')

# if senha == '123456':
#     print('Entrou')
# else:
#     print('Senha incorreta')


#se eu quiser que a senha seja checada primeiro:
# senha = input('Senha: ')

# if senha != '123456':
#     print('Senha incorreta')

# senha= input('Senha: ')

# if not senha:
#     print('Você não digitou nada.')

# print(not True) #False
# print(not False) #True


# OPERADORES IN E NOT IN

#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# nome = 'Otávio'
# # print(nome[2])
# # print(nome[-4])

# #uma condição --- se 'á está em variavel nome , printa na tela
# print('á' in nome)
# print('z' in nome)
# #função para colocar uma linha com '-'
# print(20 * '-')
# print('á'  not in nome)
# print('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')



















