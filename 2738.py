N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
B = [[0] * M for _ in range(N)]
for i in range(N):
  A[i] = input().split()
for i in range(N):
  B[i] = input().split()

for i in range(N):
  for j in range(M):
    print(int(A[i][j]) + int(B[i][j]), end=" ")
  print()
