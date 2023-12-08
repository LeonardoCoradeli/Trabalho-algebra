import numpy as np

def dimensao_base(vetores):
    matriz = np.array(vetores)
    dimensao = np.linalg.matrix_rank(matriz)
    return dimensao

