val = []
for i in range(100,1000):
    for j in range(100,1000):
        prod = str(i*j)
        if prod[::] == prod[::-1]:
            val.append(int(prod))
val.sort(reverse = True)
print(val)
print(val[0])