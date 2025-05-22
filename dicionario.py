dic = {"joão": 100, "maria": 150}
print("Dic > joão:" + str(dic["joão"]) + "\n")
print("Dic > maria:" + str(dic["maria"]) + "\n")
dic["pedro"] = 10
print("Dic > pedro:" + str(dic["pedro"]) + "\n")





dic = {"Joao" : "a", "Maria" : "b"}
s = "%(Joao)s e %(Maria)s"
print(s%dic)

dic.clear()
print(dic)

dic = {"x":1, "Y":2}
dic_copia = dic.copy()
print("Dici original : " + str(dic))
print("Dici cópia : " + str(dic_copia))

dic_copia["z"] = 3
print("Dici cópia melhorado : " + str(dic_copia))

dic = {}.fromkeys([2,3])
print(dic)

dic = dict.fromkeys(["Joao", "Maria"], 0)
print(dic)

dic = {"Joao" : "a", "Maria" : "b"}
print(dic.get("Pedro"))
print(dic.get("Joao"))

dic = {"Joao" : "a", "Maria" : "b"}
print(dic.items())
print(dic.keys())
print(dic.values())

dic = {"Joao" : "a", "Maria" : "b"}
print(dic)
excluido = dic.pop("Joao")
print("O excluido foi: " + excluido)
print(str(dic))

dic.popitem()
print(str(dic))

dic1 = {"Joao" : "a", "Maria" : "b", "Pedro" : "c"}
print(dic1)

dic2 = {"Joao":1, "Pedro": 3}

dic1.update(dic2)
print(dic1)

meu_dicionario = {}

quantidade = int(input("Quantos pares chave-valor você quer adicionar? "))

for i in range (quantidade):
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    meu_dicionario[chave] = valor
    
print("Dicionario resultante: ", meu_dicionario)


agenda = {
    "Ana": "9999-8888",
    "Julio": "2222-3333",
    "Pedro": "1111-8888"
}

print(agenda["Ana"])

estoque = {
    "maça": 30,
    "banana": 45,
    "laranja": 20,
}
estoque["maça"] -= 5
print(estoque)