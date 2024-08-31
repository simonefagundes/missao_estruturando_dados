from pessoa import Pessoa
class PessoaJurica(Pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, status, dataAberturaEmpresa, cnpj):
        super().__init__(nome, numeroConta, dataAberturaConta, status)
        self.__dataAberturaEmpresa = dataAberturaEmpresa
        self.__cnpj = cnpj
    def imprimir(self):
        super().imprimir()
        print(self.dataAberturaEmpresa)
        print(self.cnpj)
    @property
    def dataAberturaEmpresa(self):
        return self.__dataAberturaEmpresa
    @dataAberturaEmpresa.setter
    def dataAberturaEmpresa(self, dataAberturaEmpresa):
        self.__dataAberturaEmpresa = dataAberturaEmpresa
    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self,cnpj):
        if len(cnpj)!=18:
            return ValueError
        else:
            self.__cnpj = cnpj