#Primeiro e último nome de uma pessoa

n = str(input('Digite seu nome inteiro:')).strip().title()
n1 = n.rsplit()
print(f'Muito prazer em te conhecer, {n}!\n'
      f'Primeiro nome: {n.split()[0]}\n'
      f'Último nome: {n1[len(n1)-1]}')
