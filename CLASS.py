


class Item():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
a = Item('dienthaoi',200,2)
b = Item('laptop',2000,4)
print('mat hang ',a.price)



class sv():
    def __init__(self,name,masv,Village):
        self.name = name
        self.masv = masv
        self.Village = Village
    def gia(self):
        return self.masv*2
    def xuat(self):
        return (' ten sv: {} \n ma sinh vien: {} \n Que quan : {}'.format(self.name,self.masv,self.Village))
    # phuong thuc tinh
    @staticmethod
    def chech(mav):
        if mav < 200:
            return 'cho la ban con tre'
        else:
            return 'ban da gia roi'
a = sv('Vu Duc Quang',2020,'Hung Yen')
print(a.xuat())
print(a.gia())
print(a.chech(2000))
















class sv():
    def __init__(self,name: str,masv: float,Village=''):
        self.name = name
        self.masv = masv
        self.Village = Village
        # gán kiểm tra điều kiện thuộc tính
        assert masv >0
    def gia(self):
        return self.masv*2
    def xuat(self):
        return (' ten sv: {} \n ma sinh vien: {} \n Que quan : {}'.format(self.name,self.masv,self.Village))
    # phuong thuc tinh
    @staticmethod
    def chech(mav):
        if mav < 200:
            return 'cho la ban con tre'
        else:
            return 'ban da gia roi'
a = sv('Vu Duc Quang',2020,'Hung Yen')
b= sv('Nguyen Van Minh',2)
print(a.xuat())
print(a.gia())
print(a.chech(2000))
print(a.chech(a.masv))
print(b.xuat())






### TÍNH KẾ THỪA

class SIEUNHAN():
    sucmanh = 50
    stt = 0
    so_thu_tu = 0
    def __init__(self,name: str,date: int,clor = ''):
        self.name = name
        self.date = date
        self.clor = clor
        assert date >= 0
        self.stt = SIEUNHAN.so_thu_tu
        SIEUNHAN.so_thu_tu += 1
    def suc(self):
        return (f'so thu tu cua ta la: {self.stt} \n ten sieu nhan:  {self.name} \n tuoi siu nhan: {self.date} \n tinh cach : {self.clor} \n suc manh cua ta la {self.sucmanh} ')

a = SIEUNHAN('SIEU NHAN DO ',20,'VUI')
b = SIEUNHAN('SIEU NHAN VANG',30,'HAHA')
print(a.suc())
b.sucmanh = 20
print(b.suc())













class SIEUNHAN():
    sucmanh = 50
    stt = 0
    so_thu_tu = 0
    def __init__(self,name: str,date,clor = ''):
        self.name = name
        self.date = date
        self.clor = clor
        self.stt = SIEUNHAN.so_thu_tu
        SIEUNHAN.so_thu_tu += 1
    def suc(self):
        return (f'so thu tu cua ta la: {self.stt} \n ten sieu nhan:  {self.name} \n tuoi siu nhan: {self.date} \n tinh cach : {self.clor} \n suc manh cua ta la {self.sucmanh} ')
    @classmethod
    def chuyendoi(cls,s):
        lis = s.split('-')
        new = (st.strip() for st in lis)
        name, date, clor = new
        return cls(name,date,clor)
    @classmethod
    def sucmanhx(cls,smanh):
        cls.sucmanh = smanh


x = 'hai-20-hah'
a = SIEUNHAN.chuyendoi(x)
a.sucmanhx(40)
print(a.suc())













#### TẠO LỚP KẾ THỪA




class SIEUNHAN():
    sucmanh = 50
    stt = 0
    so_thu_tu = 0
    def __init__(self,name: str,date,clor):
        self.stt = SIEUNHAN.so_thu_tu
        SIEUNHAN.so_thu_tu += 1
        self.name = name
        self.date = date
        self.clor = clor
    def suc(self):
        return (f'so thu tu cua ta la: {self.stt} \n ten sieu nhan:  {self.name} \n tuoi siu nhan: {self.date} \n tinh cach : {self.clor} \n suc manh cua ta la {self.sucmanh} ')
    @classmethod
    def chuyendoi(cls,s):
        lis = s.split('-')
        new = (st.strip() for st in lis)
        name, date, clor = new
        return cls(name,date,clor)
