import math

n = 8
while n % 2 == 0:
    n /= 2
    if n == 1:
        print(2)

for i in range(3, int(math.sqrt(n)), 2):
    while n % i == 0:
        print(i)
        n /= i


if n > 2:
    print(n)