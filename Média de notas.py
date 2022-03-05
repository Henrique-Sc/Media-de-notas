# Cores e decoração de texto
reset = '\033[m'
IR = '\033[38;5;9m'
IY = '\033[38;5;11m'
IB = '\033[38;5;12m'
bold_underline = '\033[4;1m'

# Título
print(f'{IR}-=-=-=-=-=', f'{IB}MÉDIA DE NOTAS', f'{IR}=-=-=-=-=-{reset}')

# Pergunta o nome da pessoa e quantas provas quer analisar
nome = input('Digite o seu nome: ').title().strip()
provas = int(input('Total de provas para serem analizadas: ').strip())

# Se for inserido um valor maior que dois, ele analisará os dados
while True:
    if provas < 2:
        print(f'\n{IR}Valor inválido!{reset} Digite um valor acima de dois. ')
        provas = int(input('Total de provas para serem analizadas: ').strip())
    else:
        break

# for c in range(1, provas + 1):
    
    
        


# print(f'\n{IR}VALOR INVÁLIDO! Digite um valor acima de 2.')

# print('')
#     notas = 0

#     for c in range(1, provas + 1):
#         nota = float(input(f'{IR}Digite a {c}° nota: {reset}'))
#         notas += nota

#     media = notas / provas
#     print(f'\n{nome}, a sua média foi de {bold_underline}{media:.2f}{reset}')

#     if media >= 7:
#         print(f'{IB}Aprovado!{reset}')
#     elif 7 > media >= 5:
#         print(f'{yellow}Recuperação!{reset}')
#     else:
#         print(f'{IR}Reprovado!{reset}')