class Banco:
    def __init__(self, numero, saldo, nome, tipo, status, limite):
        self.numero = numero
        self.saldo = 0.00
        self.nome = nome
        self.tipo = tipo
        self.status = True
        self.limite = 0.00

    def depositar(self, valor):
        if self.status == True:
            self.saldo += valor
            return (self.saldo)
        else:
            return('Ative a conta para depositar')

    def sacar(self, valor):
        if self.status == True:
            if self.saldo > valor:
                self.saldo -= valor
                return(self.saldo)
            else:
                return('Saldo insuficiente')
        else:
            return('Ative a conta pra sacar')

    def ativarconta(self, valorLimite):
        if self.status == True:
           self.limite = valorLimite
           return(f'A conta tem limite de R${self.limite:.2f}')
        else:
            return('É necessário ativar a conta.')

    def verificarsaldo(self):
        if self.status == True:
            return(f'O saldo é de R${self.saldo:.2f}')
        else:
           return('Ative a conta para verificar')