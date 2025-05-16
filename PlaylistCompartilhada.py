playlist = []
usuarios = []
while True:
    print("==== PLAYLIST COMPARTILHADA ===")
    print("\n1. Adicionar Musica \n2. Remover Música \n3. Exibir Playlist \n4. Trocar de Usuario \n5. Ver usuarios\n6. Sair")
    opcao = int(input("Escolha uma opção entre 1 a 6: "))
    primeiro_usuario = "Convidado"
    if opcao == 1:
        print("=== ADICIONAR MÚSICA ===")
        musica = input("Digite o nome da música: ")
        artista = input("Digite o nome do artista: ")
        playlist.append({"musica": musica, "artista": artista})
        if not usuarios:
            print(f"Música '{musica}' de '{artista}' adicionada à playlist por {primeiro_usuario}.")
        else:
            print(f"Música '{musica}' de '{artista}' adicionada à playlist por {usuarios}.")
    elif opcao == 2:
        print("=== REMOVER MÚSICA ===")
        if not playlist:
            print("Playlist vazia.")
        else:
            for i, musica in enumerate(playlist, 1):
                print(f"{i}. {musica}")
            excluir = int(input("Qual música deseja excluir?: "))
            if 0 < excluir <= len(playlist):
                playlist.pop(excluir - 1)
                print("Música removida com sucesso!")
            else:
                print("Erro: Opção inválida.")
    elif opcao == 3:
        print("=== EXIBIR PLAYLIST ===")
        if not playlist:
            print("Playlist vazia.")
        else:
            print("Playlist:")
            for i, musica in enumerate(playlist, 1):
                print(f"{i}. {musica['musica']} - {musica['artista']}") or print(f"Musicas: {playlist} adicionadas por {primeiro_usuario}.")
    elif opcao == 4:
        print("=== TROCAR DE USUÁRIO ===")
        usuario = input("Digite o nome do usuário: ")
        if usuario not in usuarios:
            usuarios.append(usuario)
            print(f"Usuário trocado para {usuario}.")
        else:
            print(f"Usuário '{usuario}' já está na lista.")
    elif opcao == 5:
        print("=== VER USUÁRIOS ===")
        if not usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("Usuários:", usuarios)
    elif opcao == 6:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
