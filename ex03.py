import sys


def eval_formula(str_: str) -> bool:
    """
    complexite spatiale (memoire allouée): dependant de la longueur de linpuyt
    """
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
    return bool(stack[0])


def eval_formula_debug(str_):
    stack = []
    for elem in str_:
        print("current stack is:", stack, "taking care of:", elem)
        if elem == "&":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 and op2
            print("result is:", result, "for", op1, elem, op2)
            stack.append(result)
        elif elem == "|":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 or op2
            print("result is:", result, "for", op1, elem, op2)
            stack.append(result)
        elif elem == "!":
            op1 = stack.pop()
            result = not op1
            stack.append(result)
        elif elem == "^":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 is not op2
            print("result is:", result, "for", op1, elem, op2)
            stack.append(result)
        elif elem == ">":
            op2 = stack.pop()
            op1 = stack.pop()
            if op1 is True and op2 is False:
                stack.append(False)
            else:
                stack.append(True)
        elif elem == "=":
            op2 = stack.pop()
            op1 = stack.pop()
            result = op1 is op2
            print("result is:", result, "for", op1, elem, op2)
            stack.append(result)
        elif elem == "0":
            stack.append(False)
        elif elem == "1":
            stack.append(True)
        else:
            print("Error, invalid formula")
            sys.exit(1)
    return bool(stack[0])


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Please enter 1 string and 'debug' or 'example' option")
        sys.exit(0)
    str_ = sys.argv[1]
    if len(sys.argv) == 3:
        if sys.argv[2] == "debug":
            print("Result is", eval_formula_debug(str_))
    elif sys.argv[1] == "example":
        print("input is 10& expected is false")
        print(eval_formula("10&"))
        print("input is 10| expected is true")
        print(eval_formula("10|"))
        print("input is 11> expected is true")
        print(eval_formula("11>"))
        print("input is 10= expected is false")
        print(eval_formula("10="))
        print("input is 1011||= expected is true")
        print(eval_formula("1011||="))
    else:
        print(eval_formula(str_))
