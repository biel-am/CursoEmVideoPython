salary = float(input('Digite o salário do funcionário: R$'))
if salary > 1250:
    salary_increase = salary+(salary*0.10)
else:
    salary_increase = salary + (salary * 0.15)
print(f'O salário com aumento ficou R${salary_increase}')
