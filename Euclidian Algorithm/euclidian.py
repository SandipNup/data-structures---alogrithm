def euclidian_gcd(a: int, b:int) -> int:
    """Gives the greatest common divisior of two integers using euclidan algorithm.

    Args:
        a (int) : One integer out of two
        b (int) : Another integer out of two

    Returns:
        int : greatest common integer that divides both the integer

    """
    m = max(a,b)
    n = min(a,b)

    while n !=0:
        r = m % n
        m = n
        n = r
    return m

if __name__ == '__main__':
    print(euclidian_gcd(60, 15))
    print(euclidian_gcd(15, 0))
    print(euclidian_gcd(10, 11))
    print(euclidian_gcd(225, 60))