x, y, w, h = map(int, input().split())

a = w - x
b = h - y
if a > b:
  print(a)
else:
  print(b)
