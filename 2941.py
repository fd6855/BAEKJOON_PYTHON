word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
cnt = 0
for i in word:
  if i in a:
    a = a.replace(i, '*')

print(len(a))
