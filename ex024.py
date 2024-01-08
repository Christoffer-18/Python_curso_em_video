#Verificando as primeiras letras de um texto

c = str(input('Digite o nome da sua cidade:')).strip()
s = c.lower().split()
print(f'Sua cidade começa com santo?\n'
      f'{"santo" in s[0]}')