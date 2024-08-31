from pessoa import Pessoa
class PessoaFisica(Pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, status, dataNascimento, cpf, rg):
        super().__init__(nome,numeroConta, dataAberturaConta, status)
        self.__dataNascimento = dataNascimento
        self.__cpf = cpf
        self.__rg = rg
    def imprimir(self):
        super().imprimir()
        print(self.dataNascimento)
        print(self.cpf)
        print(self.rg)
    @property
    def dataNascimento(self):
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf)!=14:
            return ValueError("Formato inválido de cpf")
        else:
            self.__cpf=cpf

    @property
    def rg(self):
        return self.__rg
    @rg.setter
    def rg(self, rg):
        self.__rg = rg