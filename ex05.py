import sys


def get_list_values(data_structure):
    temp = ""
    for item in data_structure:
        if isinstance(item, list):
            temp += get_list_values(item)
        else:
            temp += item
    return temp


def negation_normal_form(str_: str) -> str:
    stn = standard_notation(str_)
    check = "".join(stn)
    temp_ = infix_to_nnf(check)
    return temp_


def apply_demorgans(node: list):
    # print(node)
    if node[0] == "!" and len(node[1]) > 1:
        if len(node[1]) > 2:
            if node[1][2] == "&":
                return [
                    apply_demorgans(["!", node[1][0]]),
                    apply_demorgans(["!", node[1][1]]),
                    "|",
                ]
            elif node[1][2] == "|":
                return [
                    apply_demorgans(["!", node[1][0]]),
                    apply_demorgans(["!", node[1][1]]),
                    "&",
                ]
        else:
            return node[1][0]
    elif node[0] == "!":
        return [node[1], node[0]]
    else:
        return node


def infix_to_nnf(tokens):
    # Applique De Morgan's Laws (doubleneg and stuff)
    # print(tokens)
    stack = []
    for token in tokens:
        if token != ")":  # Tant que avant ou dans parenthese
            stack.append(token)
        else:
            sub_expression = []
            while stack and stack[-1] != "(":
                sub_expression.append(stack.pop())
            stack.pop()  # enleve '('
            sub_expression.reverse()
            if "!" in sub_expression:
                if type(sub_expression[0]) is not list:
                    stack.append(sub_expression)
                else:
                    stack.append(apply_demorgans(["!", sub_expression[0]]))
            else:
                stack.append(sub_expression)
    nnf_expression = get_list_values(stack)
    return nnf_expression


def standard_notation(str_):
    # converts RPN into standard notation ie simplify and
    # puts parenthesis and ! before formula
    stack = []
    for elem in str_:
        if elem.isalpha():
            stack.append(elem)
        elif elem == "!":
            op1 = stack.pop()
            stack.append("(" + op1 + "!)")
        elif elem == "^":
            # XOR(a, b) = (a AND NOT b) OR (NOT a AND b)
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(
                "("
                + str(op1)
                + "("
                + str(op2)
                + "!)&)(("
                + str(op1)
                + "!)"
                + str(op2)
                + "&|)"
            )
        elif elem == ">":
            # (A ⇒ B) ⇔ (¬A ∨ B)
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append("((" + str(op1) + "!)" + str(op2) + "|)")
        elif elem == "=":
            # (A ⇔ B) ⇔ ((A ⇒ B) ∧ (B ⇒ A))
            # ((A ⇒ B) ∧ (B ⇒ A)) = ((¬A ∨ B) ∧ (¬B ∨ A))
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(
                "(("
                + str(op1)
                + "!)"
                + str(op2)
                + "|)(("
                + str(op2)
                + "!)"
                + str(op1)
                + "|&)"
            )
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append("(" + str(op1) + str(op2) + elem + ")")
    # print(stack)
    return stack

# (
#     (A!B|)&(B!)A|)!)
#      A!B& | b!a&

if __name__ == "__main__":
    #FROM SUBJECT
    print("input is AB&! expected is A!B!|")
    print(negation_normal_form("AB&!"))
    print("input is AB|! expected is A!B!&")
    print(negation_normal_form("AB|!"))
    print("input is AB> expected is A!B|")
    print(negation_normal_form("AB>"))
    print("input is AB= expected is AB&A!B!&|")
    print("not the same and its ok")
    print(negation_normal_form("AB="))
    print("input is AB|C&! expected is A!B!&C!|")
    print(negation_normal_form("AB|C&!"))
    #FROM else
    print("input is A expected is A")
    print(negation_normal_form("A"))
    print("input is A! expected is A!")
    print(negation_normal_form("A!"))
    print("input is AB|! expected is A!B!&")
    print(negation_normal_form("AB|!"))
    print("input is AB>! expected is AB!&")
    print(negation_normal_form("AB>!"))
    print("input is AB=! expected is flemme")
    print(negation_normal_form("AB=!"))

    # print("input is ABC|| expected is ABC||")
    # print(negation_normal_form("ABC||"))
    # print("input is ABC||! expected is ")
    # print(negation_normal_form("ABC||!"))
    # print("input is ABC&| expected is ")
    # print(negation_normal_form("ABC&|"))
    # print("input is ABC|& expected is ")
    # print(negation_normal_form("ABC|&"))
    # print("input is ABC&|! expected is ")
    # print(negation_normal_form("ABC&|!"))
    # print("input is ABC^^ expected is ")
    # print(negation_normal_form("ABC^^"))
    # print("input is ABC>> expected is ")
    # print(negation_normal_form("ABC>>"))
