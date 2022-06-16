


# with open('MO.inp','r') as f:
#     a = f.readline()
#     b = f.readline()
# lst = list(map(int,b.split()))
# aa = []
# for i in lst:
#     c = lst.count(i)
#     aa.append(c)
# d = max(aa)
# cc = aa.index(d)
# dd = str(d) + " " + str(lst[cc])
# with open('MO.OUT','w') as ff:
#     ff.write(dd)



with open('MO.inp','r') as f:
    a = f.readline()
    b = f.readline().split()
aa = max(b,key=b.count)
solan = b.count(aa)
d = str(solan) + ' '+ str(aa)
with open('MO.OUT','w') as ff:
    ff.write(d)




























