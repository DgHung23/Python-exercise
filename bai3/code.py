def nhiphan(n):
    s = ""
    temp = 0
    while n > 0:
        temp = n % 2
        s = s+str(temp)
        n = n//2
    return len(s)


n = int(input())
print(nhiphan(n))
