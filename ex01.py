import sys


def multiplier(a: int, b: int) -> int:
    """compelxite temporelle (temps que prend l algo): depend de b ou a mais un seul des 2 donc n1
    complexite spatiale (memoire allouée): pareil 3 variables sans dependance a b donc o1
    """
    try:
        a = int(a)
        b = int(b)
    except ValueError or AssertionError:
        print("Wrong input")
        sys.exit(0)
    if a < 0 or b < 0:
        print("Non natural number")
        sys.exit(0)
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
    try:
        a = int(a)
        b = int(b)
    except ValueError or AssertionError:
        print("Wrong input")
        sys.exit(0)
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
    print(
        "warning, i am lazy so the debug won't work for numbers beyond 256. Code still works!"
    )
    print("tested: 0, 0, expected 0")
    print(multiplier(0, 0))
    print("tested: 1, 0, expected 1")
    print(multiplier(1, 0))
    print("tested: 0, 1, expected 1")
    print(multiplier(0, 1))
    print("tested: 4, 20, expected 80")
    print(multiplier(4, 20))
    print("tested: 100, 25, expected 2500")
    print(multiplier(100, 25))
