class NhanVien:
    def __init__(self,fullname,age,salary):
    self.hoten = fullname
    self.tuoi  = age
    self.luong = salary
    def __str__(self):
    message ='[hoten:'+self.hoten +';tuoi:'+ str(self.tuoi)+';luong:'+ str(self.luong)+']'
 return message


