res=[]
num=[0]*3
while True:
  a,b,c=map(int,input().split())
  if a==0 and b==0 and c==0:
    break
  num[0],num[1],num[2]=a,b,c
  num=sorted(num)
  if num[2]>=num[1]+num[0]:
    res.append("Invalid")
  elif a==b and a==c:
    res.append("Equilateral")
  elif a==b or a==c or b==c:
    res.append("Isosceles")
  else:
    res.append("Scalene")

for i in res:
  print(i)