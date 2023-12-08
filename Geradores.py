import numpy as np


def gera_vetor(vetor, espaco_vetorial):
    # Verifica se o vetor é uma combinação linear dos vetores do espaço
    for v in espaco_vetorial.canonico:
        if v != vetor and not sao_combinacao_linear(vetor, espaco_vetorial.canonico):
            return False

    return True


def sao_combinacao_linear(vetor, lista_de_vetores):
    # Verifica se o vetor é uma combinação linear dos vetores da lista
    for v in lista_de_vetores:
        if not sao_proporcionais(vetor, v):
            return False
    return True


def sao_proporcionais(vetor1, vetor2):
    # Verifica se dois vetores são proporcionais
    if len(vetor1) != len(vetor2):
        return False

    # Caso especial para evitar divisão por zero
    for i in range(len(vetor1)):
        if vetor2[i] == 0 and vetor1[i] != 0:
            return False

    return all((vetor2[i] == 0 and vetor1[i] == 0) or (vetor2[i] != 0 and vetor1[i] / vetor2[i] == vetor1[0] / vetor2[0]) for i in range(len(vetor1)))
