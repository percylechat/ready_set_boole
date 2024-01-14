import sys
from itertools import product


def count_different_letters(input):
    unique_letters = set()
    i = 0
    for char in reversed(input):
        if char.isalpha():
            unique_letters.add(char)
            i += 1
    if len(input) == i and i != 1:
        print("Error, invalid string")
        sys.exit(1)
    return unique_letters


def sat(str_: str) -> bool:
    variables = count_different_letters(str_)
    variables = list(variables)
    proper_letters = [*set(variables)]
    all_combinations = list(product(["1", "0"], repeat=len(variables)))
    temp = str_
    for combination in all_combinations:
        vals = dict(zip(variables, combination))
        for val in vals:
            temp = temp.replace(val, vals.get(val))
        res_ = eval_formula(temp)
        if res_ == True:
            return True
        temp = str_
        # result.append(dict(zip(variables, combination)))
    # return result
    return False


def eval_formula(str_):
    stack = []
    for elem in str_:
        if elem == "&":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 and op2
            stack.append(result)
        elif elem == "|":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 or op2
            stack.append(result)
        elif elem == "!":
            op1 = stack.pop()
            result = not op1
            stack.append(result)
        elif elem == "^":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 is not op2
            stack.append(result)
        elif elem == ">":
            if op1 is True and op2 is False:
                stack.append(False)
            else:
                stack.append(True)
        elif elem == "=":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 is op2
            stack.append(result)
        elif elem == "0":
            stack.append(False)
        elif elem == "1":
            stack.append(True)
        elif not elem.isalpha():
            print("Error, invalid formula")
            sys.exit(1)
    return stack[0]


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Please enter 1 string or example")
        sys.exit(0)
    str_ = sys.argv[1]
    if str_ == "example":
        print("input is AB| expected is true")
        print(sat("AB|"))
        print("input is AB& expected is true")
        print(sat("AB&"))
        print("input is AA!& expected is false")
        print(sat("AA!&"))
        print("input is AA^ expected is false")
        print(sat("AA^"))
    else:
        print(sat(str_))
