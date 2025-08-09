
nomes = []

try:
    with open('arquivo_de_nomes.txt', 'r', encoding='utf-8') as file:
        for linha in file:
            nomes.append(linha.strip())
except FileNotFoundError:
    pass


while True:
    try:
        escolha = int(input('Escolha uma opção:\n1-Adicionar Nome \n2-Remover Nome \nOpção: '))
    except ValueError:
        print('Digite apenas 1 ou 2')
        continue
    if escolha == 1:
        nome = input('Digite seu nome:').title()        
        if nome not in nomes:        
            nomes.append(nome)
            with open('arquivo_de_nomes.txt', 'a', encoding='utf-8') as file:
                file.write(nome + '\n')
            print('Nome Salvo!')
        else:
            print('Nome já incluído!')
    elif escolha == 2:
        if len(nomes) == 0:
            print('Sem nomes para remover')
        else:
            print('Lista de Nomes')
            for nome in nomes:
                print(nome)
            remover = input('Digite o nome que deseja remover: ').title()
            if remover in nomes:
                nomes.remove(remover)
                with open('arquivo_de_nomes.txt', 'w', encoding='utf-8') as file:
                    for nome in nomes:
                        file.write(nome +'\n')
                print('Nome Removido!')
            else:
                print('Nome não está na lista!')
    else:
        print('Opçao não permitida!')
        continue


    while True:
        sair = input('Para continuar digite "continuar", para sair digite "sair"').strip().lower()
        if sair == 'sair' or sair == 'continuar':
            break 
        else:
            print('Escolha uma das opções')
    if sair == 'sair':
        break
    

with open('arquivo_de_nomes.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

print(f'O arquivo tem {len(linhas)} linhas')

nomes_ordem_alfabetica = sorted(nomes)
print()
print('---Lista em Ordem Alfabética---')
for nome in nomes_ordem_alfabetica:
    print(nome)