try:
    numero = int(input("Digite um numero: "))
    print(f"O numero é: {numero}")
except ValueError:
    print("Não é um numero inteiro")