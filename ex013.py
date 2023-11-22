# Reajuste Salarial

s = float(input('digite o seu salário: R$ '))
p = float(input('digite a porcentagem que ele vai subir:'))
r = (s*p)/100
print(f'O valor vai ter um aumento de {r:.2f} \n'
      f'O valor total vai ser  {r+s:.2f} \n'
      f'se fosse subtrair seria {(s-r):.2f}')