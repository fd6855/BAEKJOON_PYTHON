num = int(input())
space = " "
star = "*"

for i in range(1, num + 1):
  print(space * (num - i) + star * (2 * i - 1))

for i in range(num - 1, 0, -1):
  print(space * (num - i) + star * (2 * i - 1))
