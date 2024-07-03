import sys


def map_(x: int, y: int) -> float:
    # check que int16 bits
    if x > 65535 or x <= 0 or y > 65535 or y <= 0:
        print("error, invalid number")
        sys.exit(1)
    #on cree un chiffre avec tous les bits de x a gauche, on accole les birts de y et on divise pour avoir un float
    total_values = ( 65535 + 1) ** 2
    unique_value = (x * ( 65535 + 1)) + y

    return unique_value / total_values


if __name__ == "__main__":
    res = map_(int(125), int(47))
    print(res)
