# exercicio 1

n = int(input("Digite um numero: "))
resultado = n % 2
if resultado == 0 :
    print("O resultado é par")
else:
    print("O resultado é impar")
    
# exercicio 2

n = int(input("Digite um numero: "))
if n > 0 :
    print("O resultado é positivo")
elif n < 0:
    print("O numero é negativo")
else:
    print("O resultado é zero")

# exercicio 3

letra = input("Digite uma letra: ")
if len(letra) != 1 or not letra.isalpha():
    print("Digite apenas uma letra: ")
    
if letra in "a" or "e" or "i" or "o" or "u":
    print(f"A letra '{letra}' é uma vogal" )
else: 
    print(f"A letra '{letra}' é uma consoante")
    

# exercicio 4
a = float(input("Digite o número do primeiro lado do triangulo: "))
b = float(input("Digite o número do segundo lado do triangulo: "))
c = float(input("Digite o número do terceiro triangulo: "))

if a == b == c:
    print("o triangulo é equilatero")
elif a != b != c:
    print("o triangulo é escaleno")
else:
    print("o triangulo é isoceles")
    
# Exercicio 5

salario = float(input("Digite seu salario: "))
anos = int(input("Digite o seu tempo de trabalho: "))
salario_2 = float(salario * (1.05))
if anos > 5:
    print("O seu salario terá um bonus de 5%! agora é : ", salario_2)
elif anos == 5:
    print("Você possui 5 anos de experiencia e por isso não irá receber a bonificação: ")
else: 
    print("Você não tem a quantidade de tempo para uma bonificação! ")
    
# exercicio 6

valor_da_compra = float(input("Digite o valor da sua compra: "))
valor_desconto = (valor_da_compra * 0.10)
valor_final = valor_da_compra - valor_desconto

if valor_da_compra > 100:
    print("Você terá um desconto de 10%! portanto o valor da sua compra é de: ", valor_final )
elif valor_da_compra == 100:
    print("Sua compra não terá desconto: ")
else:
    print("Sua compra não terá desconto: ")
    
# exercicio 7

idade = int(input("Qual a sua idade?: "))

if idade <= 12:
    print("Você é criança! ")
elif idade <= 17:
    print("Você é adolecente! ")
elif idade <= 59:
    print("Você é adulto! ")
else:
    print("Você é idoso! ")
    
# exercicio 8

nota_prova = float(input("Qual foi a sua nota? "))

if nota_prova >= 9:
    print("Você tirou um A! ")
elif nota_prova >= 7:
    print("Você tirou um B! ")
elif nota_prova >= 5:
    print("Você tirou um C! ")
else: 
    print("Você tirou um D! ")
    
# exercicio 9

salario_anual = float(input("Qual é o seu salário anual? "))

if salario_anual <= 20000:
    print("A sua alíquota é de 0%! ")
elif salario_anual <= 50000:
    print("A sua alíquota é de 15%! ")
else:
    print("A sua alíquota é de 25%! ")
    
#exercicio 10

idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você é maior de idade e pode tirar a CNH! ")
else:
    print("Você é menor de idade, por isso não pode tirar a CNH! ")
    
# exercicio 11

temperatura = float(input("Qual é a temperatura? "))
temperatura_fahrenheit = ((temperatura * 9/5) + 32)

print(f"a {temperatura:.2f} está em celsius, convertida em fahrenheit é {temperatura_fahrenheit:.2f} ")

#exercicio 12

peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura em cm? "))
imc = (peso / altura)

if imc < 18:
    print("Você está abaixo do peso! ")
elif imc < 25:
    print("Você é normal! ")
elif imc < 30:
    print("Você está acima do peso! ")
else:
    print("Você é obeso! ")
    
# exercicio 13

n = int(input("Digite um numero de 1 a 10: "))
for count in range(10):
    print("%d x %d = %d" % (n, count + 1, n * (count+1)) )