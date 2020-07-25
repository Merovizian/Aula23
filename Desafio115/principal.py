from Desafio115.Lib import *
from leiaint import leiaint

arquivo = input("Informe o nome do arquivo de database: ")
arquivo = arquivo + '.txt'
while True:
    arquivoExiste(arquivo)
    menu(["Ver Pessoas Cadastradas",'Cadastrar Nova Pessoa','Sair Do Sistema'])
    menu_escolha = leiaint("\033[;35mSua Opção: \033[m",0,3)
    if menu_escolha == 1:
        opcao1(arquivo)
    if menu_escolha == 2:
        opcao2(arquivo)
    if menu_escolha == 3:
        break



