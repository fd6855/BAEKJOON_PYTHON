a,b,c,d,e,f=map(int,input().split())

if c*e>f*b:
  x=(c*e-f*b)/(a*e-d*b)
else:
  x=(f*b-c*e)/(d*b-a*e)

if c*d>f*a:
  y=(c*d-f*a)/(b*d-e*a)
else:
  y=(f*a-c*d)/(e*a-b*d)

print(int(x),int(y))