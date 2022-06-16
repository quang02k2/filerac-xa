
import sys
n, m = map(int, input().split())
a = list(map(int, input().split()))
if len(a) < n * m:
    sys.exit()
b = []
ad = []
for i , x in enumerate(a):
    ad.append(x)
if i % m == m - 1:
    b.append(ad)
    ad.clear()
print(b)