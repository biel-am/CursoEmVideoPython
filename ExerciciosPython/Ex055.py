biggest_weight = 0
smallest_weight = 0
for c in range(1, 6):
    weight = float(input(f'Peso {c}º pessoa (kg): '))
    if c == 1:
        biggest_weight = weight
        smallest_weight = weight
    else:
        if weight > biggest_weight:
            biggest_weight = weight
        if weight < smallest_weight:
            smallest_weight = weight
print(f'O maior peso foi: {biggest_weight}kg')
print(f'O menor peso foi: {smallest_weight}kg')
