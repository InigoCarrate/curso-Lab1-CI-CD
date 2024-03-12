def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error dividiendo entre 0"

if __name__ == "__main__":
    print(dividir(2, 0))