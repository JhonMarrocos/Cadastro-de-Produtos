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
    print()

def menu():
    while True:
        print(titulo("CADASTRAR PRODUTOS"))
        print("[1] Cadastrar\n[2] Remover\n[3] Verificar Estoque\n[4] Adicionar Preco\n[0] Sair\n")

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

            if len(produto) == 0 or not produto.isalnum():
                print("Informe Qual produto para Cadrastar!\n")
                parar()
                limpar_terminal()
                continue

            if produto in produtos:
                print('O Produto ja esta na lista!\n')

                while True:
                    escolha = str(input('Quer adicionar a quantidade?\n[S] Sim | [N] Nao: ')).strip().upper()
                    print()
                    if escolha not in ('N', 'S'):
                        print('Opcao Invalida!')
                        continue
                    break

                if escolha != "S":
                    continue

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
            limpar_terminal()
            print(f'\nQuantidade Atualizada!\nProduto: {produto}\nQuantidade: {produtos[produto]} → {produtos[produto] + quantidade}')
            
            produtos[produto] += quantidade

        else:
            produtos[produto] = quantidade       

            limpar_terminal()
            print(f'\nCadastro Realizado!\nProduto: {produto}\nQuantidade: {quantidade}')

        escrever_json()
        parar()

    except Exception as erro:
        print(f'Erro Inesperado!\n{erro}')

def remover():
    while True:
        print(titulo('ESTOQUE DE PRODUTOS'))

        if len(produtos) == 0:
            limpar_terminal()
            print('\nEstoque Vazio!\n')
            parar()
            return False

        list_produtos = list(produtos.keys())

        for i, (p, q) in enumerate(produtos.items(), start=1):
            print(f'[{i}] - {p} = {q} und\n')

        try:
            rmv = int(input("Qual Produto quer Remover? ([0] Para Cancelar): "))

            if rmv == 0:
                return

            if rmv < 1 or rmv > len(list_produtos):
                print('\nIndice Invalido!')
                parar()
                limpar_terminal()
                continue

            produto_escolhido = list_produtos[rmv - 1]
            quantidade_atual = produtos[produto_escolhido]

            qtd = int(input(f'Quantidade a remover (máximo {quantidade_atual}): '))

            if qtd <= 0:
                print('\nQuantidade Invalida!')
                parar()
                limpar_terminal()
                continue

            if qtd > quantidade_atual:
                print('\nQuantidade Maior que o Estoque!')
                parar()
                limpar_terminal()
                continue

            nova_quantidade = quantidade_atual - qtd

            print(f'\nQuantidade Removida!\nProduto: {produto_escolhido}\nQuantidade: {quantidade_atual} → {nova_quantidade}')

            if nova_quantidade == 0:
                del produtos[produto_escolhido]
                print(f'\nO Produto: {produto_escolhido}, foi Removido!')

            else:
                produtos[produto_escolhido] = nova_quantidade

            escrever_json()
            parar()
            limpar_terminal()

        except Exception as erro:
            print(f"\nDigite apenas numeros!\n{erro}")
            parar()
            limpar_terminal()
            continue

def estoque():
    print(titulo('ESTOQUE DE PRODUTOS'))

    if len(produtos) == 0:
        print('\nEstoque Vazio!\n')

    for i, (p, q) in enumerate(produtos.items(), start=1):
        print(f'[{i}] - {p} = {q} und\n')

    return parar()

# Main

print('Iniciando...')
barra()
carregar_json()
parar()
limpar_terminal()

while True:
    opc = menu()

    match opc:

        case 1:
            cadastrar()
            limpar_terminal()

        case 2:
            remover()
            limpar_terminal()

        case 3:
            estoque()
            limpar_terminal()