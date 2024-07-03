import sys
from itertools import product


# Wrong output order because of set
def count_different_letters(input):
    unique_letters = set()
    for char in input:
        if char.isalpha():
            unique_letters.add(char)
    return unique_letters


def print_truth_table(str_: str) -> str:
    """compelxite temporelle (temps que prend l algo): taille de l input au carre (boucle sur les possibilites plus reboucle sur l input)"""
    res = ""
    variables = count_different_letters(str_)
    variables = list(variables)
    proper_letters = [*set(variables)]
    for l in variables:
        res += "| "
        res += l
        res += " "
    res += "| = |\n"
    lo = len(variables) + 1
    bloc = "|---" * lo
    res += bloc
    res += "|\n"
    temp = str_
    all_combinations = list(product(["1", "0"], repeat=len(variables)))
    # creates list of all possible comb for abc
    for combination in all_combinations:
        vals = dict(zip(variables, combination))
        # one value for each letter
        for val in vals:
            temp = temp.replace(val, vals.get(val))
            res = res + "| " + vals.get(val) + " "
            # creates true false formula then send to previous ex
        res_ = eval_formula(temp)
        if res_ == True:
            res = res + "| 1 |\n"
        else:
            res = res + "| 0 |\n"
        temp = str_
    return res


def eval_formula(str_):
    stack = []
    for elem in str_:
        if elem == "&":
            if len(stack) < 2:
                print("Error, invalid formula")
                sys.exit(1)
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 and op2
            stack.append(result)
        elif elem == "|":
            if len(stack) < 2:
                print("Error, invalid formula")
                sys.exit(1)
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 or op2
            stack.append(result)
        elif elem == "!":
            if len(stack) < 1:
                print("Error, invalid formula")
                sys.exit(1)
            op1 = stack.pop()
            result = not op1
            stack.append(result)
        elif elem == "^":
            if len(stack) < 2:
                print("Error, invalid formula")
                sys.exit(1)
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 is not op2
            stack.append(result)
        elif elem == ">":
            if len(stack) < 2:
                print("Error, invalid formula")
                sys.exit(1)
            op2 = stack.pop()
            op1 = stack.pop()
            if op1 is True and op2 is False:
                stack.append(False)
            else:
                stack.append(True)
        elif elem == "=":
            if len(stack) < 2:
                print("Error, invalid formula")
                sys.exit(1)
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 is op2
            stack.append(result)
        elif elem == "0":
            stack.append(False)
        elif elem == "1":
            stack.append(True)
        else:
            print("Error, invalid formula")
            sys.exit(1)
    if len(stack) > 1:
        print("Error, invalid formula")
        sys.exit(1)
    return stack[0]


if __name__ == "__main__":
    print("input is AB&")
    print(print_truth_table("AB&"))
    print("input is AB|")
    print(print_truth_table("AB|"))
    print("input is AB&C|")
    print(print_truth_table("AB&C|"))
