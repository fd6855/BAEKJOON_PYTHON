a_1,a_0 = map(int,input().split())
c = int(input())
n_0 = int(input())

i=n_0

if a_1*i+a_0<=c*i and c>=a_1:
    cnt = 1
else: 
  cnt = 0

print(cnt)
