def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Operações disponíveis:")
print("1. Adição")
print("2. Subtração")

choice = input("Escolha uma operação (1/2): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if choice == '1':
    print(f"Resultado: {add(num1, num2)}")
elif choice == '2':
    print(f"Resultado: {subtract(num1, num2)}")
else:
    print("Opção inválida!")