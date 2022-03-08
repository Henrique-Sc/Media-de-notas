# Cores e decoração de texto
reset = '\033[m'
IR = '\033[38;5;9m'
IY = '\033[38;5;11m'
IB = '\033[38;5;12m'
bold_underline = '\033[4;1m'

# Título
print(f'{IR}-=-=-=-={reset}', 'MÉDIA DE NOTAS', f'{IR}=-=-=-=-{reset}')

# Pergunta o nome da pessoa e quantas provas quer analisar
nome = input('\nDigite o seu nome: ').title().strip()
provas = int(input('Total de provas para serem analizadas: ').strip())

# Se for inserido um valor maior que dois, ele analisará os dados
while True:
    if provas < 2:
        print(f'\n{IR}Valor inválido!{reset} Digite um valor acima de dois. ')
        provas = int(input('Total de provas para serem analizadas: ').strip())
    else:
        break
print('')

# Declarando as variáveis
aluno = {'Nome': nome}
notas = []

# For para inserir as notas
for c in range(1, provas + 1):
    nota = float(input(f'Digite a {c}ª nota: ').strip())
    notas.append(nota)
    del nota
    
# Colocando os dados em um dicionário
aluno['Notas'] = notas[:]
aluno['Média'] = sum(aluno['Notas']) / len(aluno['Notas'])

if aluno['Média'] < 5:
    aluno['Situação'] = f'{IR}Reprovado{reset}'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = f'{IY}Recuperação{reset}'
else:
    aluno['Situação'] = f'{IB}Aprovado{reset}'

# Linha para design
print('\n----------------------\n')

# Mostrando os dados
for k, v in aluno.items():
    if v == aluno['Média']:
        print(f'{k}: {v:.2f}')
    else:
        print(f'{k}: {v}')
        
# Linha para design
print('\n----------------------\n')

print(f'--- (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Fim da execução ✧ﾟ･: *ヽ(◕ヮ◕ヽ) ---')
