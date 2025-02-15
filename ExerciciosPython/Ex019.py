from random import choice
aluno1 = str(input('Digite o nome do 1º aluno: '))
aluno2 = str(input('Digite o nome do 2º aluno: '))
aluno3 = str(input('Digite o nome do 3º aluno: '))
aluno4 = str(input('Digite o nome do 4º aluno: '))
chosen = choice((aluno1, aluno2, aluno3, aluno4))
print(f'O aluno escolhido foi {chosen}')
