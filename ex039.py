from datetime import date
i = int(input('Qual sua data de nascimento?'))
s = date.today().year - i
print(f'Quem nasceu em {i} tem {s} anos em {date.today().year}. ')
if s > 18:
    print(f'Você já deveria ter se alistado a {s - 18} anos.\n'
         f'foi no ano de {date.today().year - s + 18} ')
elif s < 18:
   print(f'Ainda faltam {18 - s} anos para o seu alistamento.\n'
          f'Será no ano de {18 - s + date.today().year}')
elif s == 18:
    print(f'Está na hora de se alistar.')