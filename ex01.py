import sys


def multiplier(a: int, b: int) -> int:
    """compelxite temporelle (temps que prend l algo): depend de b ou a mais un seul des 2 donc n1
    complexite spatiale (memoire allouée): pareil 3 variables sans dependance a b donc o1
    """
    result = 0
    while b > 0:
        if b & 1:  # Check if the least significant bit of b is 1
            result = adder(
                result, a
            )  # Calls the add_numbers function from the previous example
        a = a << 1  # Left-shift a by 1 (equivalent to multiplying a by 2)
        b = b >> 1  # Right-shift b by 1 (equivalent to dividing b by 2)
    return result


def multiplier_debug(a, b):
    print("First value")
    bit_vizualizer(a)
    print("second value")
    bit_vizualizer(b)
    result = 0
    while b > 0:
        if b & 1:  # Check if the least significant bit of b is 1
            result = adder(
                result, a
            )  # Calls the add_numbers function from the previous example
            print(result)
            bit_vizualizer(result)
        a = a << 1  # Left-shift a by 1 (equivalent to multiplying a by 2)
        b = b >> 1  # Right-shift b by 1 (equivalent to dividing b by 2)
        print(a)
        bit_vizualizer(a)
        print(b)
        bit_vizualizer(b)
    bit_vizualizer(result)
    return result


def adder(a, b):
    while b != 0:
        temp = a & b
        a = a ^ b
        b = temp << 1
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
            print("Result is", multiplier_debug(one, two))
    else:
        print("Result is", multiplier(one, two))
