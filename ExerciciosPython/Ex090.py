student = {}
student['name'] = str(input('Digite o nome do aluno: ')).strip().title()
student['grade_avg'] = float(input('Digite a média do aluno: '))
if student['grade_avg'] < 6:
    student['situation'] = 'Reprovado'
else:
    student['situation'] = 'Aprovado'
print(f'Situação de {student['name']} é igual a {student['situation']}')
