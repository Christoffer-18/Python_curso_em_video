n1 = float(input('Digite a sua nota:'))
n2 = float(input('Digite a sua outra nota:'))
r = (n1 + n2)/ 2
if r < 5:
    print(f'''Tirando {n1} e {n2}, sua média será {r} 
\033[1;31mREPROVADO!!!''')
elif r < 5 or r < 6.9:
    print(f'''Tirando {n1} e {n2}, sua média será {r} 
\033[1;34mRECUPERAÇÃO, ESTUDE MAIS!!!''')
elif r > 7:
    print(f'''Tirando {n1} e {n2}, sua média será {r} 
\033[1;4;32mAPROVADO!!!''')
