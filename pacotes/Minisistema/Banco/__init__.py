from pacotes.Minisistema.menu import *

def arqExiste(mensagem):
    try:
        a = open(mensagem, 'rt')
        a.closed
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except: 
        print("Houve um ERRO na Criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso")

def lerArquivo(nome = str):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        escrita("PESSOAS CADASTRADAS")
        linhas = a.readlines()
        for linha in linhas:
            #Cada linha é dividida em nome e número usando o delimitador ';'
            nome , numero = linha.strip().split(';')
            # Imprime o nome e o número formatados
            print(f"{nome:<30} {numero:>3} anos")
    finally:
        a.close()

def adicionarPessoa(nome_arquivo, nome_pessoa, idade):
    # Verifica se 'nome_pessoa' é uma string e 'idade' é um inteiro
    nomes = nome_pessoa.replace(' ','')
    if not nomes.isalpha():
        print(nomes)
        print("\033[0;31mErro: nome deve conter apenas letras!\033[m")
        return
    if not idade.isnumeric():
        print("\033[0;31mErro: idade deve ser um número inteiro!\033[m")
        return

    try:
        arquivo = open(nome_arquivo, 'at')
    except:
        print("Erro ao abrir o arquivo!")
    else:
        try:
            # Escreve o nome e a idade no arquivo, separados por ';'
            arquivo.write(f"{nome_pessoa};{idade}\n")
        except:
            print("Erro ao escrever no arquivo")
        else:
            print(f"Novo registro de {nome_pessoa} adicionado.")
            arquivo.close()