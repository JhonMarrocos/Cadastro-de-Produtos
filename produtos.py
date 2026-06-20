# Bibliotecas Necessárias

from time import sleep as sl
import os
import platform
import json

# Variáveis Principais

produtos = []
arq_json = r"C:\Users\Marrocos\Desktop\Repositorio CODE\cadastro de produtos\produtos.json"

# Funções

def carregar_json():
    global produtos
    
    try:
        with open(arq_json, "r", encoding="utf-8")as arq:
            produtos = json.load(arq)

    except FileNotFoundError:
        escrever_json()
    
def escrever_json():
    with open(arq_json, "w", encoding="utf-8")as arq:
        json.dump(produtos, arq, indent=4)

def limpar_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def Barra():
    for n in range(101):
        i = "■" * (n * 25 // 101)
        print(f"r\{n}% {i}", end="", flush=True)
        sl(0.01)
    print()

def titulo(texto):
    linha = "=" * 30
    return f"{linha}\n{texto.center(len(linha))}\n{linha}"

def parar():
    input("Enter para continuar...")

def menu():
    while True:
        print(titulo("CADASTRAR PRODUTOS"))
        print("[1] Cadastrar\n[2] Remover\n[3] Modificar Preço\n[4] Verificar Estoque\n[0] Sair\n")
        
        try:
            opcao = int(input("Escolha uma Opção: "))
            return opcao
        
        except ValueError:
            print("\nEscolha uma das Opções!")
            parar()
            limpar_terminal()
            continue

menu()