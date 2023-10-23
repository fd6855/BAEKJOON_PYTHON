n = int(input())
a = [[0]*4 for _ in range(n)]
for i in range(n):
  a[i]=int(input())

for i in range(n):
  qu,da,ni,pe=0,0,0,0
  while a[i]>=25:
    qu+=1
    a[i]-=25
  while a[i]>=10:
    da+=1
    a[i]-=10
  while a[i]>=5:
    ni+=1
    a[i]-=5
  while a[i]>=1:
    pe+=1
    a[i]-=1
  print(qu,da,ni,pe)