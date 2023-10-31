res = []
while True:
  a = int(input())
  if a == -1:
    break
  cnt = 0
  tmp = ""
  tmp += str(a) + " = "
  for i in range(1, a):
    if a % i == 0:
      cnt += i
      tmp += str(i) + " + "
  if cnt == a:
    res.append(tmp)
  else:
    res.append(str(a) + " is NOT perfect.")

for i in res:
  if "+" in i:
    print(i[:len(i) - 2])
  else:
    print(i)
