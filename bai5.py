def luu_nhan_vien(dia_chi:str,ten_tap_tin: str)->list[NhanVien]
    try:
        with open(os.path.join(dia_chi,ten_tap_tin),'wb')as f:
             pickle.dump(objs,f)
        print("ket thuc ghi tap tin")
    except Exception as e:
    print("loi ghi tap tin")
