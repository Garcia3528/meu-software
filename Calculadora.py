def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("=== CALCULADORA SIMPLES ===")
print("Operações disponíveis:")
print("1. Adição (+)")
print("2. Subtração (-)")

choice = input("Escolha uma operação (1/2): ")

if choice not in ['1', '2']:
    print("Opção inválida! Por favor, escolha 1 ou 2.")
else:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if choice == '1':
        print(f"Resultado da adição: {add(num1, num2)}")
    elif choice == '2':
        print(f"Resultado da subtração: {subtract(num1, num2)}")