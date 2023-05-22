with open("bai2\data_inp.txt", "r") as f:
    n = int(f.readline())
    hocsinh = []
    for i in range(n):
        a = f.readline().strip().split()
        ten = " ".join(a[:-1])
        diem = float(a[-1])
        hocsinh.append((ten, diem))

hocsinh.sort(key=lambda x: x[1], reverse=True)

with open("bai2\data_out.txt", "w") as f:
    for ten, diem in hocsinh:
        f.write(f"{ten} {diem}\n")
