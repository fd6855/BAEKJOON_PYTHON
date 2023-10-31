def cou(a):
  cnt = 0
  for i in range(1, a + 1):
    if a % i == 0:
      cnt += 1
  if cnt == 2:
    return 1
  else:
    return 2


n = int(input())
res = [0] * n
cnt = 0
res = input().split()

for i in res:
  if cou(int(i)) == 1:
    cnt += 1

print(cnt)
