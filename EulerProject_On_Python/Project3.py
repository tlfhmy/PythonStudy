
n = int(input("Please enter a number:"))

while(n % 2 == 0):
    n /= 2
j = 3
while(n > j):
    if(n % j == 0):
        n = n / j
    else:
        j = j + 2
print(int(n))