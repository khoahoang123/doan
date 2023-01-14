def luu_nhan_vien(dia_chi:str,ten_tap_tin: str)->list[NhanVien]
    try:
        with open(os.path.join(dia_chi, ten_tap_tin), 'rb')as f:
              sv = pickle.load(f)
        return sv
    except Exception as e:
        return None
def in list nhan_vien(s:list[NhanVien]):
   print("no dung trong tap tin")
   for i in s:
       print(i)