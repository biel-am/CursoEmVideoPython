words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for w in words:
    print(f'Na palavra {w.upper()} temos ', end='')
    for l in w:
        if l in 'a' 'e' 'i' 'o' 'u':
            print(l, end=' ')
    print('')
