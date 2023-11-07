'''
Diego Silva Cavalcanti - RM 553351
Pela tabela a seguir, mostre a descrição e o preço do produto após a digitação do código pelo usuário. Se o produto não estiver cadastrado, emitir mensagem avisando. OBS: utilizar o Desvio Condicional de Múltipla Escolha.
'''

opcao = int(input("Digite uma opção de 1 a 4 : "))

match opcao:
    case 1:
        print("Caneta - R$1,20")
    case 2:
        print("Lápis - R$0,80")
    case 3:
        print("Borracha - R$1,00")
    case 4:
        print("Régua - R$1,50")
    case _:
        print("Utilizar o Desvio Condicional de Múltipla Escolha.")