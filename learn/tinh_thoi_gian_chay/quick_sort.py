# ---------------------QUICKSORT-------------------------

'''
Bài toán phân đoạn:
cho trước một dãy A
cần thực hiện phép toán gán để phân tách dãy A thành 2 phần được phân chia tại P (quickSort)
sao cho mọi i <= ,A[i] <= A[p] = pivot
mọi j >p, A[j] >pivot

-------------------------------|-----------------------------------
      (nhỏ hơn chốt)         Chốt         (lớn hơn chốt)
ss


gợi ý: pivot = A[o]
(left)----------------------(chốt)----------------------(right)

partision(a, left, right)
partision(A, 0, len(A)-1)

'''

from random import randint
from time import perf_counter


def partision(a, left, right):
    pivot = a[left]
    p = left
    i = p
    for j in range(left+1, right+1):
        if a[j] <= pivot:
            i += 1
            # thay a[i] và a[j]
            a[i], a[j] = a[j], a[i]

    a[p], a[i] = a[i], a[p]
    return i


def QuickSort(a, left, right):
    if left < right:
        p = partision(a, left, right)
        QuickSort(a, left, p-1)
        QuickSort(a, p+1, right)
    return


a = [3, 1, 9, 7, 8, 4, 6, 2, 0, 10]
QuickSort(a, 0, len(a)-1)
print(a)


# =============tính thời gian chạy của QuickSort==============
def CreateArray(n):
    a = []
    for i in range(n):
        a.append(randint(1, n//2))
    return a


n = int(input("nhập số phần tử của a để tính thời gian chạy của thuật toán: "))
a = CreateArray(n)
t1 = perf_counter()
QuickSort(a, 0, len(a)-1)
t2 = perf_counter()
print("thời gian chạy là: ", round(t2-t1, 8), "s")

# ========================Hàm tính lũy thừa=====================


def exp(a, n):
    if n == 0:
        return 1
    else:
        x = exp(a, n//2)
        if n % 2 == 0:
            return x*x
        else:
            return x*x*a


a = int(input("nhập số: "))
n = int(input("mũ: "))


def lt(a,n):
    lt=1
    for i in range(1,n):
        lt=lt*i
    return lt

t1 = perf_counter()
exp(a,n)
t2 = perf_counter()
print("thời gian chạy exp là: ", round(t2-t1, 8), "s")

t1 = perf_counter()
lt(a,n)
t2 = perf_counter()
print("thời gian chạy lt là: ", round(t2-t1, 8), "s")
