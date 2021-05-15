import os


def calcula_linhas():
    nome_ficheiro = input("Insira o nome do ficheiro: ")
    if os.path.exists(nome_ficheiro):
        f = open(nome_ficheiro)
        test = len(f.readlines())
        f.close()
        print(test)


def calcula_carateres():
    nome_ficheiro = input("Insira o nome do ficheiro: ")
    if os.path.exists(nome_ficheiro):
        f = open(nome_ficheiro)
        info = f.read().replace(" ", "")
        test = len(info)
        f.close()
        print(test)


def calcula_palavra_comprida():
    nome_ficheiro = input("Insira o nome do ficheiro: ")
    if os.path.exists(nome_ficheiro):
        f = open(nome_ficheiro)
        info = f.read().replace(",", "").split()
        print(max(info, key=len))


def calcula_ocorrencia_de_letras():
    nome_ficheiro = input("Insira o nome do ficheiro: ")
    content_list = []
    dict_content = {}
    if os.path.exists(nome_ficheiro):
        with open(nome_ficheiro) as f:
            content_list = split_c(f.read())

    for val in content_list:
        val = val.lower()
        if val == '\n':
            continue
        elif val in dict_content:
            dict_content[val] += 1
        else:
            dict_content[val] = 1
    print(dict_content)


def split_c(string):
    return [char for char in string]



