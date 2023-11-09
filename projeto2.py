'''
Baseado em um número real X (float) digitado pelo usuário, utilize o desvio condicional de múltipla escolha e faça as seguintes operações:

Opcao = 1: adicione 5 ao valor de X e exiba na tela.

Opcao = 2: subtraia 4 ao valor de X e exiba na tela.

Opcao = 3: dobre o valor de X e exiba na tela.

'''

n_real = float (input("Digite um número Real : "))

print("\n===============")
print("Opcao = 1: adicione 5 ao valor de X e exiba na tela.")
print("Opcao = 2: subtraia 4 ao valor de X e exiba na tela.")
print("Opcao = 3: dobre o valor de X e exiba na tela.")
print("===============")

opcao = int(input("\nAgora digite uma opção :  "))

match opcao:
    case 1:
        n_real = n_real + 5
        print(f"O valor é {n_real} ")
    case 2:
        n_real = n_real - 4
        print(f"O valor é {n_real}")
    case 3:
        n_real = n_real * 2
        print(f"O valor é {n_real}")
    case _:
        print("Opção inválida")