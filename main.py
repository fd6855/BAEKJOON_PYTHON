def count_change(a, b,N,M, chess):
  cnt = 0
  for i in range(a, a+8):
    for j in range(b, b+8):
      if i==M or j==N:
        break
      if chess[i][j] == "W":
        if chess[i][j + 1] == "W":
          cnt += 1
          chess[i][j + 1] = "B"
        if chess[i + 1][j] == "W":
          cnt += 1
          chess[i + 1][j] = "B"
      if chess[i][j] == "B":
        if chess[i][j + 1] == "B":
          cnt += 1
          chess[i][j + 1] = "W"
        if chess[i + 1][j] == "B":
          cnt += 1
          chess[i + 1][j] = "W"
  return cnt


N, M = map(int, input().split())
chess = [["" for j in range(M)] for i in range(N)]
for i in range(N):
  a = input()
  for j in range(M):
    chess[i][j] = a[j]
min_res = 2500
res = 2500
for a in range(0, N-8):
  for b in range(0, M - 8):
    res = count_change(a, b,N,M,chess)
  min_res = min(res, min_res)

print(min_res)
