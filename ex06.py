import sys


def get_list_values(data_structure, temp=[]):
    for item in data_structure:
        if type(item) == list:
            temp = get_list_values(item, temp)

        else:
            temp.append(item)

    return temp


def checkformula(str_: str):
    checker = set(["|", "!", "&"])
    for elem in str_:
        if not (elem.isalpha() or elem in checker):
            print("wrong formula")
            sys.exit(1)


def quickfixnoconj(un):
    temp = un.count("|")
    un = un.replace("|", "")
    return un + ("|" * temp)


def applyNegation(str_, conj):
    stack = []
    temp = ""
    adder = 0
    if len(str_) == 3:
        stack.append([str_[0] + "!" + str_[1] + "!"])
        adder += 1
    elif len(str_) == 2:
        stack.append([str_[0] + "!" + str_[1] + "!" + "|"])
        adder += -1
    else:
        stack.append([str_ + "!"])
    return stack[0], adder


def conjunctive_normal_form(str_: str) -> str:
    stack = []
    checkformula(str_)
    toadd = 0
    for c in str_:
        if c.isalpha():
            stack.append(c)
        elif c == "!":
            temp = stack.pop()
            res, adder = applyNegation(temp, toadd)
            stack.append(res)
            toadd += adder
        elif c == "|":
            temp = stack.pop()
            temp2 = stack.pop()
            stack.append(temp2 + temp + c)
        elif c == "&":
            temp = stack.pop()
            temp2 = stack.pop()
            stack.append(temp2 + temp)
            toadd += 1
        else:
            print("error")
    # print("end:", stack[0])
    un = "".join(get_list_values(stack))
    if toadd <= 0:
        str_ = quickfixnoconj(un)
    else:
        str_ = un + ("&" * toadd)

    return str_
    # print(str_)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Please enter 1 string or debug beware with exclamation point")
        sys.exit(0)
    str_ = sys.argv[1]
    if str_ == "debug":
        print("input is AB&! expected is A!B!|")
        print(conjunctive_normal_form("AB&!"))
        # print("input is AB|! expected is A!B!&")
        # print(conjunctive_normal_form("AB|!"))
        # print("input is AB|C& expected is AB|C&")
        # print(conjunctive_normal_form("AB|C&"))

        # print("input is AB|C|D| expected is ABCD|||")
        # print(conjunctive_normal_form("AB|C|D|"))
        # print("ask for a fun fact")
        # print("input is AB&C&D& expected is ABCD&&&")
        # print(conjunctive_normal_form("AB&C&D&"))
        # print("input is AB|!C!& expected is A!B!C!&&")
        # print(conjunctive_normal_form("AB|!C!&"))
    else:
        conjunctive_normal_form(str_)
