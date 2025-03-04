student = []
students = []
counter = 0
while True:
    name = str(input('Nome: ')).strip().title()
    grade_1 = float(input('Nota 1: '))
    grade_2 = float(input('Nota 2: '))
    student.append(name)
    student.append(grade_1)
    student.append(grade_2)
    students.append(student[:])
    student.clear()
    while True:
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if not op or op not in 'S' 'N':
            print('Opção Inválida, digite novamente.')
        else:
            break
    if op == 'N':
        break
print('-='*30)
while True:
    print(f'{"No.":<5} {"NOME":<15} {"MÉDIA"}')
    print('-'*30)
    for s in students:
        print(f'{counter:<5} {students[counter][0]:<15} {(students[counter][1]+students[counter][2])/2:.2f}')
        counter += 1
    counter = 0
    print('-'*45)
    while True:
        op_student = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
        if op_student == 999:
            break
        elif op_student < 0 or op_student > len(students)+1:
            print('Opção inválida, digite novamente.')
        else:
            print(f'As notas de {students[op_student][0]} são {students[op_student][1:3]}')
            break
    if op_student == 999:
        break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
