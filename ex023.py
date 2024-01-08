#Separando dígitos de um número

n = int(input('digite um número entre 0 e 9999:'))
a = n // 1 % 10
b = n // 10 % 10
c = n // 100 % 10
d =n // 1000 % 10
C = {"f": "\033[m",
     "p": "\033[7;30m",
     "ci": "\033[36m"}
print(f'Analizando o número {C["p"]}{n}{C["f"]}...\n'
      f'Unidade:{a}\n'
      f'Dezena:{b}\n'
      f'Centena:{c}\n'
      f'Milhar:{d}')
