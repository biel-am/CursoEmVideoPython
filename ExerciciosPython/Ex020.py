from random import sample
aluno1 = str(input('Digite o nome do 1º aluno: '))
aluno2 = str(input('Digite o nome do 2º aluno: '))
aluno3 = str(input('Digite o nome do 3º aluno: '))
aluno4 = str(input('Digite o nome do 4º aluno: '))
order = sample((aluno1, aluno2, aluno3, aluno4), 4)
print(f'A ordem de aprensentação será \n {order}')
