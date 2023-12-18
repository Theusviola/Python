

def cadastrar_usuario():
    pessoa = {}

    id_usuario = int(input("Digite o ID do usuário:\n"))
    nome = str(input("Digite o nome do usuário:\n"))
    idade = int(input("Digite a idade do usuário:\n"))
    endereco = str(input("Digite o endereço do usuário:\n"))

    pessoa['id_usuario'] = id_usuario
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['endereco'] = endereco

    print("Lista de pessoas cadastradas:\n")
    print(pessoa)
    opcao_final = int(input("Digite o número da opção desejada:\n 1.Retornar ao menu principal\n 2.Sair"))
    if opcao_final == 1:
        main()
    elif opcao_final == 2:
        print("Obrigado por usar nosso sistema, volte sempre!")
    else:
        print("Opção inválida!")

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

    
