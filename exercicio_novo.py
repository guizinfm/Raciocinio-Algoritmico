# exercicio 1

# A)
con = 1
while con <= 10:
    print(con, "x 5 = ", con * 5)
    con = con + 1
    
    
# B)   
con = 1 

for numero in range(1,11):
    print(con, "x 5 = ", con * 5)
    con = con + 1
   
# exercicio 2
    
acumulador = 0
contador = 0
    
while True:
    n = float(input("Digite um numero (se for negativo o programa irá parar!): "))
    
    if n < 0:
        break 
    
    if n % 2 == 1:
        acumulador += n
        contador += 1
        
    if contador > 0:
        print("a soma dos numeros impraes é: ", acumulador)
        
    else:
        print("Nenhum numero impar foi digitado!")
        
# exercicio 3

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

for n1 in range(1,11):
    print(n1, "X", n2, "=", n1 * n2)