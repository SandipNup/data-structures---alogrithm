import math
from functools import reduce

def find_prime_factor(n):
    n_prime_factor = []
    # if n is even
    while n % 2 == 0:
        n = n / 2
        n_prime_factor.append(2)
    
    # if n is odd
    for i in range(3,int(math.sqrt(n))+1, 2):
        while n % i == 0:
            n = n / i
            n_prime_factor.append(i)
    n_prime_factor.append(int(n))

    return n_prime_factor

def find_common_elements_between_two_list(list1, list2):
    common_elements = []
    for each_item in list1:
        if each_item in list2:
            common_elements.append(each_item)
            list2.remove(each_item)
    return common_elements

def gcd_prime_factorization(a, b):
    a_prime_factor = find_prime_factor(a)
    b_prime_factor = find_prime_factor(b)
    common_elements = find_common_elements_between_two_list(a_prime_factor, b_prime_factor)
    return reduce(lambda acc, value: acc*value, common_elements)


if __name__ == "__main__":
    print(gcd_prime_factorization(10, 5))
    print(gcd_prime_factorization(25, 50))
    print(gcd_prime_factorization(105, 60))