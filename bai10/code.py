def so_sanh(s1):
    s1 = s1.lower()

    alphabet = ["a", "ă", "â", "b", "c", "d", "đ", "e", "ê", "g", "h", "i", "k",
                "l", "m", "n", "o", "ô", "ơ", "p", "q", "r", "s", "t", "u", "ư", "v", "x", "y"]

    return alphabet.index(s1)

s1 = str(input("s1: "))
s2 = str(input("s2: "))

temp1 = 0
temp2 = 0

if len(s1) >= len(s2):
    for i in range(0, len(s1)):
        temp1 += so_sanh(s1[i])
        temp2 += so_sanh(s2[i])
else:
    for i in range(0, len(s2)):
        temp1 += so_sanh(s1[i])
        temp2 += so_sanh(s2[i])

        
if temp1 > temp2:
    print("s1 lon hon s2")
elif temp1 < temp2:
    print("s1 nho hon s2")
else:
    print("s1 = s2")

