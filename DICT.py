import numpy as np

# d = {
#     'ja' : 3,
#     'ew' : 4,
#     'choi'   : 7
# }

## dictname.clear() :  xóa tất cả phần tử, resert lại dict
# d.clear()
# print(d)


## dictname.copy()  : copy dict()
# d.copy()
# print(d)


## dictname.fromkeys(seq[, value]) : tạo dict, sử dụng phần tử trong list làm key,
## và có giá trị khởi tạo tương ứng
# g = d.fromkeys('a','da')
# print(g)




## dictname.get(value, default = none): return giá trị tương ứng với key,
## nếu không có giá trị đó thì return defaui

# a = d.get('3')
# print(a)


## key in dictname : nếu key có trong dict, return True, nếu không return Flase


## dictname.items() : retrun các phần tử dưới dạng list

## dictname.keys() : gọi tất các keys, trả về dưới dạng list


# dictname.setdefault(value,default = none) : giống get
## nhưng nếu ko có keys thì tự động thêm keys và thiết lập giá trị tồn tại theo default



## dictname.update(dictname2): thêm giá trị dict2 vào dict

## dictname.pop(keys[,default]) : popup valueđối với keys đồng thời xóa value đó


## dictname.popitem()  : popup cặp key/value cuối cùng, đồng thời xóa cặp đó trong dict




# def nhap():
#     d ={}
#     a = 0
#     n = int(input('nhap so dict can điền: '))
#     while True:
#         user = input("nhap vao user: ")
#         password =input("nhap vao pass: ")
#         d[user] = password
#         a += 1
#         if a == n:
#             break
#         # n = input("bấm phím bất kỳ để tiếp tục nhập , nếu không, bấm k để thoát")
#         # if n=="6":
#         #     break
#     return d
# a = nhap()
# print(a)






# BT 1

#
# dic = {
#     'user 1': '123',
#     'user 2': '123',
#     'user 3': '123',
#     'user 4': '123',
#     'user 5': '123',
#     'user 6': '123',
#     'user 7': '123',
#     'user 8': '123'
#
# }
#
# def nhap(dic,n,m):
#
#     if n not in dic:
#         print('ko ton tai')
#     elif m not in dic[n]:
#         print('ko dung mat khau ')
#     else:
#         print('ban da dung ')
#
#
# user = input('nhap keys: ')
# password = input('nhap value: ')
# a = nhap(dic,user,password)
# print(a)










# BT  2


# dict_01 = {
#     "A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
#     "H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
#     "O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
#     "V":4,"W":4,"X":8,"Y":4,"Z":10
# }
# def nhap(x):
#     a = []
#     for i in x.values():
#         a.append(str(i))
#     return a
# def nhax(x):
#     a = []
#     for i in x.keys():
#         a.append(i)
#     return a
# def tong(x):
#     s = 0
#     for i in x.values():
#         s += i
#     return s
# def chuyendoi(x):
#     c = ''
#     n = input('nhap sau ki tu: ')
#     m = n.upper()
#     for i in m:
#         if i == ' ':
#
#
# a = nhap(dict_01)
# print(a)
# b = nhax(dict_01)
# print(b)
# c = ' '.join(b)
# print(c)
# d = ' '.join(a)
# print(d)
#
# s = tong(dict_01)
# print(s)
# aa = chuyendoi(dict_01)
# print(aa)
















# BT 3


# d=[{"name":"Tuan","phone":"555-1414","email":"galailaptrinh@gmail.com"},
#     {"name":"Hung","phone":"555-1618","email":"galaixapxinh@gmail.com"},
#     {"name":"Trung","phone":"555-3141","email":""},
#     {"name":"Hoang","phone":"555-2718","email":"loli@gmail.com"}
# ]
# so 8 va email rong
# def tach(d):
#     for i in d:
#         check_so= i['phone']
#         if check_so[-1] == '8':
#             name = i['name']
#             phone = i['phone']
#             email = i['email']
#             print('name: ',name)
#             print('phone: ',phone)
#             print('email: ',email)
#             print('-'*20)
#
# def check(d):
#     for j in d:
#         check_email = j['email']
#         if check_email == "":
#             name = j['name']
#             phone = j['phone']
#             email = j['email']
#             print('name: ',name)
#             print('phone: ',phone)
#             print('email: ',email)
#             print('-'*20)
# a = tach(d)
# print(a)
# b = check(d)
# print(b)






















# BT 4

mybooks=[
{"Title": "Android App Development", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "25000","Published_Year": "2017"},
{"Title": "Python", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "23000", "Published_Year": "2019"},
{"Title": "JavaScript", "Author": "Pham Dieu",
"Publisher": "SSS", "Price": "38000","Published_Year": "2018"},
{"Title": "HTML5", "Author": "Man Nhi",
"Publisher": "HCM", "Price": "33000", "Published_Year": "2012"},
{"Title": "Compiler", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "24000","Published_Year": "2011"},
{"Title": "C language", "Author": "Man Nhi",
"Publisher": "SSS", "Price": "29000","Published_Year": "2010"},
{"Title": "Programming Linguistics", "Author": "Pham Dieu",
"Publisher": "HCM","Price": "41000", "Published_Year": "2009"},
{"Title": "C# language", "Author": "Thanh Tran",
"Publisher": "VNU", "Price": "42000","Published_Year": "2013"},
{"Title": "App Inventor", "Author": "Man Nhi",
"Publisher": "LD", "Price": "30000","Published_Year": "2015"},
]


def chon():
    x = 1
    while x == 1:
        a = input('''chon thu ban can tim:
            1: Title
            2: Publisher
            3: Author 
            BAN CHON : ''' )
        if a=='1':
            key = 'Title'
            break
        elif a=='2':
            key = 'Publisher'
            break
        elif a=='3':
            key = 'Author'
            break
        else:
            x=1
    return key

def ham(d,x):
    xx = 1
    a = 0
    n = input('nhap key ma ban muon: ')
    while xx == 1:
        for i in d:
            if n == i[x]:
                Title = i['Title']
                Publisher = i['Publisher']
                Author = i['Author']
                Price = i['Price']
                Published_Year = i['Published_Year']
                print('Title: ',Title)
                print('Publisher: ',Publisher)
                print('Author: ',Author)
                print('Price: ',Price)
                print('Published_Year: ',Published_Year)
                print('*'*25)
                a +=1
        if a== 0:
            nhap = input('''ban da sai
                            ban co the nhao y or Y de tiep tuc
                            ban chon :  ''')
            if nhap =='Y' or nhap == 'y':
                break
            xx = 1





a = chon()
print(a)
b = ham(mybooks,a)
print(b)
































