class Usuario:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class ContaBancaria:
    LIMITE_SAQUES = 3

    def __init__(self, numero, usuario):
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Falha de operação! O valor informado é inválido.")

    def saque(self, valor, limite):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha de operação! Saldo insuficiente.")
        elif excedeu_limite:
            print("Falha de operação! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Falha de operação! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print(f"Saque realizado com sucesso! Saldo atual: R$ {self.saldo:.2f}")
        else:
            print("Falha de operação! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

class Banco:
    def __init__(self):
        self.usuarios = {}
        self.contas = {}
        self.limite_saque = 250

    def cadastrar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        if cpf in self.usuarios:
            print("Usuário já cadastrado!")
            return
        nome = input("Informe o nome: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuario = Usuario(cpf, nome, data_nascimento, endereco)
        self.usuarios[cpf] = usuario
        print("Usuário cadastrado com sucesso!")

    def cadastrar_conta(self):
        cpf = input("Informe o CPF do usuário para criar a conta: ")
        usuario = self.usuarios.get(cpf)
        if not usuario:
            print("Usuário não encontrado! Cadastre o usuário primeiro.")
            return

        numero_conta = len(self.contas) + 1
        conta = ContaBancaria(numero_conta, usuario)
        self.contas[numero_conta] = conta
        print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario.nome}!")

    def realizar_deposito(self):
        numero_conta = int(input("Informe o número da conta para depósito: "))
        conta = self.contas.get(numero_conta)
        if conta:
            valor = float(input("Informe o valor do depósito: "))
            conta.deposito(valor)
        else:
            print("Conta não encontrada.")

    def realizar_saque(self):
        numero_conta = int(input("Informe o número da conta para saque: "))
        conta = self.contas.get(numero_conta)
        if conta:
            valor = float(input("Informe o valor do saque: "))
            conta.saque(valor, self.limite_saque)
        else:
            print("Conta não encontrada.")

    def exibir_extrato(self):
        numero_conta = int(input("Informe o número da conta para exibir o extrato: "))
        conta = self.contas.get(numero_conta)
        if conta:
            conta.exibir_extrato()
        else:
            print("Conta não encontrada.")

    def exibir_menu(self):
        menu = """
        [nu] Novo Usuário
        [nc] Nova Conta
        [d] Depósito
        [s] Saque
        [e] Extrato
        [q] Sair

        => """
        return input(menu)

    def executar(self):
        while True:
            opcao = self.exibir_menu()

            if opcao == "nu":
                self.cadastrar_usuario()
            elif opcao == "nc":
                self.cadastrar_conta()
            elif opcao == "d":
                self.realizar_deposito()
            elif opcao == "s":
                self.realizar_saque()
            elif opcao == "e":
                self.exibir_extrato()
            elif opcao == "q":
                print("Saindo do sistema...")
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    banco = Banco()
    banco.executar()
