import textwrap


def menu():
    menu = '''\n
    ==========Menu==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [nu]\tNovo Usuario
    [lc]\tListar Contas
    [q]\tSair
    ==>'''
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor  # adiciona o valor do deposito ao saldo
        # adiciona a informação do deposito ao extrato
        extrato += f"Deposito:\tR$ {valor :.2f}\n"
        # Exibe uma mensagem confirmando o deposito
        print("\n=== Deposito efetuado com com sucesso ===")
    else:
        '''Caso o valor não é valido
        exibe a mensgem informando o usuario => retorna ao menu'''
        print("\n!!! Somente valores positivos são permitidos para\
 deposito !!!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_saques):
    if valor > saldo:
        print("!!! Você não possui saldo suficiente !!!")
    elif valor > limite:
        print("!!! Limite do saque ecedido !!!")
    elif numero_de_saques >= limite_saques:
        print("!!! Limite de saques diarios atingido !!!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_de_saques += 1
        print("\n=== Saque realizado com sucesso ===")
    else:
        print("!!! Operação falhou, valor informado Invalido !!!")

    return saldo, extrato, numero_de_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== Extrato ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo:\t\tR$ {saldo:.2f}")
    print("=============================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("!!! Usuario já cadastrado !!!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço\
 (logradouro, nº - bairro - cidade/uf): ")

    usuarios.append(
        {"cpf": cpf, "nome": nome, "Data_nascimento": data_nascimento,
         "endereco": endereco})
    print("=== Usuario cadastrado com sucesso ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_da_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso ===")
        return {"agencia": agencia, "numero_conta": numero_da_conta,
                "usuario": usuario}
    print("!!! Usuario não encontrado, criaçã de conta encerrada. !!!")


def listar_contas(contas):
    for conta in contas:
        linha = f'''
            Agencia:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Tutular\t{conta['usuario']['nome']}
        '''
        print("=" * 30)
        print(textwrap.dedent(linha))


def main():
    # Constantes
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    # Variaveis
    saldo = 0
    limite = 500
    extrato = ""
    numeor_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":

            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numeor_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_de_saques=numeor_saques,
                limite_saques=LIMITE_SAQUES

            )

        elif opcao == "e":

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nc":

            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "nu":

            criar_usuario(usuarios)

        elif opcao == "lc":

            listar_contas(contas)

        elif opcao == "q":
            exit()
        else:
            print("Opção selecionada invalida")


main()
