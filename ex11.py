import sys


def reverse_map(n: float) -> (int, int):
    # check que int16 bits
    if n <= 0 or n > 1:
        print("error, invalid number")
        sys.exit(1)
    temp = n * (( 65535 + 1) ** 2)
    y = temp % (65535 + 1)
    x = (temp - y) / (65535 + 1)
    return int(x), int(y)


if __name__ == "__main__":
    res, res1 = reverse_map(0.0019073595758527517)
    print(res, res1)
