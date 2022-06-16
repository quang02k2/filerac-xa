#
# # Bài 1
# #
# # Viết chương trình, cho phép người dùng nhập vào một dãy số cách nhau bằng dấu phẩy. In ra tổng của các số đã nhập.
# #
# # Ví dụ, với dãy đầu vào là 1,2,3,4,5 thì tổng được in ra là 15
# #
#
#
print(sum([int(x) for x in input("nhap gia tri ").split(",") ]))
#
#
#
# # Xem đáp án
# # Bài 2
# #
# # Viết chương trình, cho người dùng nhập vào một xâu. In ra xâu đã nhập với tất cả các ký tự được viết hoa.
# #
# # Ví dụ khi nhập xâu “Hôm nay tôi hạnh phúc” thì kết quả in ra là “HÔM NAY TÔI HẠNH PHÚC”
# #
#
print((lambda a: a.upper())(input()))
#
# # Xem đáp án
# # Bài 3
# #
# # Viết chương trình, cho người dùng nhập vào một dãy số cách nhau bằng khoảng trắng.\
# # In ra danh sách chứa các số đó theo thứ tự tăng dần với các phần tử trùng lặp bị loại bỏ.
# #
print(sorted(list(set([ int(x) for x in input().split(" ")]))))
# # INPUT: 12 3 4 43 95 37 40 85
# #
# # OUTPUT: [3, 4, 12, 37, 40, 43, 85, 95] Xem đáp án
# #
# # Bài 4
# #
# # Nhập vào một dãy số nhị phân ngăn cách bởi dấu phẩy, in ra tổng của chúng trong hệ 16.
# #
# # Ví dụ:
# #
# # INPUT: 11100,10101,10001,1000000
# #
# # OUTPUT: 0x82
#
print(hex(sum(int(x) for x in input("nhap vao day so nhi phan: ").split(','))))
#
# # Xem đáp án
# # Bài 5
# #
# # Viết chương trình, cho nhập vào một số, in ra số chữ số của số vừa nhập.
# #
# # Ví dụ:
# #
# # INPUT: 4327897457386923405430
# # OUTPUT: 22
print(len(input()))
# # Xem đáp án
# # Bài 6
# #
# # Nhập vào một dãy số nguyên cách nhau bằng dấu phẩy, in ra giá trị lớn nhất của dãy số đó.
# # Hi vọng bạn sẽ làm được bài này mà không phải suy nghĩ nhiều.
# #
# print()
#
print(max((int(x) for x in input("nhap fia tri: ").split(","))))
#
# In toàn bộ các số chẵn từ 1000 đến 2000.
#
print(x for x in range(1000, 2001) if x % 2 == 0)
# Xem đáp án
# Bài 2
#
# Nhập một số, in ra giai thừa của số đó. Lưu ý: Không sử dụng vòng lặp trong bài tập này.
#
#
# Bài 3
#
# Nhập một số n, hãy tạo ra dictionary chứa các phần tử dạng i:i*2 với (i chạy từ 1 đến n) và in ra dictionary đó.
# Ví dụ với n là 3 thì đầu ra sẽ là: {1: 2, 2: 4, 3: 6}
#
n = int(input("nhap n: "))
d = dict()
for i in range(n):
    d[i] = i*2
print(d)
# Bài 4
#
# Nhập vào một dãy số ngăn cách bởi dấu phẩy, hãy tạo và in ra một list và một tuple từ các số đó. Sự khác nhau giữa list và tuple là gì?
#
print(list(map(int, input("nhap day so").split(","))))
print(tuple(map(int, input("nhap day so").split(","))))
# # Xem đáp án
# Bài 5
#
# Viết hàm tính giá trị bình phương một số. Lưu ý: phải sử dụng toán tử **
def tinh(n):
    b = n**n
    return b
a = int(input("nhap a: "))
print(tinh(a))
# Xem đáp án
# Bài 6
#
# Định nghĩa một class đơn giản để biểu diễn một đàn gà. Trong đó có 2 phương thức:
#
class DANGA:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def gamecon(self):
        print("nhap so luong ga me: {}".format(self.a))
        print("nhap so luong ga con: {}".format(self.b))
    def nang(self):
        print("ga me nag {}".format(self.c))
a = DANGA(3,4,2)
print(a.gamecon())
print(a.nang())

#
# Viết chương trình, cho phép người dùng nhập vào một dãy số cách nhau bằng dấu phẩy. In ra tổng của các số đã nhập.
#
# Ví dụ, với dãy đầu vào là 1,2,3,4,5 thì tổng được in ra là 15


print(sum((list([int(x) for x in input("nhap day so: ").split(",")]))))
#
# Xem đáp án
# Bài 2
#
# Viết chương trình, cho người dùng nhập vào một xâu. In ra xâu đã nhập với tất cả các ký tự được viết hoa.
#
# Ví dụ khi nhập xâu “Hôm nay tôi hạnh phúc” thì kết quả in ra là “HÔM NAY TÔI HẠNH PHÚC”

print((lambda a: a.upper())(input("nhap: ")))
#
# Xem đáp án
# Bài 3
#
# Viết chương trình, cho người dùng nhập vào một dãy số cách nhau bằng khoảng trắng.
# In ra danh sách chứa các số đó theo thứ tự tăng dần với các phần tử trùng lặp bị loại bỏ.

print(sorted(list(set([int(x) for x in input("nhap day so: ").split(" ")]))))
#
# INPUT: 12 3 4 43 95 37 40 85
#
# OUTPUT: [3, 4, 12, 37, 40, 43, 85, 95] Xem đáp án
#
# Bài 4
#
# Nhập vào một dãy số nhị phân ngăn cách bởi dấu phẩy, in ra tổng của chúng trong hệ 16.

print(hex(sum(int(x) for x in input("nhap day so: ").split(","))))

# INPUT: 11100,10101,10001,1000000
#
# OUTPUT: 0x82
#
# Xem đáp án
# Bài 5
#
# Viết chương trình, cho nhập vào một số, in ra số chữ số của số vừa nhập.

print(len( input("nhap day so: ")))

# INPUT: 4327897457386923405430
#
# OUTPUT: 22
#
# Xem đáp án
# Bài 6

# Nhập vào một dãy số nguyên cách nhau bằng dấu phẩy, in ra giá trị lớn nhất của dãy số đó.
# Hi vọng bạn sẽ làm được bài này mà không phải suy nghĩ nhiều.
#
# Ví dụ:

# INPUT: 19,238,45,1929,232,639
print(max(int(x) for x in input("nhap day so ").split(",")))
# OUTPUT: 1929


