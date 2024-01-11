c = ('\033[m', #0 - sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    )

def pyhelp():
    while True:
        print(f"{c[1]}")
        print(f"~~~~~" * 5)
        print("SISTEMA DE AJUDA PyHELP")
        print("~~~~~" * 5, f"{c[0]}")
        ajuda = str(input("Função ou Biblioteca > ")).strip().lower()
        if ajuda == "fim":
            print(f"{c[4]}")
            print("ATÉ LOGO",f"{c[0]}")
            break
        else:
            N_letras = len(ajuda) + 28
            print(f"{c[2]}")
            print("~" * N_letras)
            print(f"  Acessando o manual do '{ajuda}'")
            print("~" * N_letras, f"{c[0]}")
            print(f"{c[3]}")
            print(help(ajuda))
            print(c[0])

pyhelp()