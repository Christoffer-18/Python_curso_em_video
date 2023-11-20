# Antecessor e Sucessor

n = int(input('digite um número:'))
c = {'f': '\033[m',
     'v': '\033[31m'}
print(f'analisando o número {c["v"]}{n}{c["f"]}\n'
      f'O seu antecessor é \033[34m{n-1}\033[m \n'
      f'E seu sucessor é \033[36m{n+1}')
