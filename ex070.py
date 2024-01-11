t = contmil =cont = me = aux = 0 # t = valor total, contmil = cont de mais de mil, me = menor
barato = ' '

#quant = int(input("Quantos produtos vão ser cadastrados ?"))
#while aux < quant:

while True:
    p = str(input('Nome do prduto:')).strip().title()#produto
    valor = float(input('Preço: R$'))
    print('--' * 20)
    cont += 1
    t += valor
    if valor >= 1000:
        contmil += 1
    if cont == 1 or valor < me:
        me = valor
        barato = p
    aux += 1
    o = ' '
    while o != 'N' and o != 'S':
        o = str(input('Deseja continuar? [S/N]')).strip().upper()[0]#opção
    print('--' * 20)
    if o == 'N':
        break
#print('='* 20 , end='') #end é para a linha de baixo continuar em cima
print('{:=^40}'.format('Fim Do Programa'))
#print('='* 20)
print(f'O total de compra foi R${t:.2f}\n'
      f'temos {contmil} prudutos custando mais de R$1000.00\n'
      f'O produto mais barato foi {barato}, custando R${me:.2f}')