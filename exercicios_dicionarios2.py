# exercicio 1

def cadastrar_alunos():
    alunos = {}
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i} do aluno (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida! Deve estar entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida! Por favor, insira um número.")
        alunos[nome] = notas
    return alunos

def listar_alunos_aprovados(alunos):
    print("\nAlunos com média ≥ 7:")
    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        if media >= 7:
            print(nome)

def buscar_aluno(alunos):
    nome = input("\nDigite o nome do aluno que deseja buscar: ")
    if nome in alunos:
        notas = alunos[nome]
        media = sum(notas) / len(notas)
        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"
        print(f"Nome: {nome}, Média: {media:.2f}, Situação: {situacao}")
    else:
        print("Aluno não encontrado.")

def main():
    alunos = cadastrar_alunos()
    listar_alunos_aprovados(alunos)
    buscar_aluno(alunos)

if __name__ == "__main__":
    main()


# exercicio 2

def cadastrar_produtos():
    produtos = {}
    while True:
        nome = input("Digite o nome do produto (ou 'sair' para encerrar o cadastro): ").strip()
        if nome.lower() == 'sair':
            break
        while True:
            try:
                quantidade = int(input(f"Digite a quantidade em estoque para {nome}: "))
                if quantidade < 0:
                    print("Quantidade não pode ser negativa. Tente novamente.")
                else:
                    produtos[nome] = quantidade
                    break
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")
    return produtos

def consultar_produto(produtos):
    nome = input("Digite o nome do produto para consultar a quantidade em estoque: ").strip()
    quantidade = produtos.get(nome)
    if quantidade is not None:
        print(f"Quantidade em estoque de {nome}: {quantidade}")
    else:
        print("Produto não encontrado.")

def realizar_compra(produtos):
    nome = input("Digite o nome do produto: ").strip()
    if nome not in produtos:
        print("Produto não encontrado.")
        return
    while True:
            quantidade_compra = int(input(f"Digite a quantidade de {nome}: "))
            if quantidade_compra <= 0:
                print("Quantidade deve ser maior que zero.")
            elif quantidade_compra > produtos[nome]:
                print(f"Quantidade insuficiente em estoque. Disponível: {produtos[nome]}")
            else:
                produtos[nome] -= quantidade_compra
                print(f"Compra realizada com sucesso! Estoque atualizado: {produtos[nome]}")
                break
            
def main():
    print("=== Cadastro de Produtos ===")
    produtos = cadastrar_produtos()
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Consultar quantidade em estoque")
        print("2 - Realizar uma compra")
        print("3 - Sair")
        opcao = input("Opção: ").strip()
        if opcao == '1':
            consultar_produto(produtos)
        elif opcao == '2':
            realizar_compra(produtos)
        elif opcao == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()

# exercicio 3

def contar_frequencia(frase):
    frase = frase.lower().replace(" ", "")
    frequencia = {}
    for letra in frase:
        if letra.isalpha():
            frequencia[letra] = frequencia.get(letra, 0) + 1
    return frequencia

def main():
    frase = input("Digite uma frase: ")
    frequencia_letras = contar_frequencia(frase)
    print("Contagem das letras:")
    print(frequencia_letras)
    
if __name__ == "__main__":
    main()

# exercicio 4

def cadastrar_votos():
    votos = {}
    while True:
        nome = input("Digite o nome do candidato: ").strip()
        if nome in votos:
            votos[nome] += 1
        else:
            votos[nome] = 1
        print(f"Voto computado para {nome}.")
    return votos

def exibir_resultados(votos):
    if not votos:
        print("Nenhum voto registrado.")
        return
    print("\nResultados da votação:")
    for candidato, quantidade in votos.items():
        print(f"{candidato}: {quantidade} voto(s)")

def main():
    print("Sistema de Votação")
    votos = cadastrar_votos()
    exibir_resultados(votos)
    
if __name__ == "__main__":
    main()
        
