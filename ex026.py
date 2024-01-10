#Primeira e última ocorrência de uma string

b = str(input('Digite uma frase:')).strip().upper()
print(f'A letra "A" aparecu {b.count("A")} vez(es)\n'
      f'O primeiro "A" foi encontrado na posição {b.find("A")+1}\n'
      f'O último "A" apareceu na posição {b.rfind("A")+1}')