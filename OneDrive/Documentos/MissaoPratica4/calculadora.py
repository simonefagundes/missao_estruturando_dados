class Calculadora():
    def __init__(self, valorA, valorB, operacao):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao
    @property
    def valorA(self):
        return self.__valorA
    @valorA.setter
    def valorA(self,valorA):
        self.__valorA = valorA
    @property
    def valorB(self):
        return self.__valorB
    @valorB.setter
    def valorB(self,valorB):
        self.__valorB = valorB
    @property
    def operacao(self):
        return self.__operacao
    @operacao.setter
    def operacao(self,operacao):
        self.__operacao=operacao
    def validarOperacao(self,operacao):
        operadores = ['+', '-', 'x', '%']
        if operacao in operadores:
            return True
        else:
            return False
    def calcular(self):
        if self.validarOperacao(self.operacao) == False:
            print("A operação selecionada é inválida")
            return
        elif self.operacao == '+':
            resultado = self.valorA + self.valorB
        elif self.operacao == '-':
            resultado = self.valorA - self.valorB
        elif self.operacao == 'x':
            resultado = self.valorA * self.valorB
        elif self.operacao == '%':
            if self.valorA == 0 or self.valorB == 0:
                print('A divisão não pode ser realizada com o número 0')
                return
            else:
                resultado = self.valorA/self.valorB
        return str(resultado)
    def mostrarResultado(self):
            print(str(self.valorA) + ' ' + self.operacao + ' ' + str(self.valorB) + ' = ' + str(self.calcular()))
    