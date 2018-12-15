"""
coautores:
    Jonathan Vasquez Mora
    Delia Hernandez Ruiz
    Erick Hernandez Camacho
"""

from itertools import *

def replace(iter, pos, formulas):
    yield from islice(iter, 0, pos)
    yield from formulas
    yield from islice(iter, pos+1, None)
    
if __name__ == "__main__":
    m = [0,1,2,3,4,5]
    rep = [666]
    print(m, rep, list(replace(m, 2, rep)))