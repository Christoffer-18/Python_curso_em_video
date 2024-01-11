def leiaint(mensagem):
    #valida o dado
    while True:
        # faz o serviço do input
        print(mensagem)
        resposta = input().strip()
        if resposta.isnumeric():
            return resposta
            #return tb serve como break 
        else:
            print("\033[0;31mERRO!! Digite um número.\033[m")

#programa principal
n = leiaint("Digite um número: ")
print(f"Você digitou o número {n}.") 
