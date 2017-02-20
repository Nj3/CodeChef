for c in range(1000):
    for b in range(1000):
        if b<c:
            for a in range(1000):
                if a<b:
                    if a*a + b*b == c*c and a + b + c == 1000:
                        print(a*b*c)
                        break