import math


class diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = diem(int(input('toa do x cua diem A: ')),
          int(input('toa do y cua diem A: ')))
p2 = diem(int(input('toa do x cua diem B: ')),
          int(input('toa do y cua diem B: ')))
p3 = diem(int(input('toa do x cua diem C: ')),
          int(input('toa do x cua diem C: ')))


def khoang_cach(p1, p2):
    distant = round(math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2), 2)
    return distant


def chu_vi(p1, p2, p3):
    chuvi = round(khoang_cach(p1, p2)+khoang_cach(p2, p3) +
                  khoang_cach(p3, p1), 2)
    return chuvi


def dien_tich(p1, p2, p3):
    nua_chuvi = chu_vi(p1, p2, p3) / 2
    dientich = round(math.sqrt(nua_chuvi * (nua_chuvi - khoang_cach(p1, p2)) *
                     (nua_chuvi - khoang_cach(p2, p3)) * (nua_chuvi - khoang_cach(p3, p1))), 2)
    return dientich


print("khoảng cách: ", khoang_cach(p1, p2))
print("chu vi: ", chu_vi(p1, p2, p3))
print("dientich: ", dien_tich(p1, p2, p3))
