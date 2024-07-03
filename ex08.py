import sys

# https://docs.python.org/3.10/library/stdtypes.html#set-types-set-frozenset
# note: no vector in python !
# here we make do with sets and frozensets


def powerset_gen(s: list) -> list:
    if not s:
        return [[]]
    element = s.pop()
    subsets = powerset_gen(s)
    new_subsets = [subset + [element] for subset in subsets]
    return subsets + new_subsets


def powerset(set_: set) -> set:
    set__ = powerset_gen(list(set_))
    res = set()
    for elem in set__:
        res.add(frozenset(elem))
    return res


if __name__ == "__main__":
    ex: set = (1, 2, 3)
    print(powerset(ex))
