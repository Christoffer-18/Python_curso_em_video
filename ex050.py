s = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número inteiro: '))
    if num%2 == 0:
        s = s + num
        cont += 1
print(f'A soma dos {cont} números pares informados é {s}.')
