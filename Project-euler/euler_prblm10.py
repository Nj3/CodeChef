n = 2000000

prime = [True for i in range(n+1)]

for i in range(2, int(n**(1/2))):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False

p = []
for i in range(2, n+1):
    if prime[i]:
        p.append(i)

print(sum(p))