from sympy import *

def giai_hpt():
    print("Giai he phuong trinh:")
    x,y,z=symbols("x,y,z")
    pt1=Eq(2*x-5*y+z,-5)
    pt2=Eq(4*x+2*y-2*z,2)
    pt3=Eq(x+y-z,0)
    kq=solve((pt1,pt2,pt3),(x,y,z))
    kq=print(kq)
    return kq

from sympy import *

def giai_lim():
    print("Giai limit:")
    x=symbols("x")
    f=((x**3-3*x**2)**(1/3))+(x**2-2*x)**(1/2)
    kq=limit(f,x,oo)
    kq=print(kq)
    return kq

from sympy import *

def giai_dh():
    print("Giai dao ham:")
    x=symbols("x")
    f=(2*x-1)/(x+2)
    kq=diff(f,x)
    kq=print(kq)
    return kq

from sympy import *

def giai_nh():
    print("Giai nguyen ham:")
    x=symbols("x")
    f=x/(x**2-1)
    kq=integrate(f,x)
    kq=print(kq)
    return

from sympy import *

def giai_tp():
    print("Giai tich phan:")
    x=symbols('x')
    f=((1-x*tan(x))/(x**2-cos(x)+x))
    kq=integrate(f,(x,(2*pi)/3,pi))
    print(kq)

from doan.phan2.cau2 import bai1bai2bai3bai4bai5bai6,bai2,bai3,bai4,bai5

def main():
    bai1bai2bai3bai4bai5bai6.giai_hpt()
    bai2.giai_lim()
    bai3.giai_dh()
    bai4.giai_nh()
    bai5.giai_tp()
if __name__=='__main__':
    main()