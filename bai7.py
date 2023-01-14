def main():
    soluong=int(input("nhap so luong nhan vien: "))
    nv=thong_tin(soluong,NhanVien)
    hien_thi(nv)
    sap_xep (nv)
    dia_chi=str(input("nhap dia chi tap tin"))
    ten_tap_tin=str(input("nhap ten tap tin"))
    luu_nhan_vien(dia_chi,ten_tap_tin,nv)
    noi_dung=doc_nhan_vien(dia_chi,ten_tap_tin)
    in list nhan vien(noi dung)
    print('ket thuc chuong trinh')
if__name__=='__main__':
     main()