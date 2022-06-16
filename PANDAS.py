import pandas as pd

def nhap(x):

    with open(x,'a') as f:
        while True:

            name = input('nhap ten sv: ')
            if name =='':
                break
            date = input('nhap tuoi sinh vien: ')
            masv = input("nhap ma sv: ")
            clas = input('nhap lop : ')
            print('-' * 20, 'SINH VIEN')
            f.write('\t'.join([name,date,masv,clas]) + '\n')
    with open(x,'r') as f:
        svv = pd.read_csv(f,sep='\t',names = ['ten','tuoi','masv','lop'])
        # sap sep
        ds = svv.sort_values(['tuoi'])
        # trich xuat du lieu
        i = int(input('nhap tuoi: '))
        z = input('nhap lop: ')
        p = svv.query(f'tuoi == {i} or lop == "{z}"')
        # c = svv.query('tuoi == 20 or lop == "a3"')
        # nhập trực tiếp hoặc nhập gán giá trị đều được
        return svv,ds,p

a,b,c = nhap('D:\WEDD\ha.txt')
print(a)
print(b)
print(c)

































