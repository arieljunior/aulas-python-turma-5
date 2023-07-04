import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def testar_soma(self):
        valor_recebido = Calculadora.somar(5,5)
        self.assertEqual(valor_recebido, 10, "Erro na soma de valores")

    def testar_subtracao(self):
        valor_recebido = Calculadora.subtrair(5,5)
        self.assertEqual(valor_recebido, 0, "Erro na subtração de valores")

    def testar_multiplicacao(self):
        valor_recebido = Calculadora.multiplicar(5,5)
        self.assertEqual(valor_recebido, 25, "Erro na multiplicação de valores")

    def testar_divisao(self):
        valor_recebido = Calculadora.dividir(5,5)
        self.assertEqual(valor_recebido, 1, "Erro na divisão de valores")

if __name__ == "__main__":
    unittest.main()


