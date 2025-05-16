dicionário = []
while True:
    print("=== DICIONÁRIO EM INGLÊS ===")
    print("1. Dicionar Palavra \n2. Buscar palavra \n3. Filtrar \n4. Sair")
    opcao = int(input("Escolha uma das opções acima: "))
    if opcao == 1:
        palavra = str(input("Adicione uma palavra: "))
        traducao = str(input("Escreva a Tradução: "))
        tipo = str(input("Digite o tipo da palavra: "))
        pri = str(input("digite a primeira letra da palavra: "))
        dicio = {"palavra": palavra, "Traduz": traducao, "tipo": tipo, "Letra": pri}
        dicionário.append(dicio)
    elif opcao == 2:
        Busca =str(input("Digite a palavra pra procurar: "))
        for dicio in dicionário:
            if Busca == dicio['palavra']:
                print(f"Palavra: {dicio['palavra']} | Tradução: {dicio['Traduz']} | Tipo: {dicio['tipo']}")
    elif opcao == 3:
        procura = int(input("Deseja filtrar por 1-letra ou 2-tipo: "))
        if procura == 1:
            letra = str(input("Digite a letra para filtrar: "))
            for dicio in dicionário:
                if dicio['Letra'] == letra:
                    print(f"Palavra: {dicio['palavra']} tradução: {dicio['Traduz']} tipo: {dicio['tipo']}")
        elif procura == 2:
            tipinho = str(input("Digite o tipo da palavra: "))
            for dicio in dicionário:
                if dicio['tipo'] == tipinho:
                    print(f"Palavra: {dicio['palavra']} tradução: {dicio['Traduz']} tipo: {dicio['tipo']}")
        else:
            print("rapaz nao existe!")
    elif opcao == 4:
        print("Saindo...") 
        break
    else:
        print("Opção inválida!")