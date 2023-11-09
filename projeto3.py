'''
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
        print(f"{n1} + {n2} = {soma}")
    case 2:
        sub = n1 - n2
        print(f"{n1} - {n2} = {sub}")
    case 3:
        mult = n1 * n2
        print(f"{n1} * {n2} = {mult}")
    case 4:
        div = n1 / n2
        print(f"{n1} / {n2} = {div:.2f}")
    case _:
        print("Opção inválida")