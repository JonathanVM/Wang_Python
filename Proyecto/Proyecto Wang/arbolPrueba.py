from deduction import *
from proof import *

class DeductionTree:
    def __init__(self, root):
        self.root = root
        self.tree = []

    def pipe(init, *iterables):

        return reduce(lambda a, n: n(a), iterables, init)


    buildTree = pipe(
        AXIOM_RULE(actual),
        AND_LEFT_RULE,
        OR_RIGHT_RULE,
        opener,
        lines,
        clean_newline,
        filter_not_empty,
    )
    buildTree = lambda actual: (init(actual),)