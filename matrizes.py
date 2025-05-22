import numpy as np

notas = np.array([
    [85, 92, 78],
    [70, 88, 91],
    [62, 75, 88]
])

medias_alunos = np.mean(notas, axis=1)
print("Média pr aluno: ", medias_alunos)

medias_avaliações = np.mean(notas, axis=0)
print("Média por avaliação: ", medias_avaliações)
