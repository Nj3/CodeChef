num = 40
flag = False
while 1:
    for i in range(1, 21):
        if num % i == 0:
            if i == 20:
                print(num)
                flag = True
                break
            continue
        break
    if flag:
        break
    elif num > 10**10:
        break
    else:
        num += 20 # since the largest factor is 20