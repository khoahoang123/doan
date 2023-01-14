import random

def sinh_list(a,b):
    n = abs(int(input("nhap so phan tu cho list:")))
    c = [((b + 1 - a) * random.random()+a) for i in range(n)]
    for i in range(len(c)):
        c[i] = round(c[i], 1)
    print("a=", c)
    return c

def sap_xep(a):
    v = input("True hoac False:")
    if v == "True":
        print('sap xep theo chieu tang dan:')
        a = sorted(a, reverse=False)
    else:
        print('sap xep theo chieu giam dan:')
        a = sorted(a, reverse=True)
    print(a)
    return a

def tim(a):
    x = []
    n = float(input())
    for i in range(len(a)):
        if n == a[i]:
            x.append(i)
    if len(x) == 0:
        print("Không tìm thấy")
    else:
        print(x)
    return a


def luu(nguon:str,a):
    n = input()
    if n == "w":
        a = str(a)
        f=open(nguon, n)
        f.write(a)
        f.close()
    if n == "wb":
        a = bytearray(a)
        f = open(nguon, n)
        f.write(a)
        f.close()
    print('Đã lưu list')


from doan.phan1.bai1vabai2 import bai1vabai2,bai2,bai3,bai4

def main():
    nguon = input()
    a = float(input())
    b = float(input())
    v = bai1vabai2.sinh_list(a, b)
    bai4.luu(nguon, v)
    s = bai2.sap_xep(v)
    bai4.luu(nguon, s)
    bai3.tim(s)

if __name__ == '__main__':
    main()