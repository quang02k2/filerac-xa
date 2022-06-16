import numpy as np
import pandas as pd

#
# def sinh_vien(x):
#     with open(x,'a') as f:
#         while True:
#             name = input('nhap ten sinh vien: ')
#             if name =='':
#                 break
#             date = input('tuoi: ')
#             masv = input('ma sinh vien: ')
#             clas = input('lop: ')
#             diem = input('diem: ')
#             f.write('\t'.join([name,date,masv,clas,diem])+'\n')
#     with open(x,'r') as f:
#         sv = pd.read_csv(f,sep='\t',names=['ten','tuoi','masv','lop','diem'])
#         sap_xep = sv.sort_values(['diem'])
#         n = input('tuoi : ')
#         m = input('diem : ')
#         truy_xuat = sv.query(f'tuoi == {n} or diem == {m}')
#         return sv,sap_xep,truy_xuat
# a,b,c = sinh_vien('D:\WEDD\ha.txt')
#
# print(a)
# print(b)
# print(c)












# class sieu_nhan():
#     stt = 1
#     so_thu_tu = 1
#     suc_manh = 30
#     def __init__(self,mau,tuoi,vu_khi,cao):
#         self.stt = sieu_nhan.so_thu_tu
#         sieu_nhan.so_thu_tu += 1
#         self.mau = 'sieu nhan mau ' + mau
#         self.tuoi = tuoi
#         self.vu_khi = vu_khi
#         self.cao = cao
#
#     @staticmethod
#     def batdau():
#         print('1,2,3: sieu nhan xuat hien')
#     def xuat(self):
#         return (f' so thu tu: {self.stt}  - {self.mau} -  tuoi {self.tuoi} - vu khi {self.vu_khi} - cao {self.cao} ')
#     @classmethod
#     def chuyen_doi(cls,s):
#         cls.suc_manh = s
#         return s
#
# class SIEU_NHAN_A(sieu_nhan):
#     suc_manh = 20
#     def __init__(self,mau,tuoi,vu_khi,cao,love):
#         super().__init__(mau,tuoi,vu_khi,cao)
#         self.love = love
#     def xuatA(self):
#         return (SIEU_NHAN_A.xuat(self) + '-  tinh yeu cau sieu nhan: {}'.format(self.love))
#
# a = SIEU_NHAN_A('DO','20','KIEM','1M65','SIU NHAN')
# b = SIEU_NHAN_A('VANG','22','DAO','1M70','YEU QUAI')
# # print(a.xuat() +'-'+ a.xuatA())
# # print(a.__dict__)
# print(a.xuatA())
# print(b.xuatA())
# print(b.__dict__)




# nhapp











