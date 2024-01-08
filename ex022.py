# Analisador de Textos
from time import sleep as t

n = str(input('Qual o seu nome inteiro?')).strip()
print('Analisando seu nome...')
t(1)
print(f'Seu nome em maiúscole é {n.upper()}')
print(f'Seu nome em minúsculo é {n.lower()}')
print(f'Seu nome tem ao todo: {len(n)-n.count(" ")} letras.')
s = n.split()
print(f'Seu primeiro nome é {s[0]} e ele tem {len(s[0])} letras.')
