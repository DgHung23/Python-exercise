def so_sanh(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()


    alphabet = ["a", "ă", "â", "b", "c", "d", "đ", "e", "ê", "g", "h", "i", "k", "l", "m", "n", "o", "ô", "ơ", "p", "q", "r", "s", "t", "u", "ư", "v", "x", "y"]

    index_s1 = alphabet.index(s1)
    index_s2 = alphabet.index(s2)

    if index_s1 < index_s2:
        return (s1,"dung truoc",s2)
    elif index_s1 > index_s2:
        return (s2,"dung truoc",s1)
    else:
        return (s1,"= ",s2)


s1=str(input("s1: "))
s2=str(input("s2: "))
print(so_sanh(s1, s2))