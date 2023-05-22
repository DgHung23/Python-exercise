def scount(s, sub):
    temp = 0
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)] == sub:
            temp += 1
    return temp


s = str(input())
sub = str(input())
print(scount(s, sub))
