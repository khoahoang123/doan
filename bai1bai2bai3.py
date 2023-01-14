import numpy as np

def tinh():
    print("Bai 1:")
    N = abs(int(input("nhap so phan tu cua vector x:")))
    x = np.random.uniform(-10, 10, N).reshape(N,1)
    print("x=",x)
    m = abs(int(input("Nhap so hang cho ma tran A:")))
    n = abs(int(input("Nhap so cot cho ma tran A:")))
    while N != n:
        n = abs(int(input("So cot cua A phai bang so phan tu cua x:")))
    else:
        A = np.random.uniform(-10,10,m*n).reshape(m,n)
        print("A=",A)
        tich = np.dot(A,x)
        tich = print("A.x=",tich)
    return tich

import numpy as np

def tinh2():
    print("Bai 2:")
    m = abs(int(input("Nhap so hang cho ma tran A, B:")))
    n = abs(int(input("Nhap so cot cho ma tran A, B:")))
    A = np.random.uniform(-10, 10, m*n).reshape(m, n)
    print("A=", A)
    B = np.random.uniform(-10, 10, m*n).reshape(m, n)
    print("B=", B)
    print("Phep nhan Hadamard:")
    h = np.multiply(A, B)
    h = print("AoB=", h)
    print("Phep nhan hai ma tran:")
    C = A.copy()
    C = C.T
    tich = np.dot(C, B)
    tich = print("A*B", tich)
    return h, tich


from doan.phan2.cau1.bai1bai2bai3 import *
from doan.phan2.cau1.bai2 import *

def main():
    tinh()
    tinh2()
if __name__=='__main__':
    main()