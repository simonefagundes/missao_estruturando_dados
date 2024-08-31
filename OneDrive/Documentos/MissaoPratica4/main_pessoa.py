from pessoa import Pessoa
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJurica
pessoa1 = Pessoa("Ana", "101010", "26-06-1999", False)
pessoa1.imprimir()
pessoa2 = PessoaFisica("Ana", "101010", "26-06-1999", False,"2000-01-01", "000.111.222-33", "15975388-1")
pessoa2.imprimir()
pessoa3 = PessoaJurica("Ana", "101010", "26-06-1999", False,"2019-01-01", "00.000.000/0001-00")
pessoa3.imprimir()
