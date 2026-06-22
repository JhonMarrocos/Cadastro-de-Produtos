# Bibliotecas Necessárias

from time import sleep as sl
import os
import platform
import json

# Variáveis Principais

produtos = {}
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

def barra():
    for n in range(101):
        i = "■" * (n * 25 // 101)
        print(f"\r{n}% {i}", end="", flush=True)
        sl(0.01)
    print("\n")

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
            limpar_terminal()
            return opcao
        
        except ValueError:
            print("\nEscolha uma das Opções!")
            parar()
            limpar_terminal()
            continue

def cadastrar():
    try:
        while True:
            print(titulo('CADASTRO'))
            produto = (input('Produto: ')).strip().upper()

            if len(produto) == 0 or not produto.isalpha():
                print("Informe Qual produto para Cadrastar!\n")
                parar()
                limpar_terminal()
                continue

            if produto in produtos:
                print('O Produto ja esta na lista!\n')
                
                while True:
                    escolha = str(input('Quer adicionar a quantidade?\n[S] Sim | [N] Nao: ')).strip().upper()
                    
                    if escolha not in ('N', 'S'):
                        print('Opcao Invalida!')
                        continue
                    break
                
                if escolha != "S":
                    continue
                
                limpar_terminal()
           
            break
        
        while True:
            try:
                quantidade = int(input('Quantidade: '))

                if quantidade <= 0:
                    print('Invalido!')
                    continue
                break
            except:
                print('\nDigite apenas numeros!\n')
                parar()
                continue

        if produto in produtos:
            produtos[produto] += quantidade

        else:
            produtos[produto] = quantidade
        
        print(f'Cadastro Realizado! {produtos}')    
        
        #escrever_json()

    except Exception as erro:
        print(f'Erro Inesperado!\n{erro}')

# Main

print('Iniciando...')
barra()
parar()
limpar_terminal()

while True:
    opc = menu()
    
    if opc == 1:
        cadastrar()
        parar()
        limpar_terminal()
