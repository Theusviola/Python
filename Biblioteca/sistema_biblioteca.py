def retorna_menu():
    opcao_final = int(input("Digite o número da opção desejada:\n 1.Retornar ao menu principal\n 2.Sair\n"))
    if opcao_final == 1:
        main()
    elif opcao_final == 2:
        print("Obrigado por usar nosso sistema, volte sempre!")
    else:
        print("Opção inválida!")

def cadastrar_usuario():
    lista_usuarios = []

    id_usuario = int(input("Digite o ID do usuário:\n"))
    nome = str(input("Digite o nome do usuário:\n"))
    idade = int(input("Digite a idade do usuário:\n"))
    endereco = str(input("Digite o endereço do usuário:\n"))

    usuarios = {"ID": id_usuario, "Nome": nome, "Idade": idade, "Endereço": endereco}
    lista_usuarios.append(usuarios)    

    print("Lista de pessoas cadastradas:\n")
    print(lista_usuarios)
    retorna_menu()

lista_livros = []
def cadastrar_livro():
    nome_livro = str(input("Digite o nome do livro que deseja cadastrar ou devolver:\n"))
    genero_livro = str(input("Digite o gênero do livro:\n"))

    livro = {"Nome": nome_livro, "Gênero":genero_livro}
    lista_livros.append(livro)

    print("Lista de livros atualizada:\n")
    print(lista_livros)
    retorna_menu()

def verificar_disponibilidade():
    livro = str(input("Digite o nome do livro que deseja verificar:\n"))

    if livro in lista_livros:
        print("Livro disponível")
    else:
        print("Livro indisponível")
    retorna_menu()

def ver_lista():
    print("Essa é a lista de livros em nossa biblioteca:\n")
    print(lista_livros)
    retorna_menu()

def retirar_livro():
    livro = str(input("Digite o nome do livro que deseja retirar:\n"))

    if livro in lista_livros:
        lista_livros.remove(livro)
        print("Livro retirado!\n Devolva em 7 dias!\n")
    else:
        print("Livro indisponível")

    retorna_menu()


def main():
    print("Olá, seja muito bem-vindo ao sistema da Biblioteca do Bairro")
    opcao = int(input("Digite o número da opção que deseja escolher: \n 1.Cadastrar novo usuário.\n 2.Cadastrar novo livro.\n 3.Verificar disponibilidade\n 4.Retirada de livros.\n 5.Devolução de livros\n 6.Sair\n"))
    if opcao == 1:
        cadastrar_usuario()
    elif opcao == 2:
        print("Cadastrar livro")
    elif opcao == 3:
        print("Verificar disponibilidade")
    elif opcao == 4:
        print("Retirar livros")
    elif opcao == 5:
        print("Devolução")
    elif opcao == 6:
        print("Sair")
    else:
        print("Opção inválida")

main()

    
