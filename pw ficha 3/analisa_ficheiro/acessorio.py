import os


def pede_nome():
    while True:
        nome_ficheiro = input("Insira o nome do ficheiro: ")
        if os.path.exists(nome_ficheiro):
            print(nome_ficheiro)


def gera_nome():

    nome_ficheiro = input("Insira o nome do ficheiro: ")
    if os.path.exists(nome_ficheiro):
        if nome_ficheiro.endswith(".json"):
            print("Já existe")
        else:
            with open(nome_ficheiro.split(".")[0]+".json", "w") as f:
                with open(nome_ficheiro, "r") as r:
                    dados = f.readlines()
