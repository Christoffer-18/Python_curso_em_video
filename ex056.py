somaidade = 0
m = 0  # média da idade
homemaisvelho = 0
maioridade = 0
mulher20 = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    n = str(input(f'Nome:')).strip().title()
    i = int(input(f'Idade:'))
    s = str(input(f'sexo [M/F]:')).strip().upper()
    somaidade += i
    if c == 1 and s == 'M':
        maioridade = i
        homemaisvelho = n
    if s == 'M' and i > maioridade:
        maioridade = i
        homemaisvelho = n
    if s == 'F' and i > 20:
        mulher20 += 1
m = somaidade / 4
print(f'A média das idades digitadas é de {m:.1f}.\n'
      f'O homem mais velho tem {maioridade} e se chama {homemaisvelho}.\n'
      f'Tem {mulher20} mulher(es) com 20 anos ou menos.')