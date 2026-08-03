def calcular(a, b, operacao):
    resultado = None

    if operacao == "soma":
        resultado = a + b
    elif operacao == "subtracao":
        resultado = a - b
    elif operacao == "multiplicacao":
        resultado = a * b
    elif operacao == "divisao":
        if b != 0:
            resultado = a / b
        else:
            print("Erro")
    else:
        print("Operação inválida")

    return resultado


def main():
    print(calcular(10, 5, "soma"))
    print(calcular(10, 0, "divisao"))


if __name__ == "__main__":
    main()
