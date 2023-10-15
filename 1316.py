a = int(input())
cnt = a

for i in range(a):
  s = input()
  for j in range(len(s) - 1):
    if s[j] == s[j + 1]:
      continue
    elif s[j] in s[j + 1:]:
      cnt = cnt - 1
      break

print(cnt)
