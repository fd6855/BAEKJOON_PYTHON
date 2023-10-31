def cou(a):
  cnt = 0
  for i in range(1, a + 1):
    if a % i == 0:
      cnt += 1
  if cnt == 2:
    return 1
  else:
    return 2


M = int(input())
N = int(input())
sum = 0
cnt = 0
for i in range(M, N + 1):
  if cou(i) == 1:
    sum += i
    if cnt == 0:
      cnt = i

if cnt == 0:
  print("-1")
else:
  print(sum)
  print(cnt)
