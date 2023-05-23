class Tprime:
    def __init__(self, n):
        self.n = n
        self.primes = self.generate_prime_numbers(n)
        
    def __getitem__(self, k):
        return self.primes[k]
        
    def generate_prime_numbers(self, n):
        primes = []
        temp = 0
        num = 2
        
        while temp < n:
            if self.snt(num):
                primes.append(num)
                temp += 1
            num += 1
        
        return primes
        
    def snt(self, num):
        if num < 2:
            return False
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        
        return True



pnum = Tprime(int(input("nhap n:")))

for i in range(pnum.n):
    print("Số nguyên tố thứ", i + 1, "là:", pnum[i])





