catalogo = []

def adicionar_filme():
    novo_filme = {
        "nome do filme": input('Digite o nome do filme: '),
        "ano de lançamento": int(input('Digite o ano de lançamento: ')),
        "genero": input('Digite o gênero do filme: '),
            "nome do diretor":input('digite o nome do diretor')
    }
    catalogo.append(novo_filme)


def atualizar_filme():
    indice = int(input('Digite o índice do filme que deseja atualizar: '))
    if 0 <= indice < len(catalogo):
        catalogo[indice]['nome do filme'] = input('Digite o novo nome do filme: ')
        catalogo[indice]['ano de lançamento'] = int(input('Digite o novo ano de lançamento: '))
        catalogo[indice]['genero'] = input('Digite o novo gênero do filme: ')
    else:
        print("Índice inválido!")

def remover_filme():
    indice = int(input('Digite o índice do filme que deseja remover: '))
    if 0 <= indice < len(catalogo):
        del catalogo[indice]
    else:
        print("Índice inválido!")

def visualizar_catalogo():
    for i, filme in enumerate(catalogo):
        print(f"Filme {i}:")
        print(f"  Nome do filme: {filme['nome do filme']}")
        print(f"  Ano de lançamento: {filme['ano de lançamento']}")
        print(f"  Gênero: {filme['genero']}")

while True:
    print("1. Adicionar filme")
    print("2. Atualizar filme")
    print("3. Remover filme")
    print("4. Visualizar catálogo")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        adicionar_filme()
    elif escolha == '2':
        atualizar_filme()
    elif escolha == '3':
        remover_filme()
    elif escolha == '4':
        visualizar_catalogo()
    elif escolha == '5':
        break
    else:
        print("Opção inválida! Tente novamente.")