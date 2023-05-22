with open("bai1\data_inp.txt", "r") as f:
    data = f.readline().split()
    data2 = f.readline().split()
sum = 0
sum2 = 0
tb = 0
tb2 = 0
cout1 = 0
cout2 = 0
for i in data:
    sum += int(i)
    cout1 += 1
for i in data2:
    sum2 += int(i)
    cout2 += 1
tb = round(sum/cout1, 2)
tb2 = round(sum2/cout2, 2)


with open("bai1\data_out.txt", "w") as f:
    f.write(str(sum))
    f.write(" ")
    f.write(str(tb))
    f.write("\n")
    f.write(str(sum2))
    f.write(" ")
    f.write(str(tb2))
