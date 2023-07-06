nome_modulo = "Funções para calcular"

class Calculadora:
    @staticmethod
    def somar(numero1: int | float, numero2: int | float) -> int | float:
        return numero1 + numero2
    
    @staticmethod
    def subtrair(numero1: int | float, numero2: int | float) -> int | float:
        return numero1 - numero2
    
    @staticmethod
    def dividir(numero1: int | float, numero2: int | float) -> int | float:
        return numero1 / numero2
    
    @staticmethod
    def multiplicar(numero1: int | float, numero2: int | float) -> int | float:
        return numero1 * numero2