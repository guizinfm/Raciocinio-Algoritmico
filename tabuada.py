for _ in range(2):
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    n3 = float(input("Digite a terceira nota do aluno: "))
    n4 = float(input("Digite a quarta nota do aluno: "))
    
    ma = (n1 + n2 + n3 + n4) / 4
    
    print(f"media anual = {ma:.2f}")