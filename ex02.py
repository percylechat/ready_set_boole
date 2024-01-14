import sys

# https://fr.wikipedia.org/wiki/Code_de_Gray


def gray_code(one: int) -> int:
    if one == 0:  # special case, since 0 is empty, no need to convertt anything
        return one
    bin_ = bit_converter(one)  # convert int to str bit equivalent
    res = "1"  # tjr 1 car nombre ops, mais si 0 inclu on check avant et on enverrait 0 ou pas
    i = 1
    while i < len(bin_):  # si indice et indice -1 pareil 0 else 1
        if bin_[i] != bin_[i - 1]:
            res = res + "1"
        else:
            res = res + "0"
        i += 1
    final_res = num_converter(res)
    return final_res


def gray_code_debug(one):
    if one == 0:  # special case, since 0 is empty, no need to convertt anything
        return one
    bin_ = bit_converter(one)  # convert int to str bit equivalent
    print(bin_)
    res = "1"  # tjr 1 car nombre ops, mais si 0 inclu on check avant et on enverrait 0 ou pas
    i = 1
    while i < len(bin_):  # si indice et indice -1 pareil 0 else 1
        if bin_[i] != bin_[i - 1]:
            res = res + "1"
        else:
            res = res + "0"
        i += 1
    print(res)
    final_res = num_converter(res)
    return final_res


def num_converter(str_):
    newres = "".join(reversed(str_))  # on retourne pour commencer par le pls petit
    main = 1
    i = 0
    res = 0
    while i < len(newres):
        if newres[i] == "1":
            res += main
        main *= 2
        i += 1
    return res


def bit_converter(num) -> str:
    res = ""
    while num > 0:
        res = str(num % 2) + res
        num = num // 2
    return res


def bit_converter_full(num):
    res = ""
    while num > 0:
        res = str(num % 2) + res
        num = num // 2
    while len(res) % 8 != 0:
        res = "0" + res
    return res


def bit_vizualizer(num):
    if num > 256:
        print("Number too big to be explained")
        return
    res = "¦"
    main = 128
    while num != 0 or main >= 1:
        if num / main >= 1:
            num = num - main
            res += "1¦"
        else:
            res += "0¦"
        main = main // 2
    print(res)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Please enter 1 natural number and 'debug' or just 'full' option")
        sys.exit(0)
    try:
        one = int(sys.argv[1])
    except ValueError or AssertionError:
        print("Wrong input")
        sys.exit(0)
    if one < 0:
        print("Wrong input")
        sys.exit(0)
    if len(sys.argv) == 3:
        if sys.argv[2] == "debug":
            print("Result is", gray_code_debug(one))
        elif sys.argv[2] == "full":
            print("input 0, expected is 0")
            print("Result is", gray_code(0))
            print("input 1, expected is 1")
            print("Result is", gray_code(1))
            print("input 2, expected is 3")
            print("Result is", gray_code(2))
            print("input 3, expected is 2")
            print("Result is", gray_code(3))
            print("input 4, expected is 6")
            print("Result is", gray_code(4))
            print("input 5, expected is 7")
            print("Result is", gray_code(5))
            print("input 6, expected is 5")
            print("Result is", gray_code(6))
            print("input 7, expected is 4")
            print("Result is", gray_code(7))
            print("input 8, expected is 12")
            print("Result is", gray_code(8))
    else:
        print("Result is", gray_code(one))
