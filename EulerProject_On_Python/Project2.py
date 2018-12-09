a = []
a.append(1)
a.append(1)

i = 1
while(a[i] < 4000000):
    a.append(a[i]+a[i-1])
    i += 1

sum = 0
for n in a:
    if(n % 2 == 0):
        sum += n

print(f"The sum of even-terms of Fibonacci sequence \n which is less than 4 million is {sum}")