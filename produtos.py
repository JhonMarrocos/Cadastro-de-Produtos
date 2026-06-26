# Bibliotecas Necessárias ↓

from time import sleep as sl
import os
import platform
import json

# Variáveis Principais ↓

produtos = [] # ← Armazena (produtos, quantidades e preços) em uma biblioteca

local_arq = os.path.dirname(os.path.abspath(__file__)) # ← Determina o local onde o script está localizado

arq_json = os.path.join(local_arq, "produtos.json") # ← Determina onde será criado o arquivo .json

# Funções ↓

def carregar_json():
    global produtos

    try:
        with open(arq_json, "r", encoding="utf-8")as arq:
            produtos = json.load(arq)

    except FileNotFoundError:
        escrever_json()

def escrever_json():
    with open(arq_json, "w", encoding="utf-8")as arq:
        json.dump(produtos, arq, indent=4, ensure_ascii=False)

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

def encontrar_produto(nome):
    for i, item in enumerate(produtos):
        if item['Produto'] == nome:
            return i
    return -1

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

            indice = encontrar_produto(produto)

            if indice != -1:
                print('O Produto ja esta na lista!\n')

                while True:
                    escolha = str(input('Quer adicionar a quantidade?\n[S] Sim | [N] Nao: ')).strip().upper()
                    print()
                    if escolha not in ('N', 'S'):
                        print('Opcao Invalida!')
                        continue
                    break

                if escolha != "S":
                    limpar_terminal()
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

        indice = encontrar_produto(produto)

        if indice != -1:
            quantidade_antiga = produtos[indice]['Quantidade']

            limpar_terminal()
            print(f'\nQuantidade Atualizada!\nProduto: {produto}\nQuantidade: {quantidade_antiga} → {quantidade_antiga + quantidade}')

            produtos[indice]['Quantidade'] += quantidade

        else:
            produtos.append({'Produto': produto, 'Quantidade': quantidade, 'Preço': 0.0})

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

        for i, item in enumerate(produtos, start=1):
            print(f"[{i}] - {item['Produto']} = {item['Quantidade']} und\n")

        try:
            rmv = int(input("Qual Produto quer Remover? ([0] Para Cancelar): "))

            if rmv == 0:
                return

            if rmv < 1 or rmv > len(produtos):
                print('\nIndice Invalido!')
                parar()
                limpar_terminal()
                continue

            indice = rmv - 1
            produto_escolhido = produtos[indice]['Produto']
            quantidade_atual = produtos[indice]['Quantidade']

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
                del produtos[indice]
                print(f'\nO Produto: {produto_escolhido}, foi Removido!')

            else:
                produtos[indice]['Quantidade'] = nova_quantidade

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

    for i, item in enumerate(produtos, start=1):
        print(f"[{i}] - {item['Produto']} = {item['Quantidade']} und | R$ {item['Preço']:.2f}\n")
    
    return parar()

def adicionar_preco():
    while True:
        print(titulo('ADICIONAR PREÇO'))

        if len(produtos) == 0:
            limpar_terminal()
            print('\nEstoque Vazio!\n')
            parar()
            return False

        for i, item in enumerate(produtos, start=1):
            print(f"[{i}] - {item['Produto']} = R$ {item['Preço']:.2f}\n")

        try:
            esc = int(input("Qual Produto quer Atualizar o Preço? ([0] Para Cancelar): "))

            if esc == 0:
                return

            if esc < 1 or esc > len(produtos):
                print('\nIndice Invalido!')
                parar()
                limpar_terminal()
                continue

            indice = esc - 1

            preco = float(input('Novo Preço: R$ ').replace(',', '.'))

            if preco < 0:
                print('\nPreço Invalido!')
                parar()
                limpar_terminal()
                continue

            preco_antigo = produtos[indice]['Preço']
            produtos[indice]['Preço'] = preco

            print(f"\nPreço Atualizado!\nProduto: {produtos[indice]['Produto']}\nPreço: R$ {preco_antigo:.2f} → R$ {preco:.2f}")

            escrever_json()
            parar()
            limpar_terminal()

        except Exception as erro:
            print(f"\nDigite apenas numeros!\n{erro}")
            parar()
            limpar_terminal()
            continue

# Main (Inicio do Programa) ↓

print('Iniciando...')

barra() # ← Barra de Carregamento de 0 a 100%

carregar_json() # ← Adiciona o arquivo: 'produtos.json' na lista de produtos

parar() # ← Trava o terminal ate que o usuario pressione ENTER

limpar_terminal() # ← Limpa o terminal

while True:
    opc = menu() # ← Inicia o Menu

    match opc:

        case 1:
            cadastrar() # ← Cadastra e atualiza (produtos e quantidades)
            limpar_terminal()

        case 2:
            remover() # ← Remove (produtos e quantidades)
            limpar_terminal()

        case 3:
            estoque() # ← Verifica quais produtos tem na lista
            limpar_terminal()

        case 4:
            adicionar_preco() # ← Acrescenta preço aos produtos
            limpar_terminal()

        case 0:
            limpar_terminal()
            print('Saindo...')
            break

        case _:
            print('\nOpção Invalida!')
            parar()
            limpar_terminal()