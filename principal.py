#Importar modulo forma padrão
import calculadora 

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
        opcao_valida = possiveis_opcoes.inex(opcao) > -1
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
            resultado = calculadora.somar(numero1, numero2)
        elif opcao == '2':
            resultado = calculadora.subtrair(numero1, numero2)
        elif opcao == '3':
            resultado = calculadora.multiplicar(numero1, numero2)
        elif opcao == '4':
            resultado = calculadora.dividir(numero1, numero2)
        
        print(f"Resultado: {resultado}")
