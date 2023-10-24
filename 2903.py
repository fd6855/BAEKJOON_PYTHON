n = int(input())

a = 1
res = 2
for i in range(n):
  res += a
  a *= 2
print(res * res)
