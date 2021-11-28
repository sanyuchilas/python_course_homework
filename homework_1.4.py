n = int(input())
maxNum = -1
while n:
  if n % 10 > maxNum:
    maxNum = n % 10
  n //= 10
print(maxNum)