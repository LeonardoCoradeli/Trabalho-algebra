class R:
    def __init__(self, dimensao):
        self.dim = dimensao
        self.canonico = [[0] * i + [1] + [0] * (dimensao - 1 - i) for i in range(dimensao)]

class M:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.canonico = [[[1 if i == m and j == n else 0 for n in range(colunas)] for m in range(linhas)] for j in range(colunas) for i in range(linhas)]
        self.dim = linhas*colunas


class P:
    def __init__(self, grau):
        self.grau = grau
        self.canonico = [[0] * i + [1] + [0] * (grau - i) for i in range(grau + 1)]
        self.dim = grau+1

