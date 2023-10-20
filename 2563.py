a = [[0] * 101 for _ in range(101)]
num = int(input())
arr = [[0] * 2 for _ in range(num)]
for i in range(num):
  arr[i] = input().split()

for i in range(num):
  for x in range(int(arr[i][0]), int(arr[i][0]) + 10):
    for y in range(int(arr[i][1]), int(arr[i][1]) + 10):
      a[x][y] += 1
cnt = 0

for i in range(101):
  for j in range(101):
    if a[i][j] >= 1:
      cnt += 1
print(cnt)
