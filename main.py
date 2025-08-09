arquivo = 'Ola_mundo.txt'

with open(arquivo, 'w', encoding='utf-8') as arq:
    arq.write('Olá Mundo')


arquivo2 = input('Digite um texto')

with open('arquivo2.txt', 'w', encoding='utf=8') as file:
    file.write(arquivo2)

frase = input('Mais uma; ')

with open('arquivo2.txt', 'a', encoding='utf=8') as file:
    file.write('\n' + frase)

with open('arquivo2.txt', 'r', encoding='utf--8') as file:
    for linha in file:
        print(linha.strip())