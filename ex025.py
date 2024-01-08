#Procurando uma string dentro de outra

n = str(input('Digite o seu nome:')).strip()
m =n.title().split()
print(f'o seu nome tem Silva?\n'
      f'{"Silva" in m}')