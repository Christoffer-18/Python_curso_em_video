soma = 0  #Acumulador normalmete soma um valor
cont = 0  # Um contador normalmente soma +1
for c in range(1,500, 2):
    if c % 3 ==0:
       cont += 1
       soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma} ')