class SIEUNHANA(SIEUNHAN):
    sucmanh = 40
    def __init__(self,name,date,clor,suc_manh):
        super().__init__(name,date,clor)
        self.nangluc = suc_manh
    @classmethod
    def sucmanhx(cls, smanh):
        cls.sucmanh = smanh

b = SIEUNHANA('sieu nhanh do',50,'vui ve',21)
print(b.sucmanh)
b.sucmanhx(20)
print(b.sucmanh)
print(b.__dict__)


















class SIEUNHAN():
    sucmanh = 50
    stt = 0
    so_thu_tu = 0
    def __init__(self,name: str,date,clor):
        self.stt = SIEUNHAN.so_thu_tu
        SIEUNHAN.so_thu_tu += 1
        self.name = name
        self.date = date
        self.clor = clor
    def a(self):
        return f'so thu tu cua ta la: {self.stt} ,ten sieu nhan:  {self.name} , tuoi siu nhan: {self.date} , tinh cach : {self.clor} , suc manh cua ta la {self.sucmanh} '
#     @classmethod
    def chuyendoi(cls,s):
        lis = s.split('-')
        new = (st.strip() for st in lis)
        name, date, clor = new
        return cls(name,date,clor)
class SIEUNHANA(SIEUNHAN):
    sucmanh = 40
    def __init__(self,name,date,clor,suc_manh):
        super().__init__(name,date,clor)
        self.nangluc = suc_manh
    @classmethod
    def sucmanhx(cls, smanh):
        cls.sucmanh = smanh

b = SIEUNHAN('sieu nhanh do',50,'vui ve')
print(b.a)
print(b.__dict__)



















class sinh_vien():
    def __init__(self,ho,ten):
        self.ho = ho
        self.ten = ten
        self.email = ho + ten + '@gmail.com'
    def ho_va_ten(self):
        return (self.ho + self.ten + '@gmail.com')

a = sinh_vien('duc','quang')
a.ho = 'vu'
a.ten = 'minh'
print(a.ho)
print(a.ten)
print(a.email)
print(a.ho_va_ten())






class sinh_vien():
    def __init__(self,ho,ten):
        self.ho = ho
        self.ten = ten
    def ho_va_ten(self):
        return (self.ho + self.ten )
    @property
    def emai(self):
        return (self.ho + self.ten + '@gmail.com')

a = sinh_vien('duc','quang')
a.ho = 'vu'
a.ten = 'minh'
print(a.ho)
print(a.ten)
print(a.emai)
print(a.ho_va_ten())










class sinh_vien():
    def __init__(self,ho,ten):
        self.ho = ho
        self.ten = ten
    @property
    def ho_va_ten(self):
        return (self.ho + self.ten )
    @property
    def emai(self):
        return (self.ho + self.ten + '@gmail.com')
    @ho_va_ten.setter
    def ho_va_ten(self,ten_moi):
        ho_moi, ten_m= ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_m

a = sinh_vien('duc','quang')
a.ho_va_ten = 'duc quang'
print(a.ho_va_ten)











class sinh_vien():
    def __init__(self,ho,ten):
        self.ho = ho
        self.ten = ten
    @property
    def ho_va_ten(self):
        return (self.ho + self.ten )
    @property
    def emai(self):
        return (self.ho + self.ten + '@gmail.com')
    @ho_va_ten.setter
    def ho_va_ten(self,ten_moi):
        ho_moi, ten_m= ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_m
    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print('da xoa')

a = sinh_vien('duc','quang')
a.ho_va_ten = 'duc quang'
print(a.ho_va_ten)
del a.ho_va_ten
print(a.ho)
print(a.ten)
import os


class nhap():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return ('{}, {}'.format(self.x,self.y))
    def __add__(self, other):
        x = self.x +other.x
        y = self.y + other.y
        return x,y
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return x,y
    def __mul__(self, other):
        x = self.x * other.x
        y = self.y + other.y
        return x,y
    def __pow__(self, power, modulo=None):
        x = self.x ** power.x
        y = self.y ** power.y
        return x,y
    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return x,y
    def __floordiv__(self, other):
        x = self.x // other.x
        y = self.y // other.y
        return x,y
    def __mod__(self, other):
        x = self.x % other.x
        y = self.y % other.y
        return x,y


a = nhap(int(2),int(3))
b = nhap(4,5)
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(b//a)
print(b%a)





















































































