# # EXERCICIO 1
# entrada = input('Digite um número: ')

# # if entrada.isdigit():
# #     entrada_int = int(entrada)
# #     par_impar = entrada_int % 2 == 0
# #     par_impar_texto = 'ímpar'

# #     if par_impar:
# #         par_impar_texto = 'par'
# #     print(f'O número {entrada_int} é {par_impar_texto}')
# # else:
# #     print('Você não digitou um número inteiro')

# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')

# EXERCICIO 2

# entrada = input('Digite a hora: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora.')
# except:
#     print('Por favor, digite apenas, número inteiros')

# EXERCÍCIO 3

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    # se as 2 condições IF estiverem separadas por blocos, o ocódigo irá executar ou um ou outro
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6: #o elif da a opção de escolher um ou outro no mesmo bloco
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande.')
else: 
    print('Digite mais de uma letra.')



























