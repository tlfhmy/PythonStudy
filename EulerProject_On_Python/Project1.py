import collections

num3_mult = range(3,1000,3)
num5_mult = range(5,1000,5)

num3_5_mult = list(set(num3_mult) | set(num5_mult))

print(sum(num3_5_mult))
