acumulador = 0
contador = 0

while True:
    n = float(input("Digite um numero (se for negativo o programa irá parar!): "))
    
    if n < 0:
        break
    
    if n % 2 == 0:
        acumulador += n
        contador += 1
        
    if contador > 0:
        media = acumulador / contador
        print("a soma dos numeros pares é: ", acumulador)
        print("a media dos numeros pares é: ", media)
        
    else:
        print("Nenhum numero par foi digitado!")