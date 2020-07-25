def opcao2(file):
    arquivo = open(f"{file}",'r')
    cont = 1
    for a in arquivo:
        cont += 1
    arquivo.close()
    nome = input(f"Informe o nome da {cont}ª pessoa: ")
    idade = input(f'Informe a idade de {nome} : ')
    escrita = open(f"{file}",'a')
    texto = list()
    texto.append(f'{nome:<30}')
    texto.append('\t')
    texto.append(idade+' anos')
    texto.append('\n')
    escrita.writelines(texto)
    escrita.close()

def opcao1(file):
    print('-' * 30)
    print(f"{'PESSOAS CADASTRADAS':^30}")
    arquivo = open(f"{file}", "r")
    print(arquivo.read())
    print()
    arquivo.close()
    print('-' * 30)

def arquivoExiste(nome):
    '''
    Verifica se um arquivo já existe, se não o cria.
    :param nome: arquivo
    :return:1 - Se o arquivo já existe
    '''
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        print("Arquivo Inexistente\nCriando arquivo!")
        a = open(nome,'wt+')
    else:
        return 1

def menu(lista):
    print('-'*30)
    print(f"{'MENU PRINCIPAL':^30}")
    print('-'*30)
    for p,a in enumerate(lista):
        print(f"\033[1;33m{p+1} - \033[m\033[;34m{a}\033[m")
    print('-'*30)

