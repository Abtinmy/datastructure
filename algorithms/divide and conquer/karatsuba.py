"""
    *** Time Complexity ***
    * T(n) = 3T(n/2) + n
    * theta(n ^ log2(3))
"""


def karatsuba(num1: str, num2: str) -> str:
    
    try:
        num1, num2 = int(num1), int(num2)
    except ValueError:
        print(f'{num1}, {num2} are not valid integers.')

    if len(str(num1)) == 1 or len(str(num2)) == 1:
        return num1 * num2

    power = int(max(len(str(num1)), len(str(num2))) / 2)
    divisor = int(pow(10, power))

    a, b, c, d = int(num1 / divisor), int(num1 % divisor), int(num2 / divisor), int(num2 % divisor)

    ac = int(karatsuba(str(a), str(c)))
    bd = int(karatsuba(str(b), str(d)))

    ad_bc = int(karatsuba(a + b, c + d)) - ac - bd
    
    return str(ac * (10 ** (2*power)) + ad_bc * (10 ** power) + bd)

