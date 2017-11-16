from math import log

n = 10001
limit = int(n * (log(n) + log(log(n))))
prime = [True for i in range(limit+1)]

for i in range(2, int(limit**(1/2))):
    if prime[i]:
        for j in range(i*i, limit+1, i):
            prime[j] = False

p = []
for i in range(2, limit+1):
    if prime[i]:
        p.append(i)
print(p[n-1])
