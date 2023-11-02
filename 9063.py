n = int(input())
xy = [[0] for _ in range(2)] * n
max_x = -10001
min_x = 10001
max_y = -10001
min_y = 10001
for i in range(n):
  a, b = map(int, input().split())
  if a > max_x:
    max_x = a
  if a <= min_x:
    min_x = a
  if b > max_y:
    max_y = b
  if b <= min_y:
    min_y = b

print((max_x - min_x) * (max_y - min_y))
