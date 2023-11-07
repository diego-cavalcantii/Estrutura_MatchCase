'''
Diego Silva Cavalcanti - RM 553351
Baseado em um número real X (float) digitado pelo usuário, utilize o desvio condicional de múltipla escolha e faça as seguintes operações:
'''

n_real = float (input("Digite um número Real : "))

opcao = int(input("Agora digite uma opção :  "))

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