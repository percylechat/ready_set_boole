import sys


def reverse_map(n: float) -> (int, int):
    # check que int16 bits
    if n <= 0 or n > 1:
        print("error, invalid number")
        sys.exit(1)
    # exo precedent (x*y)/z=A i    # check que int16 bitsci inverse
    # donc z*A=x*y donc on fait num * equa
    # plusieurs results possibles pour x et y, le plus simple est que tjr 1*res
    # on peut aussi div par 2 et ajouter 1 si pair a un des chiffres?
    x = n * ((2**16 - 1) ** 2)
    return int(x), 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please enter 1 float")
        sys.exit(0)
    nbr1 = sys.argv[1]
    res, res1 = reverse_map(float(nbr1))
    print(res, res1)
