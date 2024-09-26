def divisao(a, b):
    return a / b
def main():
    try:
        a = int(input("Qual o valor de A? "))
        b = int(input("Qual o valor de B? "))
        resultado = divisao(a, b)   
        print(f"A divisão é {resultado}")
    except ZeroDivisionError:
        print("Não é possivel dividir por zero!")
    except ValueError:
        print("Não é um valor inteiro")
    except Exception as e:
        return e
main()