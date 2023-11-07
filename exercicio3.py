'''
Diego Silva Cavalcanti - RM 553351
Crie um menu com as 4 operações matemáticas (soma, subtração, multiplicação e divisão) que devem ser executadas com 2 números reais (float) de acordo com a escolha (opção) do usuário:
'''

n1 = float(input("Digite o primeiro número real : "))
n2 = float(input("Digite o segundo número real : "))

print("======================")
print("[1]... Adição")
print("[2]... Subtração")
print("[3]... Multiplicação")
print("[4]... Divisão")
print("======================")

opcao = int(input("Digite a opção desejada (1 a 4) : "))

match opcao:
    case 1:
        soma = n1 + n2
        print(f"A soma dos 2 números é {soma}")
    case 2:
        sub = n1 - n2
        print(f"A subtração dos 2 números é {sub}")
    case 3:
        mult = n1 * n2
        print(f"A multiplicação dos 2 números é {mult}")
    case 4:
        div = n1 / n2
        print(f"A divisão dos 2 números é {div:.2f}")
    case _:
        print("Opção inválida")