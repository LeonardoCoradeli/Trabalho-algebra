import numpy as np


def todos_os_vetores_mesmo_tamanho(vetores):
    # Verificar se o conjunto de vetores não está vazio
    if not vetores:
        return False

    # Tamanho do primeiro vetor
    tamanho_referencia = len(vetores[0])

    # Verificar se todos os vetores têm o mesmo tamanho
    for vetor in vetores[1:]:
        if len(vetor) != tamanho_referencia:
            return False

    return True


def mesmo_numero_vetores_e_elementos(conjunto_vetores):
    # Verificar se o conjunto de vetores não está vazio
    if not conjunto_vetores:
        return False

    # Número de vetores no conjunto
    num_vetores = len(conjunto_vetores)

    # Número de elementos no primeiro vetor
    num_elementos_referencia = len(conjunto_vetores[0])

    # Verificar se o número de vetores é igual ao número de elementos em cada vetor
    return (all(len(vetor) == num_elementos_referencia for vetor in conjunto_vetores) and
            len(conjunto_vetores) == num_elementos_referencia)

def e_li(vetores):
    if not todos_os_vetores_mesmo_tamanho(vetores):
        return False
    else:

