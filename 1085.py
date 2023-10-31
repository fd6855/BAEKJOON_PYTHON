x, y, w, h = map(int, input().split())

min_x = x
min_y = y

if x > w - x:
  min_x = w - x
if y > h - y:
  min_y = h - y
if min_x > min_y:
  print(min_y)
else:
  print(min_x)
