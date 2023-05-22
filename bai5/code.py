def check(s):
    a = 0
    for i in s:
        if i == " ":
            a += 1
    if a == 0:
        return True
    else:
        return False


s = str(input())
print(check(s))
