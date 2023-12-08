import numpy as np


def numero_vetores_maior_que_elementos(conjunto_vetores):
    # Verificar se o conjunto de vetores não está vazio
    if not conjunto_vetores:
        return False

    # Número de vetores no conjunto
    num_vetores = len(conjunto_vetores)

    # Número de elementos no primeiro vetor
    num_elementos_referencia = len(conjunto_vetores[0])

    # Verificar se o número de vetores é maior que o número de elementos em cada vetor
    return num_vetores > num_elementos_referencia

def conjunto_vetores_para_matriz(vetores):
    if not vetores:
        raise ValueError("O conjunto de vetores está vazio.")

    tamanho_vetor = len(vetores[0])

    if any(len(vetor) != tamanho_vetor for vetor in vetores):
        raise ValueError("Os vetores no conjunto têm tamanhos diferentes.")

    # Criar a matriz
    matriz = np.array(vetores)

    return matriz.T


def resolver_sistema_linear(A):

    #B é composto por zeros
    B = np.zeros(A.shape[0])

    # Concatenar A e B para formar a matriz aumentada [A | B]
    matriz_aumentada = np.column_stack((A, B))

    # Aplicar a eliminação de Gauss
    linha, coluna = matriz_aumentada.shape
    for i in range(min(linha, coluna - 1)):
        # Pivoteamento parcial
        pivot_row = np.argmax(np.abs(matriz_aumentada[i:, i])) + i
        matriz_aumentada[[i, pivot_row]] = matriz_aumentada[[pivot_row, i]]

        # Eliminação
        for j in range(i + 1, linha):
            coeficiente = matriz_aumentada[j, i] / matriz_aumentada[i, i]
            matriz_aumentada[j, i:] -= coeficiente * matriz_aumentada[i, i:]

    # Aplicar a substituição regressiva
    x = np.zeros(coluna - 1)
    for i in range(linha - 1, -1, -1):
        x[i] = (matriz_aumentada[i, -1] - np.dot(matriz_aumentada[i, i:-1], x[i:])) / matriz_aumentada[i, i]

    return x


def e_li(vetores):
    if numero_vetores_maior_que_elementos(vetores):
        return False
    else:
        resultado = resolver_sistema_linear(conjunto_vetores_para_matriz(vetores))
        return np.all(resultado == 0)