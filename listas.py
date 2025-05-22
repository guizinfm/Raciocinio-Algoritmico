nome_alunos = []
alunos = 0

for i in range(alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nome_alunos.append(nome)
    
print("\nNome dos alunos da turma: ")
for nome in nome_alunos:
    print(nome)
    
