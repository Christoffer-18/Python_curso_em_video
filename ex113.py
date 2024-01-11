def leiaint(mens):
    while True:
        try:
            resposta = int(input(mens))
        except(ValueError, TypeError):
            print("\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m")
        except KeyboardInterrupt:
            print('\n\033[0;31musuário preferiu não informar esse número.\033[m')
            return 0
        else:
            return resposta

def leiaFloat(mens):
    while True:
        try:
            resposta = float(input(mens))
        except (ValueError, TypeError):
            print("\033[0;31mERRO: Por favor, digite um número flutuante válido.\033[m")
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return resposta

#programa principal
inteiro = leiaint("Digite um número inteiro: ")
flutuante = leiaFloat("DIgite um número flutuante: ")
print(f"O valor inteiro digitado foi {inteiro} e o flutuante foi {flutuante}")
