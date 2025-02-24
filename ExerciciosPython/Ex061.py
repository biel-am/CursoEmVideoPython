n_count = 0
first_number = int(input('Digite o primeiro termo: '))
total = first_number
reason = int(input('Digite a razão: '))
while True:
    if n_count == 10:
        break
    print(total)
    total += reason
    n_count += 1
