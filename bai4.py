def__gt__(self,obj):
      return(self.tuoi>obj.tuoi)
def__ge__(self,obj):
      return(self.tuoi>=obj.tuoi)
def__It__(self,obj):
      return(self.tuoi--obj.tuoi)
def__le__(self,obj):
      return(self.tuoi<=obj.tuoi)
def__eq__(self,obj)
      return(self.tuoi==obj.tuoi)
def sap_xep(nv):
    sv=sorted(nv)
    print("sau sap xep thong tin gia tri tuoi")
    for item in sv:
        print(item)