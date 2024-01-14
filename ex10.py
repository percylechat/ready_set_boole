import sys


def map_(x: int, y: int) -> float:
    # check que int16 bits
    if x > 65535 or x <= 0 or y > 65535 or y <= 0:
        print("error, invalid number")
        sys.exit(1)
    result = (x * y) / ((2**16 - 1) ** 2)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please enter 2 numbers")
        sys.exit(0)
    nbr1 = sys.argv[1]
    nbr2 = sys.argv[2]
    res = map_(int(nbr1), int(nbr2))
    print(res)
    print(f"{res:.20f}")
