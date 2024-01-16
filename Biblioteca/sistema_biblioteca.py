def retorna_menu():
    opcao_final = int(input("Digite o número da opção desejada:\n 1.Retornar ao menu principal\n 2.Sair\n"))
    if opcao_final == 1:
        main()
    elif opcao_final == 2:
        print("Obrigado por usar nosso sistema, volte sempre!")
    else:
        print("Opção inválida!")

lista_usuarios = []
def cadastrar_usuario():
    id_usuario = int(input("Digite o ID do usuário:\n"))
    nome = str(input("Digite o nome do usuário:\n"))
    idade = int(input("Digite a idade do usuário:\n"))
    endereco = str(input("Digite o endereço do usuário:\n"))

    usuarios = {"ID": id_usuario, "Nome": nome, "Idade": idade, "Endereço": endereco}
    lista_usuarios.append(usuarios)    

    print("Usuário cadastrado com sucesso!\n")
    retorna_menu()

def ver_usuarios_cadastrados():
    print("Lista de usuários cadastrados:\n")
    print(lista_usuarios)
    retorna_menu()

lista_livros = []
def cadastrar_livro():
    nome_livro = str(input("Digite o nome do livro que deseja cadastrar ou devolver:\n"))
    genero_livro = str(input("Digite o gênero do livro:\n"))

    livro = {"Nome": nome_livro, "Gênero":genero_livro}
    lista_livros.append(livro)
    print("Livro adicionado!")
    retorna_menu()

def verificar_disponibilidade():
    livro = str(input("Digite o nome do livro que deseja verificar:\n"))

    for livro in lista_livros:
        if livro in lista_livros:
            print("Livro disponível")
        else:
            print("Livro indisponível")
    retorna_menu()

def ver_lista():
    print("Essa é a lista de livros em nossa biblioteca:\n")
    print(lista_livros)
    retorna_menu()

emprestados = []
def retirar_livro():
    livro = str(input("Digite o nome do livro que deseja retirar:\n"))
    for livro in lista_livros:
        if livro in lista_livros:
            lista_livros.remove(livro)
        else:
            print("Livro indisponível")
    
    nome = str(input("Digite o seu nome:\n"))
    
    for nome in lista_usuarios:
        if nome in lista_usuarios:
            print(f"Feito, {nome}. Você pegou o livro {livro} emprestado!")
            print("Livro retirado!\n Devolva em 7 dias!\n")

            registro = {"Nome": nome, "Livro": livro}
            emprestados.append(registro)

        else:
            print("Usuário não cadastrado!")
    retorna_menu()

def ver_empretados():
    print("Essa é a lista de livros que estão emprestados:\n")
    print(emprestados)

    retorna_menu()

def devolucao():
    livro = str(input("Digite o nome do livro que deseja devolver:\n"))

    for livro in emprestados:
        if livro in emprestados:
            emprestados.remove(livro)
        else:
            print("Livro não encontrado na lista de empréstimos!")

    genero = str(input("Digite o gênero do livro:\n"))
    
    nome = str(input("Digite o seu nome:\n"))
    for nome in emprestados:
        if nome in emprestados:
            emprestados.remove(nome)
            print(f"Feito {nome}. O livro {livro} foi devolvido á nossa biblioteca!\n")
            print("Muito obrigado por utilizar nossa biblioteca!\n")
            
        else:
            print("Usuário não encontrado!")

    livro = {"Nome": livro, "Gênero":genero}
    lista_livros.append(livro)
    retorna_menu()

def main():
    print("Olá, seja muito bem-vindo ao sistema da Biblioteca do Bairro")
    opcao = int(input("Digite o número da opção que deseja escolher: \n 1.Cadastrar novo usuário.\n 2.Ver usuários cadastrados\n 3.Cadastrar livro.\n 4.Verificar disponibilidade\n 5.Ver lista de livros\n 6.Retirada de livros.\n 7.Ver livros emprestados\n 8.Devolução\n 9.Sair\n"))
    if opcao == 1:
        cadastrar_usuario()
    elif opcao == 2:
        ver_usuarios_cadastrados()    
    elif opcao == 3:
        cadastrar_livro()
    elif opcao == 4:
        verificar_disponibilidade()
    elif opcao == 5:
        ver_lista()
    elif opcao == 6:
        retirar_livro()
    elif opcao == 7:
        ver_empretados()
    elif opcao == 8:
        devolucao()
    elif opcao == 9:
        print("Obrigado por usar nosso sistema, volte sempre!")
    else:
        print("Opção inválida")

main()

    
