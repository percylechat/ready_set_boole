import sys

# https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset


def count_different_letters(input):
    unique_letters = set()
    for char in reversed(input):
        if char.isalpha():
            unique_letters.add(char)
    return unique_letters


def powerset_gen(s):
    if not s:
        return [[]]
    element = s.pop()
    subsets = powerset_gen(s)
    new_subsets = [subset + [element] for subset in subsets]
    return subsets + new_subsets


def powerset(str_):
    set_ = powerset_gen(list(str_))
    # print(set_)
    res = set()
    for elem in set_:
        res.add(frozenset(elem))
    # print(res)
    return res


def eval_set(str_: str, set_: list[set]) -> set[frozenset]:
    variables = count_different_letters(str_)
    variables = list(variables)
    proper_letters = [*set(variables)]
    if len(proper_letters) != len(set_):
        print("fail", proper_letters, len(set_), set_)
        sys.exit(1)
    megaset = set()
    for elem in set_:
        megaset = megaset | elem
    # print(str(set_))
    # for elem in set_:
    #     S = ""
    #     for el in elem:
    #         # print(el)
    #         S += str(el)
    #     megaset = megaset | powerset(S)
    stack = []
    ref = dict(zip(proper_letters, set_))
    # print(ref)
    for elem in str_:
        # print(elem)
        if elem.isalpha():
            stack.append(ref[elem])
        elif elem == "!":
            op1 = stack.pop()
            print("op1", op1)
            print("mega", megaset)
            op2 = megaset - op1
            stack.append(op2)
        elif elem == ">":
            op2 = stack.pop()
            op1 = stack.pop()
            op3 = megaset - op1
            stack.append(op3 | op2)
        elif elem == "=":
            op2 = stack.pop()
            op1 = stack.pop()
            op3 = megaset - op1
            op4 = megaset - op2
            stack.append((op3 | op2) & (op1 | op4))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if elem == "|":
                stack.append(op1 | op2)
            else:
                stack.append(op1 & op2)
    return stack[0]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter 1 string and 'debug' option")
        sys.exit(0)
    str_ = sys.argv[1]
    set_ = sys.argv[2]
    if len(sys.argv) == 3:
        if sys.argv[2] == "debug":
            val1 = [set([0, 1, 2]), set([0, 4, 5])]
            print("input is AB& and ", val1, " expected is [0]")
            print(eval_set("AB&", val1))
            val2 = [set([0, 1, 2]), set([3, 4, 5])]
            print("input is AB| and ", val2, " expected is [0, 1, 2, 3, 4, 5]")
            print(eval_set("AB|", val2))
            val3 = [set([0, 1, 2])]
            print("input is A! and ", val3, " expected is [] / empty set")
            print(eval_set("A!", val3))
    else:
        eval_set(str_, set(set_))
