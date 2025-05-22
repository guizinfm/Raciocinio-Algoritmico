# exercicio 1

a = []

for i in range(10):
    num = int(input(f"Digite o {i+1} numero inteiro: "))
    a.append(num)
    
print("A lista de numeros digitada é: ", a)
  
# exercicio 2

for i in range(len(a)):
    print(f"Índice {i}: valor {a[i]}") 
    
# exercicio 3

maior = max(a)
menor = min(a)

print("Maior número:", maior)
print("Menor número:", menor)

# exercicio 4

quantidade = int(input("Digite a quantidade de alunos: "))
repetente = 0
aprovado = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1} (0 a 10.0): "))
    
    if nota < 6.0:
        repetente += 1
    elif nota == 6.0:
        aprovado += 1
        

print(f"\nQuantidade de alunos abaixo da média: {repetente}")
print(f"Quantidade de alunos na média: {aprovado}")

# exercicio 5

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1} número inteiro: "))
    numeros.append(num)

maior_par = None
menor_impar = None
soma = sum(numeros)
media = soma / len(numeros)

for num in numeros:
    if num % 2 == 0:
        if maior_par is None or num > maior_par:
            maior_par = num
    else:
        if menor_impar is None or num < menor_impar:
            menor_impar = num

print(f"\nSomatório dos elementos: {soma}")
print(f"Média dos elementos: {media:.2f}")

if maior_par is not None:
    print(f"Maior elemento par: {maior_par}")
else:
    print("Nenhum número par foi inserido.")

if menor_impar is not None:
    print(f"Menor elemento ímpar: {menor_impar}")
else:
    print("Nenhum número ímpar foi inserido.")
