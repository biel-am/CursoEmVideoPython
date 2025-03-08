from random import randint
def maior(num):
    size = len(num)
    count = 0
    print('-=' * 40)
    for n in num:
        count += 1
        if count == 1:
            biggest = n
        else:
            if biggest < n:
                biggest = n
        print(n, end=' ')
    print(f'Foram informados {size} valores ao todo')
    print(f'O maior valor informado foi {biggest}')


for c in range(0, 5):
    total_numbers = randint(1, 10)
    numbers = []
    for q in range(0, total_numbers):
        random_num = randint(0, 10)
        numbers.append(random_num)
    maior(numbers)
