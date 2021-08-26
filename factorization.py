
import math

def factorize(n):
        prime = []
        while n % 2 == 0:
            prime.append(n),
            n = n / 2

        for i in range(3,int(math.sqrt(n))+1,2):
            while (n % i == 0):
                prime.append(i)
                n = n / i
        if n > 2:
            prime.append(n)
        return prime


def test_factorize():
    assert factorize(412415) == [5, 82483]
    assert factorize(27) == [3,3,3]
    assert factorize(31) == [31]

test_factorize()
