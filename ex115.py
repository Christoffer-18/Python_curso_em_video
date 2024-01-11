from pacotes.Minisistema.menu import *
from pacotes.Minisistema.Banco import *

arq = 'nomeEidade.txt'
if not arqExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        # OPÇÃO DE LISTAR O CONTEÚDO DE UM ARQUIVO
        escrita("Pessoas Cadastradas")
        lerArquivo(arq)
    elif resposta == 2:
        escrita("Novo Cadastro")
        nome = input("Nome: ")
        idade = input("Idade: ").strip()
        adicionarPessoa(arq,nome,idade)
    elif resposta == 3:
        escrita("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mErro! Digite uma opção válida!\033[m")
    time.sleep(0.7)