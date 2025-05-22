while True:
    nota = float(input("Digite uma nota de zero a dez: "))
    if nota >= 0 and nota <= 10:
        print("Nota válida.")
        break
    else:
        print("Nota inválida. Por favor, digite uma nota de 0 a dez.")