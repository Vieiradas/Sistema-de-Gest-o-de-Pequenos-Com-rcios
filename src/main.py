from conexao import conectar


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("E-mail: ")
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
    cpf = input("CPF: ")
    telefone = input("Contato: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO clientes
        (nome, email, data_nascimento, cpf, telefone)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        sql,
        (nome, email, data_nascimento, cpf, telefone)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    print("\nCliente cadastrado com sucesso!")


def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes;")

    clientes = cursor.fetchall()

    for cliente in clientes:
        print(cliente)

    cursor.close()
    conexao.close()


def menu():
    while True:
        print("\n========================")
        print("       TECH & CIA")
        print("========================")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_clientes()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


menu()