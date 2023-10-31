res = []

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  if a >= b:
    if a % b == 0:
      res.append("multiple")
    else:
      res.append("neither")
  else:
    if b % a == 0:
      res.append("factor")
    else:
      res.append("neither")
for i in res:
  print(i)
