a = input()
a = a.lower()
ma = 0
c = []
for i in set(a):
  if a.count(i)>=ma:
    ma=a.count(i)
    b=i
    c.append(ma)
if c.count(max(c))>1 :
    b="?"
print(b.upper())