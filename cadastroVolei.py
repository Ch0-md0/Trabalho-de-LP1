from datetime import datetime
import json

def lerJSON():
    with open("cadastroVolei.json","r") as meuArquivo:
        return json.load(meuArquivo)

def salvarJSON(lista):
    with open("cadastroVolei.json", "w") as meuArquivo:
        json.dump(lista, meuArquivo, indent=4)

def ler_valor_nao_vazio(nome_variavel):
    valor_lido = input(f'Dê algum valor para {nome_variavel}: ').strip()
    while not valor_lido:
        print(f'Inválido! O valor para {nome_variavel} não pode ser vazio.')
        valor_lido = input(f'Dê algum valor para {nome_variavel}: ').strip()
    return valor_lido

def ler_altura(nome_variavel):
    while True:
        try:
            valor_lido = float(input(f'Defina a {nome_variavel} (em metros): '))
            if 1.40 <= valor_lido <= 2.20:
                return valor_lido
            else:
                print(f'Inválido! O valor deve estar entre 1.40 e 2.20 metros.')
        except ValueError:
            print('Inválido! Digite um número válido.')

def ler_sexo(nome_variavel):
    while True:
        valor_lido = input(f'Defina o {nome_variavel} (masculino/feminino): ').strip().lower()
        if valor_lido in ['masculino', 'feminino']:
            return valor_lido
        print('Inválido! Escolha entre masculino ou feminino.')

def ler_posicao(nome_variavel):
    opcoes = ['libero', 'levantador', 'ponteiro', 'central', 'oposto']
    print(f'Opções disponíveis: {", ".join(opcoes)}')
    while True:
        valor_lido = input(f'Defina sua {nome_variavel}: ').strip().lower()
        if valor_lido in opcoes:
            return valor_lido
        print('Inválido! Escolha uma posição válida.')

def ler_experiencia(nome_variavel):
    opcoes = ['pouca', 'mediana', 'alta']
    print(f'Opções disponíveis: {", ".join(opcoes)}')
    while True:
        valor_lido = input(f'Defina sua {nome_variavel}: ').strip().lower()
        if valor_lido in opcoes:
            return valor_lido
        print('Inválido! Escolha uma experiência válida.')

def ler_pessoa():
    print("\n--- Cadastro do Jogador ---")
    nome = ler_valor_nao_vazio('nome')
    while True:
        dataNascimentoString = input('Digite sua data de nascimento (dd/mm/aaaa): ')
        try:
            dataNascimento = datetime.strptime(dataNascimentoString, "%d/%m/%Y")
            if dataNascimento > datetime.now():
                print('Data inválida. Não pode ser uma data futura.')
            else:
                break
        except ValueError:
            print('Data inválida. Use o formato (dd/mm/aaaa).')

    altura = ler_altura('altura')
    sexo = ler_sexo('sexo')
    posicao = ler_posicao('posição')
    experiencia = ler_experiencia('experiência')

    return {
        'Nome': nome,
        'DataNascimento': dataNascimentoString,
        'Altura': altura,
        'Sexo': sexo,
        'Posicao': posicao,
        'Experiencia': experiencia
    }

def imprimir_jogador(jogador):
    print("\n--- Dados do Jogador ---")
    print(f"Nome: {jogador['Nome']}")
    print(f"Data de Nascimento: {jogador['DataNascimento']}")
    print(f"Altura: {jogador['Altura']} m")
    print(f"Sexo: {jogador['Sexo']}")
    print(f"Posição: {jogador['Posicao']}")
    print(f"Nível de Experiência: {jogador['Experiencia']}")

def exibir_jogadores(jogadores):
    if not jogadores:
        print("Nenhum jogador cadastrado.")
    else:
        for i, jogador in enumerate(jogadores):
            print(f"\nJogador {i + 1}")
            imprimir_jogador(jogador)

def incluir_jogador(jogadores):
    if len(jogadores) < 5:
        jogador = ler_pessoa()
        jogadores.append(jogador)
        salvarJSON(jogadores)
        print("Jogador cadastrado com sucesso.")
    else:
        print("Limite jogadores atingido.")

def editar_jogador(jogadores):
    if not jogadores:
        print("Nenhum jogador para editar.")
    else:
        exibir_jogadores(jogadores)
        indice = int(input("Informe o número do jogador a editar: ")) - 1
        if 0 <= indice < len(jogadores):
            jogadores[indice] = ler_pessoa()
            salvarJSON(jogadores)
            print("Jogador atualizado com sucesso.")
        else:
            print("Número inválido.")

def remover_jogador(jogadores):
    if not jogadores:
        print("Nenhum jogador para remover.")
    else:
        exibir_jogadores(jogadores)
        indice = int(input("Informe o número do jogador a remover: ")) - 1
        if 0 <= indice < len(jogadores):
            jogadores.pop(indice)
            salvarJSON(jogadores)
            print("Jogador removido com sucesso.")
        else:
            print("Número inválido.")
try:
    jogadores = lerJSON()
except FileNotFoundError:
    jogadores = []
    
salvarJSON(jogadores)

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Incluir Jogador")
        print("2. Exibir Jogadores")
        print("3. Editar Jogador")
        print("4. Remover Jogador")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_jogador(jogadores)
        elif opcao == "2":
            exibir_jogadores(jogadores)
        elif opcao == "3":
            editar_jogador(jogadores)
        elif opcao == "4":
            remover_jogador(jogadores)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input()

print("Seja bem-vindo às inscrições para o time de vôlei!")
menu()

