grade = ['0'] * 20
abc = ['0'] * 20
for i in range(20):
  tmp = input().split()
  grade[i] = tmp[1]
  if tmp[2] == 'A+':
    abc[i] = 4.5
  elif tmp[2] == 'A0':
    abc[i] = 4.0
  elif tmp[2] == 'B+':
    abc[i] = 3.5
  elif tmp[2] == 'B0':
    abc[i] = 3.0
  elif tmp[2] == 'C+':
    abc[i] = 2.5
  elif tmp[2] == 'C0':
    abc[i] = 2.0
  elif tmp[2] == 'D+':
    abc[i] = 1.5
  elif tmp[2] == 'D0':
    abc[i] = 1.0
  elif tmp[2] == 'F':
    abc[i] = 0.0
  elif tmp[2] == 'P':
    abc[i] = 'P'
sum = 0
cnt = 0

for i in range(20):
  if abc[i] != 'P':
    sum += float(grade[i]) * float(abc[i])
    cnt += float(grade[i])
result = round(sum / cnt, 6)
print(result)
