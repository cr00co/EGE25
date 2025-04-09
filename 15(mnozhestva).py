for x in [k * 0.25 for k in range(-10000, 10000)]:
    P = x in [3,5,7,11,12,15]
    Q = x in [5,6,12,15]
    A = 0 # Если найти нужно наим. - 0, если наиб. - 1
    f = (P <= (not Q)) or A
    if f != 1:
        print(x)