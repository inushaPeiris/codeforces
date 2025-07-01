from math import floor

input = str(input())
x = input.split(' ')
sqrs = int(x[0]) * int(x[1])

if (sqrs % 2 == 0):
  print(floor(sqrs / 2))
else:
  print(floor((sqrs - 1) / 2))
