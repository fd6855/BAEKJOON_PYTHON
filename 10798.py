a = [["-"] * 15 for _ in range(5)]
k = [0] * 5
for i in range(5):
  a[i] = input()
  k[i] = len(a[i])

for j in range(15):
  for i in range(5):
    if j < k[i]:
      print(a[i][j], end="")
