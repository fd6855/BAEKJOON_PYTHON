N, M = map(int, input().split())
num = [0] * N
num = input().split()

res = 0
for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      tmp = int(num[i]) + int(num[j]) + int(num[k])
      if tmp > M:
        continue
      else:
        res = max(res, tmp)

print(res)
