

# round(numbers,ndigits=)

# numbers : so ban muon lam tron
# ndigitis : so chu so ban muon lam tron
#
# a = 1.223
# print(round(a,2))



def sohoanthien(lst):
    o = lst.split(",")
    i = []
    for j in o:
        l=0
        j = int(j)
    for k in range(1,j):
        if j%k==0:
            l+=k
        if j==l:
            i.append(str(j))
    return i
lst = input("Nhập vào dãy số để kiểm tra số hoàn thiện: ")
print(sohoanthien(lst))








