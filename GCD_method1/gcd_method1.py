

def gcd_method1(a: int, b: int) -> int:
    """Gives the greatest common divisior of two numbers by method 1
    
    Args:
        a (int) : one integer out of two
        b (int) : another integer out two

    Returns:
        int : greatest common divisor that divides both integer
    """
    t = min(a, b)

    while ( a % t != 0 or b % t != 0):
        t = t - 1

    return t


if __name__ == '__main__':
    print(gcd_method1(10, 15))
    print(gcd_method1(60, 30))
    print(gcd_method1(105, 60))