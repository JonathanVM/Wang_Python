from itertools import *

def replace(iter, pos, formulas):
    yield from islice(iter, 0, pos)
    yield from formulas
    yield from islice(iter, pos+len(formulas)-1, None)
    
if __name__ == "__main__":
    m = [0,1,2,3,4,5]
    rep = [666, 777]
    print(m, rep, list(replace(m, 0, rep)))