voca = input()
res = 1
l = len(voca)
for i in range(l):
  if i == 0:
    x = voca[:1]
    y = voca[-1:]
  else:
    x = voca[i:i + 1]
    y = voca[-(i + 1):-(i)]
  if x == y:
    continue
  else:
    res = 0
print(res)
