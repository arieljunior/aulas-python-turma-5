#Importar modulo forma padrão
from calculadora import Calculadora 

#Importar modulo por função
# from calculadora import somar, subtrair, multiplicar, dividir, nome_modulo

#Importar modulo trocando o nome
# import calculadora as funcoes
possiveis_opcoes = ["1", "2", "3", "4", "5"]
opcao = ""
while opcao != "5":
    print("1 - somar\n2 - subtrair\n3 - multiplicar\n4 - dividir\n5 - sair")
    opcao = input("Digite uma opção: ")
    
    try:
        opcao_valida = possiveis_opcoes.index(opcao) > -1
    except ValueError:
        print("Opção inválida")
        opcao_valida = False
    except:
        print("Erro inesperado")
        opcao_valida = False

    if opcao_valida == True and opcao != "5":
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

        resultado = 0
        if opcao == '1':
            resultado = Calculadora.somar(numero1, numero2)
        elif opcao == '2':
            resultado = Calculadora.subtrair(numero1, numero2)
        elif opcao == '3':
            resultado = Calculadora.multiplicar(numero1, numero2)
        elif opcao == '4':
            resultado = Calculadora.dividir(numero1, numero2)
        
        print(f"Resultado: {resultado}")

#nova linha