"""
CHIA ĐỂ TRỊ?        SẮP XẾP TRỘN?       ÁP DỤNG CHIA_ĐỂ_TRỊ vào sắp xếp trộn?
"""

''' 
kh phải thuật toán => phương pháp 

gồm 3 bước sau:
1. chia
2. trị 
3. kết hợp


bài toán lớn chia thành nhìu bài toán con
=================tổng quát================== 
bài toán P 
-> chia nhỏ thành: p1(n/3), p2(n/3), p3(n/3)   (chia)
=> giải p1, p2, p3                             (trị)
=> kết hợp lại giải bài toán P                 (kết hợp)
* Công thức tính thời gian chạy của chia để trị: T(n)=bT(n/a)+f(n)
'''


'''
ví dụ: bài toán tìm kiếm nhị phân
cho dãy A sắp xếp tăng dần, hệ số K
tìm chỉ số i, A[i]=k, nếu không thấy thì trả về -1
'''
# ===================Đệ Quy====================


def BinacySearch(a, left, right, K):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == K:
            return mid
        elif a[mid] < K:
            return BinacySearch(a, mid + 1, right, K)
        else:
            return BinacySearch(a, left, mid-1, K)


'''
ví dụ: sắp xếp trộn (MerseSort)
cho 2 dãy B,C đã được sắp xếp tăng dần
trộn 2 dãy B,C tạo thành dãy A sap cho A sắp xếp tăng dần
'''
# b = [1, 3, 7, 10]
# c = [2, 4, 5, 6]


def Merse(b, c):
    m = len(b)
    n = len(c)
    a = [0]*(m+n)
    i = j = k = 0
    while i < m and j < n:
        if b[i] < c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    if i == m:         # i ra ngoài mảng khỏi B, phải chuyển phần còn lại của C vào A
        while j < n:
            a[k] = c[j]
            j += 1
            k += 1
    else:   # i       # j=n       j ra ngoài C, chuyển phần còn lại của B vào A
        a[k] = b[i]
        i += 1
        k += 1
    return a
# print(Merse(b, c))
"""===từ chương trình trên, sử dụng CHIA_ĐỂ_TRỊ để xây dựng hàm sắp xếp==="""


def MergeSort(a):
    if len(a) <= 1:
        return a
    else:
        k = len(a)//2    # (chia)
        b = MergeSort(a[: k])  # (trị)
        c = MergeSort(a[k:])
        return Merse(b, c)  # (kết hợp)


a = [2, 1, 8, 4, 6, -7, 4, 3, 6, 10]
print ("merge sort: ")
print(MergeSort(a))


"""
vd: Tìm tổng con lớn nhất
cho trước dãy A gồm các số nguyên
tổng con: S(i,j) = A[i] + A[i+1] + ... + A[j]
tìm dãy con liên tục có tổng con maximum

Hướng giải:
==================1==============|================2================
                                mid

phân loại các dãy con liên túc trong A (chia)
3 loại: 
+ nằm gọn trong B (1)
+ nằm gọn trong C (2)
+ không nằm gọn trong B,C (dãy con chứa phần tử mid)
"""

n=str(input("PRESS ANY KEY TO CONTINUE: "))
minINF = float("-inf")      # min infinities(nhỏ nhất)    

def MaxCrossArray(a, left, mid, right):

    # ------------bên trái------------
    sumL = a[mid]  # Sum left
    start = mid
    currsum = 0  # con trỏ (current)
    for i in range(mid, left-1, -1):
        currsum += a[i]
        if currsum > sumL:
            sumL = currsum
            start = i

# ------------bên phải------------
    sumR = a[mid+1]
    end = mid+1
    currsum = 0  # con trỏ (current)
    for i in range(mid+1, right+1):
        currsum += a[i]
        if currsum > sumR:
            sumR = currsum
            end = i

    return sumL + sumR, start, end


def MaxSubArray(a, left, right):
    if left > right:
        return minINF,None,None  #rỗng
    elif left == right:
        return a[left],left,left
    else: 
        mid= (left+right)//2
        sumL,startL,endL =MaxSubArray(a,left,mid)          # left
        sumR,startR,endR =MaxSubArray(a,mid+1,right)       # right
        sumX,startX,endX =MaxCrossArray(a,left,mid,right)  # mid
        if sumL >= sumR and sumR >= sumX:
            return sumL, startL, endL
        elif sumR >= sumL and sumR >= sumX:
            return sumR, startR, endR
        else:
            return sumX, startX, endX


a=[1,2,-3,0,-7,3,6,10,-5,-1,3,9,5,-3]
sum, start, end= MaxSubArray(a,0,len(a)-1)
print ("dãy con có tổng max là: ", sum)
if sum > minINF:
    for i in range(start, end+1):
        print (a[i], end=" ")
else:
        print("dãy rỗng")