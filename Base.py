import numpy as np
import LI
import Geradores

def e_base(vetores,espaço_vetorial):
    if isinstance(espaço_vetorial,list):
        return len(vetores) == len(espaço_vetorial) and LI.e_li(vetores)
    elif hasattr(espaço_vetorial,'canonico'):
        return len(vetores) == espaço_vetorial.dim and LI.e_li(vetores)
    else:
        return "Elemento invalido usado!"