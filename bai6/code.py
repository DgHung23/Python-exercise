def deletele(s, k, n):
    for i in range(k, k+n, 1):
        s.pop(k)
    return s


s = list(input("nhap chuoi "))
k = int(input("nhap vị tri "))
n = int(input("nhap so luong "))
print(deletele(s, k, n))
