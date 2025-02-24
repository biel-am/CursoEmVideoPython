while True:
    sex = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    if sex and sex in 'M' 'F':
        break
    else:
        print('Opção inválida, digite novamente.')
print('Cadastrado com sucesso!')
