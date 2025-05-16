print("=== CATALOGO ===")
print("Escolha uma opção:")
while True:
    print("\n1. Filmes \n2. Series \n3. Livros \n4, Jogos \n5. Sair")
    opcao = int(input("Escolha uma opção entre 1 a 5: "))
    if opcao == 1:
        print("=== FILMES ===")
        filmes = []
        while True:
            opcao_filme = int(input("\n1. Adicionar Filme \n2. Remover Filme \n3. Exibir Filmes \n4. Voltar \nEscolha uma opção entre 1 a 4: "))
            if opcao_filme == 1:
                filme = input("Digite o nome do filme: ")
                filmes.append(filme)
                print(f"Filme '{filme}' adicionado ao catálogo.")
            elif opcao_filme == 2:
                if not filmes:
                    print("Nenhum filme na lista.")
                else:
                    for i, filme in enumerate(filmes, 1):
                        print(f"{i}. {filme}")
                    excluir = int(input("Qual filme deseja excluir?: "))
                    if 0 < excluir <= len(filmes):
                        filmes.pop(excluir - 1)
                        print("Filme removido com sucesso!")
                    else:
                        print("Erro: Opção inválida.")
            elif opcao_filme == 3:
                if not filmes:
                    print("Nenhum filme no catálogo.")
                else:
                    print("Filmes no catálogo:")
                    for i, filme in enumerate(filmes, 1):
                        print(f"{i}. {filme}")
            elif opcao_filme == 4:
                break
            else:
                print("Opção inválida.")
    elif opcao == 2:
        print("=== SERIES ===")
        series = []
        while True:
            opcao_serie = int(input("\n1. Adicionar Série \n2. Remover Série \n3. Exibir Séries \n4. Voltar \nEscolha uma opção entre 1 a 4: "))
            if opcao_serie == 1:
                serie = input("Digite o nome da série: ")
                series.append(serie)
                print(f"Série '{serie}' adicionada ao catálogo.")
            elif opcao_serie == 2:
                if not series:
                    print("Nenhuma série na lista.")
                else:
                    for i, serie in enumerate(series, 1):
                        print(f"{i}. {serie}")
                    excluir = int(input("Qual série deseja excluir?: "))
                    if 0 < excluir <= len(series):
                        series.pop(excluir - 1)
                        print("Série removida com sucesso!")
                    else:
                        print("Erro: Opção inválida.")
            elif opcao_serie == 3:
                if not series:
                    print("Nenhuma série no catálogo.")
                else:
                    print("Séries no catálogo:")
                    for i, serie in enumerate(series, 1):
                        print(f"{i}. {serie}")
            elif opcao_serie == 4:
                break
            else:
                print("Opção inválida.")
    elif opcao == 3:
        print("=== LIVROS ===")
        livros = []
        while True:
            opcao_livro = int(input("\n1. Adicionar Livro \n2. Remover Livro \n3. Exibir Livros \n4. Voltar \nEscolha uma opção entre 1 a 4: "))
            if opcao_livro == 1:
                livro = input("Digite o nome do livro: ")
                livros.append(livro)
                print(f"Livro '{livro}' adicionado ao catálogo.")
            elif opcao_livro == 2:
                if not livros:
                    print("Nenhum livro na lista.")
                else:
                    for i, livro in enumerate(livros, 1):
                        print(f"{i}. {livro}")
                    excluir = int(input("Qual livro deseja excluir?: "))
                    if 0 < excluir <= len(livros):
                        livros.pop(excluir - 1)
                        print("Livro removido com sucesso!")
                    else:
                        print("Erro: Opção inválida.")
            elif opcao_livro == 3:
                if not livros:
                    print("Nenhum livro no catálogo.")
                else:
                    print("Livros no catálogo:")
                    for i, livro in enumerate(livros, 1):
                        print(f"{i}. {livro}")
            elif opcao_livro == 4:
                break
            else:
                print("Opção inválida.")
    elif opcao == 4:
        print("=== JOGOS ===")
        jogos = []
        while True:
            opcao_jogo = int(input("\n1. Adicionar Jogo \n2. Remover Jogo \n3. Exibir Jogos \n4. Voltar \nEscolha uma opção entre 1 a 4: "))
            if opcao_jogo == 1:
                jogo = input("Digite o nome do jogo: ")
                jogos.append(jogo)
                print(f"Jogo '{jogo}' adicionado ao catálogo.")
            elif opcao_jogo == 2:
                if not jogos:
                    print("Nenhum jogo na lista.")
                else:
                    for i, jogo in enumerate(jogos, 1):
                        print(f"{i}. {jogo}")
                    excluir = int(input("Qual jogo deseja excluir?: "))
                    if 0 < excluir <= len(jogos):
                        jogos.pop(excluir - 1)
                        print("Jogo removido com sucesso!")
                    else:
                        print("Erro: Opção inválida.")
            elif opcao_jogo == 3:
                if not jogos:
                    print("Nenhum jogo no catálogo.")
                else:
                    print("Jogos no catálogo:")
                    for i, jogo in enumerate(jogos, 1):
                        print(f"{i}. {jogo}")
            elif opcao_jogo == 4:
                break
            else:
                print("Opção inválida.")
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")