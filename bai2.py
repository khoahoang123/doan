from bai1 import NhanVien
import pickle
import os
def thong_tin(soluong,NhanVien):
    nv = []
    for i in range (soluong):
        hoten,tuoi,luong =input().split('.')
        nv.append(NhanVien(hoten,tuoi,luong))
    return nv


