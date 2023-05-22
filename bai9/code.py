class Tprime:

    def __init__(self,n):
        self.n = n

pnum = Tprime(int(input("nhap n:")))


def snt(test):
    if test < 2:
        return False
    else:
        for i in range(2, test//2+1):
            if test % i == 0:
                return False
        return True


