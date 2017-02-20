prev = 1
curr = 2
fibo = [1,2]
sm = 0
while 1:
    sm = prev+curr
    if sm >= 4000000:
        break
    # print(sm,prev,curr)
    fibo.append(sm)
    prev = curr
    curr = sm
print(fibo)
fibo = [i for i in fibo if i%2==0]
print(sum(fibo))
