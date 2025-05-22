cont = 0
soma_medias = 0

while cont < 5:
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    n3 = float(input("Digite a terceira nota do aluno: "))
    n4 = float(input("Digite a quarta nota do aluno: "))
               
    media = (n1 + n2 + n3 + n4) / 4
    soma_medias += media
    print("A média dos numeros é: ", media)
    
    if media >= 7:
        print("Aluno Aprovado! ")
    else:
        print("Aluno reprovado! ")
        
    cont = cont + 1
    media_total = soma_medias / cont
    
print(f"A média total é: {media_total:.2f}") 