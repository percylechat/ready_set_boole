import sys


def adder(a: int, b: int) -> int:
    """compelxite temporelle (temps que prend l algo): depend de b donc n1
    complexite spatiale (memoire allouée): pareil 3 variables sans dependance a b donc o1
    """
    while b != 0:
        temp = a & b  # Temp prend la valeur des bits de A ET B ensemble
        a = a ^ b  # A ne prend que les bits de A ou B ou l'un est Vrai
        b = temp << 1  # Les bits de B sont decales vers la droite (augmentation)
    return a


def adder_debug(a: int, b: int) -> int:
    print("First value")
    bit_vizualizer(a)
    print("second value")
    bit_vizualizer(b)
    while b != 0:
        temp = a & b  # Temp prend la valeur des bits de A ET B ensemble
        a = a ^ b  # A ne prend que les bits de A ou B ou l'un est Vrai
        b = temp << 1  # Les bits de B sont decales vers la droite (augmentation)
        print("First we take first AND second values bits")
        bit_vizualizer(temp)
        print("Then first XOR second value bits")
        bit_vizualizer(a)
        print("Last we right shift bits from second value")
        bit_vizualizer(b)
    print("final result is")
    bit_vizualizer(a)
    return a


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
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Please enter 2 natural numbers and 'debug' option")
        sys.exit(0)
    try:
        one = int(sys.argv[1])
        two = int(sys.argv[2])
    except ValueError or AssertionError:
        print("Wrong input")
        sys.exit(0)
    if one <= 0 or two <= 0:
        print("Wrong input")
        sys.exit(0)
    if len(sys.argv) == 4:
        if sys.argv[3] == "debug":
            print(
                "warning, i am lazy so the debug won't work for numbers beyond 256. Code still works!"
            )
            print("Result is", adder_debug(one, two))
    else:
        print("Result is", adder(one, two))
