
#Objeto
class Conta:

    #Função construtora
    def __init__(self, numero, titular, saldo, limite):
        print('Construindo Objeto...{}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Verifica o valor da conta.
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    #Deposita um valor na conta
    def deposita(self, valor):
        self.__saldo += valor

    #Retira um valor na conta
    def saca(self, valor):
        self.__saldo -= valor

    #Transfere o valor de uma conta para a outra.
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def mostra_saldo(self):
        return self.__saldo