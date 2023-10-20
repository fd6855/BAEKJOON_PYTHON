a = [[0] * 9 for _ in range(9)]
for i in range(9):
  a[i] = input().split()
for i in range(9):
  for j in range(9):
    a[i][j] = int(a[i][j])
max_num = max(a[0])
for i in range(9):
  if max_num < max(a[i]):
    max_num = max(a[i])

for i in range(9):
  for j in range(9):
    if max_num == a[i][j]:
      print(max_num)
      print(i + 1, j + 1)
