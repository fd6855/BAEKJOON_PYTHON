a = int(input())
so = 2
while a >= so:
  if a % so == 0:
    print(so)
    a /= so
  else:
    so += 1
