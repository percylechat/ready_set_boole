from ex05 import negation_normal_form


def conjunctive_normal_form(str_: str) -> str:
    temp = negation_normal_form(str_)
    is_conj = temp.count("&")
    end = ""
    start = ""
    if temp[-1] == "|" and is_conj > 0:
        print("warning, this my be an invalid formula. Maybe it was simplified too much, maybe it was bad from the beginning")
    for elem in temp:
        if elem == "&":
            end += elem
        elif elem == "|" and is_conj == 0:
            end += elem
        else:
            start += elem
    res = start + end
    return res

if __name__ == "__main__":
    print("input is AB&! expected is A!B!|")
    print(conjunctive_normal_form("AB&!"))
    print("input is AB|! expected is A!B!&")
    print(conjunctive_normal_form("AB|!"))
    print("input is AB|C& expected is AB|C&")
    print(conjunctive_normal_form("AB|C&"))

    print("input is AB|C|D| expected is ABCD|||")
    print(conjunctive_normal_form("AB|C|D|"))
    print("input is AB&C&D& expected is ABCD&&&")
    print(conjunctive_normal_form("AB&C&D&"))
    print("input is AB|!C!& expected is A!B!C!&&")
    print(conjunctive_normal_form("AB|!C!&"))

        #FROM else
    print("input is A expected is A")
    print(conjunctive_normal_form("A"))
    print("input is A! expected is A!")
    print(conjunctive_normal_form("A!"))

    print("input is AB|! expected is A!B!&")
    print(conjunctive_normal_form("AB|!"))
    print("input is AB>! expected is AB!&")
    print(conjunctive_normal_form("AB>!"))
    print("input is AB=! expected is ")
    print(conjunctive_normal_form("AB=!"))