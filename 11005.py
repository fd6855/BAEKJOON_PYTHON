num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, input().split())
s = ''
while n:
  s += str(num_list[n % b])
  n //= b
print(s[::-1])
