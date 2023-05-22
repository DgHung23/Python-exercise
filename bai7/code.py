def snt(test):
    if test < 2:
        return False
    else:
        for i in range(2, test//2+1):
            if test % i == 0:
                return False
        return True


def primes(n):
    a = []
    test = 2
    while len(a) < n:
        if snt(test):
            a.append(test)
        test += 1
    return a


n = int(input())
print(primes(n))
